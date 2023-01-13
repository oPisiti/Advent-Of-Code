import re
import timeMe
import numpy as np

class Monkey():
    def __init__(self, number: int, items: list[str], op: str,
                 test: int, if_true: int, if_false: int, n_total_items: int):
        self.number        = number
        
        self.items               = np.zeros(n_total_items, dtype=np.ulonglong)
        self.items[0:len(items)] = np.array(items, dtype=np.ulonglong)
        self.items_len           = len(items)

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
        """
        Base inspection for a monkey's items.
        Returns a dictionary with monkeys to receive items as keys
        and items to be received as values.
        """

        items_to_throw = {
            self.if_true:  [],
            self.if_false: []
        }

        for i in range(self.items_len):
            worry_level = self.items[i]
            
            # Operation
            operation = re.findall("\*|\+", self.op)[0]
            operation_num = re.findall("\d+|old$", self.op)[0]
            if operation_num == "old": operation_num = worry_level
            else:                      operation_num = int(operation_num)
            
            match operation:
                case "*": worry_level *= operation_num
                case "+": worry_level += operation_num

            # Testing worry level
            if not (worry_level%self.test): give_to = self.if_true
            else:                           give_to = self.if_false
            
            items_to_throw[give_to].append(worry_level)
            
        
        self.has_inspected += self.items_len
        self.items_len =  0

        return items_to_throw 

    def receive_items(self, items: list[int]) -> None:
        """
        Appends items to a monkey's items list
        """

        if len(items) == 0: return

        print(f"\nMonkey's items before: {self.items}")
        print(f"Received:              {items}")
        print(self.items_len)
        for i, item in enumerate(items):
            print(f"i: {i}")
            self.items[self.items_len + i] = item

        self.items_len += len(items)     

        print(f"After received:        {self.items}\n")   

    def reset_items(self) -> None:
        self.items[:] = 0

@timeMe.timeMe
def main():
    with open("input.txt") as data:
        a = data.read().split("\n\n")
    
    a = [item.splitlines() for item in a]

    # Getting data
    monkeys = []
    n_items = sum([len(list(map(int, re.findall("\d+", items[1])))) for items in a])
    for monkey in a:
        number   = int(re.findall("\d", monkey[0])[0])
        items    = list(map(int, re.findall("\d+", monkey[1])))
        op       = re.findall("new.*", monkey[2])[0]
        test     = int(re.findall("\d+", monkey[3])[0])
        if_true  = int(re.findall("\d+", monkey[4])[0])
        if_false = int(re.findall("\d+", monkey[5])[0])

        monkeys.append(Monkey(number, items, op, test, if_true, if_false, n_items))

    # Playing out the rounds
    n_rounds = 1000
    for round in range(n_rounds):
        # print(f"\n\n ----- Round {round+1} -----")

        for monkey in monkeys:     
            items_to_throw = monkey.inspect()
            
            for monkey_num in items_to_throw:
                # print()
                # print(f"Giving monkey {monkey_num}: {items_to_throw[monkey_num]}")
                monkeys[monkey_num].receive_items(items_to_throw[monkey_num])
            
            monkey.reset_items()

        # for i, mon in enumerate(monkeys):
            # print(f"Monkey {i}'s items:      {mon.items}")    

    print()
    n_inspected = sorted([monkey.has_inspected for monkey in monkeys], reverse=True)
    print(f"\nInspections: {n_inspected}")
    print(f"Level of monkey business: {n_inspected[0]*n_inspected[1]}")


if __name__ == '__main__':
    main()