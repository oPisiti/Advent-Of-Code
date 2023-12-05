import re

class Monkey():
    def __init__(self, number: int, items: list[str], op: str,
                 test: int, if_true: int, if_false: int):
        self.number        = number
        self.items         = items
        self.op            = op
        self.test          = test
        self.if_true       = if_true
        self.if_false      = if_false
        self.has_inspected = 0
    
    def __repr__(self) -> str:
        return (f"Monkey {self.number}\n"+
                f"  Items: {self.items}\n"+
                f"  Operation: {self.op}\n"+
                f"  Test: divisible by {self.test}\n"+
                f"    If true: throw to monkey {self.if_true}\n"+
                f"    If false: throw to monkey {self.if_false}")


    def inspect(self) -> dict:
        items_to_throw = {
            self.if_true:  [],
            self.if_false: []
        }

        for item in self.items:
            worry_level = item
            
            # Operation
            operation = re.findall("\*|\+", self.op)[0]
            operation_num = re.findall("\d+|old$", self.op)[0]
            if operation_num == "old": operation_num = worry_level
            else:                      operation_num = int(operation_num)
            
            match operation:
                case "*": worry_level *= operation_num
                case "+": worry_level += operation_num

            # Gets bored
            worry_level = int(worry_level/3)

            # Testing worry level
            if not (worry_level%self.test): give_to = self.if_true
            else:                           give_to = self.if_false
            
            items_to_throw[give_to].append(worry_level)
            
        
        self.has_inspected += len(self.items)
        return items_to_throw

    def get_items(self, items: list[int]) -> None:
        for item in items:
            self.items.append(item)

    def reset_items(self) -> None:
        self.items = []


def main():
    with open("input.txt") as data:
        a = data.read().split("\n\n")
    
    a = [item.splitlines() for item in a]

    # Getting data
    monkeys = []
    for monkey in a:
        number   = int(re.findall("\d", monkey[0])[0])
        items    = list(map(int, re.findall("\d+", monkey[1])))
        op       = re.findall("new.*", monkey[2])[0]
        test     = int(re.findall("\d+", monkey[3])[0])
        if_true  = int(re.findall("\d+", monkey[4])[0])
        if_false = int(re.findall("\d+", monkey[5])[0])

        monkeys.append(Monkey(number, items, op, test, if_true, if_false))

    # Playing out the rounds
    n_rounds = 20
    for round in range(n_rounds):
        for monkey in monkeys:     
            items_to_throw = monkey.inspect()
            
            for monkey_num in items_to_throw:
                monkeys[monkey_num].get_items(items_to_throw[monkey_num])
            
            monkey.reset_items()

        print(f"\n ----- After round {round+1} -----")
        for i, mon in enumerate(monkeys):
            print(f"Monkey {i}'s items: {mon.items}")    

    n_inspected = sorted([monkey.has_inspected for monkey in monkeys], reverse=True)
    print(f"\nInspections: {n_inspected}")
    print(f"Level of monkey business: {n_inspected[0]*n_inspected[1]}")


if __name__ == '__main__':
    main()