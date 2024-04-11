from dataclasses import dataclass
from multimethod import multimethod

@multimethod
@dataclass
class vec3d():
    x: int
    y: int
    z: int


@multimethod
class vec3d():
    def __init__(self, arr: list[int]) -> None:
        self.x, self.y, self.z = arr

    def __sub__(self, other) -> None:
        return vec3d(self.x - other.x, self.y - other.y, self.z - other.z)
        

class Brick():
    def __init__(self, a: vec3d, b: vec3d) -> None:
        self.a = a
        self.b = b
        self.min_z = min(self.a.z, self.b.z)
        self.max_z = max(self.a.z, self.b.z)
        
        self.delta = b - a

        self.is_vertical = self.min_z != self.max_z 
        if self.is_vertical:
            common_point = self.a if self.a.z == self.min_z else self.b
            self.z_plane_segment = [common_point, common_point]

        self.support_of_indexes = []
        self.supported_by_count = 0

    def apply_fall(self, d: int) -> None:
        if d < 0: raise ValueError("d must be a positive value")

        if self.min_z - d <= 0: 
            raise ValueError("Final z value would be smaller than 1")

        self.a.z = max(self.a.z - d, 1)
        self.b.z = max(self.b.z - d, 1)
        self.min_z = min(self.a.z, self.b.z)
        self.max_z = max(self.a.z, self.b.z)

    def is_on_top(self, other) -> bool:
        # https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect

        # If is one z plane above
        if other.max_z + 1 != self.min_z: return False

        # Value for comparison
        if self.is_vertical:   
            return min(other.a.x, other.b.x) <= self.a.x <= max(other.a.x, other.b.x) and \
                   min(other.a.y, other.b.y) <= self.a.y <= max(other.a.y, other.b.y)
            
        if other.is_vertical: 
            return min(self.a.x, self.b.x) <= other.a.x <= max(self.a.x, self.b.x) and \
                   min(self.a.y, self.b.y) <= other.a.y <= max(self.a.y, self.b.y)
        
        # Checking for collision
        r, s = self.delta, other.delta
        cross_r_s = cross_product_z_plane(r, s)
        q_p = vec3d(self.a.x - other.a.x, self.a.y - other.a.y, 0)
        cross_qp_r = cross_product_z_plane(q_p, r)
        cross_qp_s = cross_product_z_plane(q_p, s)

        # Parallel
        if cross_r_s == 0:
            # Collinear and overlapping ?
            if self.a.x == other.a.x:
                return min(self.a.y, self.b.y) <= other.a.y <= max(self.a.y, self.b.y) or \
                       min(self.a.y, self.b.y) <= other.b.y <= max(self.a.y, self.b.y)
            else:
                return min(self.a.x, self.b.x) <= other.a.x <= max(self.a.x, self.b.x) or \
                       min(self.a.x, self.b.x) <= other.b.x <= max(self.a.x, self.b.x)
                  
        t = abs(cross_qp_s / cross_r_s)
        u = abs(cross_qp_r / cross_r_s)

        # Collide
        if cross_r_s != 0:
            return 0 <= t <= 1 and 0 <= u <= 1        
        
        return False 


def cross_product_z_plane(a: vec3d, b: vec3d) -> int:
    return a.x * b.y - a.y * b.x


def main():
    # Dealing with input data
    with open("input.txt") as f:
        data = f.read().strip().split("\n")
    
    bricks = []
    for d in data:
        coords = [[int(c) for c in e.split(",")] for e in d.split("~")]
        
        bricks.append(Brick(vec3d(coords[0]), vec3d(coords[1])))

    bricks.sort(key=lambda x: x.min_z)

    # Applying physics to all blocks
    for i in range(len(bricks)):
        apply_physics(bricks, i)

    # bricks.sort(key=lambda x: x.min_z)
        

    # Determining how many bricks support a given brick
    desintegratable_count = 0
    for i in range(len(bricks)):
        is_desin = True

        for index in bricks[i].support_of_indexes:
            if bricks[index].supported_by_count <= 1:
                is_desin = False
                break

        if is_desin: 
            desintegratable_count += 1 

    print(f"{desintegratable_count = }")
    pass


def apply_physics(bricks: list[Brick], index: int) -> None:
    while True:
        if bricks[index].min_z == 1: return   
        
        # Collision between current brick and one below
        has_collided = False
        for i in range(index):
            if bricks[index].is_on_top(bricks[i]):
                bricks[i].support_of_indexes.append(index)
                bricks[index].supported_by_count += 1
                has_collided = True
        
        if has_collided: return

        bricks[index].apply_fall(1) 
        


if __name__ == '__main__':
    main()