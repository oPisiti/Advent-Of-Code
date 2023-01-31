from multipledispatch import dispatch

class vec3d():
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def set_all_0(self) -> None:
        self.__init__(0, 0, 0)

    def set_val(self, x, y, z) -> None:
        self.__init__(x, y, z)

    def __mul__(self, scalar: int):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        
        return self


class Moon():
    @dispatch(int, int, int, int ,int ,int)
    def __init__(self, x_: int, y_: int, z_: int, vx_: int, vy_: int, vz_: int) -> None:
        self.x = x_
        self.y = y_
        self.z = z_
        self.vx = vx_
        self.vy = vy_
        self.vz = vz_
    
    @dispatch(list, list)
    def __init__(self, pos: list[int], vel: list[int]) -> None:
        self.__init__(pos[0], pos[1], pos[2], vel[0], vel[1], vel[2])

    @dispatch(list)
    def __init__(self, pos: list[int]) -> None:
        self.__init__(pos, [0, 0, 0])
    
    def __repr__(self) -> str: 
        return f"pos=<x= {self.x}, y= {self.y}, z= {self.z}>, vel=<x= {self.vx}, y= {self.vy}, z= {self.vz}>"

    def put_vel(self, vel) -> None:
        self.vx += vel.x
        self.vy += vel.y
        self.vz += vel.z

    def apply_vel(self) -> None:
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def p_energy(self) -> int:
        return abs(self.x) + abs(self.y) + abs(self.z)

    def k_energy(self) -> int:
        return abs(self.vx) + abs(self.vy) + abs(self.vz)


def apply_gravity_all(moons: list[Moon]) -> None:
    deltaPos  = vec3d(0, 0, 0)
    add_vel_i = vec3d(0, 0, 0)      # Velocities to add according to moon i

    for i in range(len(moons)):
        for j in range(i + 1, len(moons)):
            add_vel_i.set_all_0()
            deltaPos.set_val(moons[i].x - moons[j].x,
                             moons[i].y - moons[j].y,
                             moons[i].z - moons[j].z)

            if   deltaPos.x < 0:  add_vel_i.x =  1
            elif deltaPos.x > 0:  add_vel_i.x = -1
            if   deltaPos.y < 0:  add_vel_i.y =  1
            elif deltaPos.y > 0:  add_vel_i.y = -1
            if   deltaPos.z < 0:  add_vel_i.z =  1
            elif deltaPos.z > 0:  add_vel_i.z = -1

            moons[i].put_vel(add_vel_i)
            moons[j].put_vel(add_vel_i*(-1))

    for moon in moons:  moon.apply_vel()

            
def get_total_energy(moons: list[Moon]) -> int:
    energy = 0

    for moon in moons:
        energy += moon.p_energy() * moon.k_energy()

    return energy
