"""
This is the solution of part of the Advent of Code Challenge 2023
Author: oPisiti
"""

from copy import deepcopy
from enum import Enum
from queue import Queue
import re


class Global:
    low_pulse_count = 0
    high_pulse_count = 0
    queue = Queue()


class Pulse(Enum):
    LOW = 0
    HIGH = 1


class Broadcaster:
    def __init__(self, name: str) -> None:
        self.name = name

    def add_connections(self, connections: str, modules: dict) -> None:        
        self.con = re.findall("\w+", connections)

        # Adding connections that are Conjunctions to their memory
        for c in self.con:
            if isinstance(modules[c], Conjunction):
                modules[c].add_source(self.name)

    def run(self, data: dict, modules: dict) -> None:
        # Adding pulses to count
        if data["pulse"] == Pulse.LOW: Global.low_pulse_count  += 1
        else:                          Global.high_pulse_count += 1

        for c in self.con:
            # Dead end
            if c not in modules.keys():
                if data["pulse"] == Pulse.LOW: Global.low_pulse_count  += 1
                else:                          Global.high_pulse_count += 1
                continue

            Global.queue.put({"came_from": data["to"],
                              "pulse": data["pulse"],
                              "to": c})

class Conjunction:
    def __init__(self, name: str) -> None:
        self.memory = dict()
        self.name = name

    def add_connections(self, connections: str, modules: dict) -> None:
        self.con = re.findall("\w+", connections)
    
    def add_source(self, source: str) -> None:
        self.memory[source] = Pulse.LOW
    
    def run(self, data: dict, modules: dict) -> None:
        # Adding pulses to count
        if data["pulse"] == Pulse.HIGH: Global.high_pulse_count += 1
        else:                           Global.low_pulse_count  += 1

        # Updating memory
        self.memory[data["came_from"]] = data["pulse"]
        
        # HIGH for all in memory -> send LOW to all modules connected
        if all(m == Pulse.HIGH for m in self.memory.values()):
            pulse_value = Pulse.LOW
        
        # -> send LOW to all modules connected
        else:
            pulse_value = Pulse.HIGH

        # Sending the pulses
        for c in self.con:
            # Dead end
            if c not in modules.keys():
                if pulse_value == Pulse.LOW: Global.low_pulse_count  += 1
                else:                        Global.high_pulse_count += 1
                continue

            Global.queue.put({"came_from": data["to"],
                              "pulse": pulse_value,
                              "to": c})

class Flipflop:
    def __init__(self, name: str) -> None:
        self.name = name
        self.state_is_on = False
        
    def add_connections(self, connections: str, modules: dict) -> None:
        self.con = re.findall("\w+", connections)

        # Adding connections that are Conjunctions to their memory
        for c in self.con:
            if isinstance(modules[c], Conjunction):
                modules[c].add_source(self.name)
        
    def run(self, data: dict, modules: dict) -> None:
        # Adding pulses to count
        if data["pulse"] == Pulse.LOW: Global.low_pulse_count  += 1
        else:                          Global.high_pulse_count  += 1

        if data["pulse"] == Pulse.HIGH: return

        self.state_is_on = not self.state_is_on

        # Sending pulses
        if self.state_is_on: pulse_value = Pulse.HIGH
        else:                pulse_value = Pulse.LOW

        for c in self.con:
            # Dead end
            if c not in modules.keys():
                if pulse_value == Pulse.LOW: Global.low_pulse_count  += 1
                else:                        Global.high_pulse_count += 1
                continue

            Global.queue.put({"came_from": data["to"],
                              "pulse": pulse_value,
                              "to": c})
        

class Output:
    def __init__(self) -> None:
        self.count = 0

    def run(self, data: dict, *args) -> None:
        # Adding pulses to count
        if data["pulse"] == Pulse.LOW: Global.low_pulse_count  += 1
        else:                          Global.high_pulse_count += 1


def pulse_propagation():

    with open("input.txt") as f:
        data = f.read().strip().split("\n")

    tokens = [t.split(" -> ") for t in data]
    
    # Creating a dictionary of the modules in which the keys are their names
    # and the values are the corresponding objects
    modules = dict()
    modules["output"] = Output()
    modules["broadcaster"] = Broadcaster("broadcaster")
    for token in tokens:        
        match token[0][0]:
            case "%": modules[token[0][1:]]  = Flipflop(token[0][1:])
            case "&": modules[token[0][1:]]  = Conjunction(token[0][1:])

    # Making the connections between modules
    for token in tokens:        
        match token[0][0]:
            case "%": modules[token[0][1:]].add_connections(token[1], modules)
            case "&": modules[token[0][1:]].add_connections(token[1], modules)
            case "b": modules[token[0]].add_connections(token[1], modules)
            case _:   raise ValueError(f"Unsupported value {token[0]}")

    # Iterating
    original_modules = deepcopy(modules)
    for i in range(1_000):
        Global.queue.put({"came_from": None, "pulse": Pulse.LOW, "to": "broadcaster"})

        # Signal propagation
        while not Global.queue.empty():
            op_info = Global.queue.get()

            modules[op_info["to"]].run(op_info, modules)

    return (Global.low_pulse_count, Global.high_pulse_count, Global.low_pulse_count * Global.high_pulse_count)


if __name__ == '__main__':
    print(pulse_propagation())