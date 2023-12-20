"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

from functools import reduce
import re


class Global:
    comb = 0
    MAX_VALUE = 4000


def aplenty():
    with open("input.txt") as f:
        workflows, parts = f.read().strip().split("\n\n")

    workflow = dict()
    for w in workflows.split("\n"):
        name, data = re.findall("(\w+)\{(.*)\}", w)[0]
        workflow[name] = [rule.split(":") for rule in data.split(",")]

    # Applying the workflows
    possible_values = {k: Global.MAX_VALUE for k in ("x", "m", "a", "s")}

    get_rule_score(workflow, "in", 0, possible_values)

    for i in range(1, len(workflow["in"])):
        update_poss_values(workflow["in"][i-1][0], possible_values, False)
        get_rule_score(workflow, "in", i, possible_values)
    return Global.comb


def get_rule_score(workflow: list[list[str]], rule_name: str, rule_index: int, possible_values: dict) -> int:
    values = possible_values.copy()

    rule = workflow[rule_name][rule_index]

    # Catch-all rule
    if len(rule) == 1: 
        match rule[0]:
            case "R": 
                pass
            case "A": 
                # update_poss_values(rule[0], values)         
                Global.comb += reduce(lambda x, y: x*y, [v for v in values.values()])
                pass
            case _:
                next_rules_name = rule[0]
                for i in range(len(workflow[next_rules_name])):    
                    get_rule_score(workflow, next_rules_name, i, values)            
        
        return

    next_rules_name = rule[1]

    # Found exit rule
    if next_rules_name in ("A", "R"):
        update_poss_values(rule[0], values)         
        Global.comb += reduce(lambda x, y: x*y, [v for v in values.values()])
        return
    
    # Next steps
    get_rule_score(workflow, next_rules_name, 0, values)
    for i in range(1, len(workflow[next_rules_name])):   
        update_poss_values(workflow[next_rules_name][i-1][0], values, False)
        get_rule_score(workflow, next_rules_name, i, values) 
        pass


def update_poss_values(rule: str, possible_values: dict, valid: bool = True) -> None:
    # Parsing the rule
    rule_part, rule_comp, rule_num = re.findall("(\w+)([><])(\d+)", rule)[0]
    
    # Applying       
    if not valid: rule_comp = "<" if rule_comp == ">" else ">"

    if rule_comp == ">":
        possible_values[rule_part] = Global.MAX_VALUE - int(rule_num)
    elif rule_comp == "<":
        possible_values[rule_part] = int(rule_num)


if __name__ == '__main__':
    print(f"{aplenty() = }")