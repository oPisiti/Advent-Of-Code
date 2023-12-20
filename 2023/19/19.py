"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

import re

class Part():
    def __init__(self, data: str):
        cats = re.findall("([xmas]=\d+)", data)
        
        self.attr = dict()
        for cat in cats:
            tokens = cat.split("=")
            self.attr[tokens[0]] = int(tokens[1])


def aplenty():
    with open("input.txt") as f:
        workflows, parts = f.read().strip().split("\n\n")

    parts = [Part(p) for p in parts.split("\n")]
    workflow = dict()
    for w in workflows.split("\n"):
        name, data = re.findall("(\w+)\{(.*)\}", w)[0]
        workflow[name] = [rule.split(":") for rule in data.split(",")]

    # Applying the workflows
    score = 0
    for part in parts:
        rules = workflow["in"]
        found_exit = False

        while True:    
            for rule in rules:
                # Catch-all rule
                if len(rule) == 1: 
                    next_rules_name = rule[0]
                    if rule[0] in ("A", "R"):
                        found_exit = True
                    break
                
                # Parsing the rule
                rule_part, rule_comp, rule_num = re.findall("(\w+)([><])(\d+)", rule[0])[0]
                
                # Applying
                if (rule_comp == ">" and part.attr[rule_part] > int(rule_num)) or \
                   (rule_comp == "<" and part.attr[rule_part] < int(rule_num)):
                    
                    next_rules_name = rule[1]
                
                    # Found exit rule
                    if next_rules_name in ("A", "R"):
                        found_exit = True
                    
                    break
            
            if found_exit:
                if next_rules_name == "A":
                    score += sum([a for a in part.attr.values()])
                break
            else:
                # Changing to the next rule set
                rules = workflow[next_rules_name]
                
    return score

if __name__ == '__main__':
    print(aplenty())