from enum import Enum
class Mode(Enum):
    zero = "Position Mode"     
    one  = "Immediate Mode"     
    two  = "Relative Mode"

class IntCodeComputer():
    def __init__(self, path: str, input_ = 1, prompt_for_inputs = False):
        self.base_opcode       = ...
        self.init_inst_pointer = 0
        
        # Code
        self.path_input  = path
        self.opcode      = ...
        self.read_input_file()        
        
        # How many addresses to jump given each instruction
        # DEFINES valid instructions (except halt instruction)
        self.n_arguments = {    
            1: 3,
            2: 3,
            3: 1,
            4: 1,
            5: 2,   # 5 and 6 (jump if true/false) don't jump 3 positions, but is equivalent to.
            6: 2,   # This is for determining the output address in self.run()
            7: 3,
            8: 3,
            9: 1
        }
        self.jump            = None
        self.inst_pointer    = self.init_inst_pointer

        # Possible instructions
        self.opcode_len = 2         # How many digits for an opcode, i.e. 02, 01, 99 all equal 2
        self.valid_inst = {key for key in self.n_arguments.keys()}
        self.halt_inst  = {99}

        # Memory
        # Given opcode CBAZZ, ABC is the base memory and ZZ is the instruction
        self.memory = {
            "A": None,
            "B": None,
            "C": None
        }
        self.extra_mem = {}

        # Modes
        self.modes_len      = len(self.memory.keys())
        self.inst_max_len   = self.modes_len + self.opcode_len
        self.modes          = [Mode.zero for _ in range(self.modes_len)]
        self.rel_base_off   = 0

        # Used in self.search_memory_on_modes()
        self.n_dereferences = [{Mode.one}, {Mode.zero, Mode.two}]   # Modes in position 0 (mode a) will be dereferenced 0 times        
                                                                    # Modes in position 1 (modes b and c) will be dereferenced once...

        # IO
        self.input         = input_
        self.prompt_inputs = prompt_for_inputs
        self.output        = None

    def run(self, show_outputs=True) -> None:
        """
        Executes opcode
        Output instructions are printed to console if show_outputs == True
        """
        self.show_outputs = show_outputs

        # Determining instruction
        _, curr_inst = self.get_opcode_and_modes(self.opcode[self.inst_pointer])

        while curr_inst not in self.halt_inst:            
            # Instruction and modes
            self.modes, curr_inst = self.get_opcode_and_modes(self.opcode[self.inst_pointer])

            if curr_inst in self.halt_inst:
                return
            if curr_inst not in self.valid_inst:
                raise ValueError(f"Instruction '{curr_inst}' not valid")

            # Setting to Memory         
            for i, key in enumerate(self.memory.keys()):
                mem_index = self.inst_pointer + i + 1
                
                # Simple instructions like 3 and 4 require only memory A to be updated
                if mem_index >= (self.inst_pointer + self.n_arguments[curr_inst] + 1): break

                # Last memory (where to write) should only be dereferenced ONCE at this stage
                # It will be again dereferenced in "operations".
                if i == (self.n_arguments[curr_inst] - 1):
                    self.memory[key] = self.get_from_opcode(mem_index)

                    if self.modes[i] == Mode.two: 
                        self.memory[key] += self.rel_base_off

                    break

                # Instructions that need to read more than one memory address
                match self.modes[i]:
                    case Mode.zero:
                        self.memory[key] = self.get_from_opcode(self.opcode[mem_index])
                    case Mode.one:
                        self.memory[key] = self.get_from_opcode(mem_index)
                    case Mode.two:
                        self.memory[key] = self.get_from_opcode(self.opcode[mem_index] + self.rel_base_off)
                    case _:
                        raise ValueError(f"Mode '{self.modes[i]}' not supported")
      
            # Determining the output address
            mem = chr(65 + self.n_arguments[curr_inst] - 1)
            output_addr = self.memory[mem]

            # Operations
            cont = self.handle_operation(curr_inst, output_addr)
            if cont: continue

            # Jumping. P.S.: self.jump is updated every instruction by self.get_opcode_and_modes()
            self.inst_pointer += self.jump

    def handle_operation(self, curr_inst: int, output_addr: int) -> bool:        
        match curr_inst:
            case 1:     # Addition
                self.put_to_opcode(self.memory["A"] + self.memory["B"], output_addr)

            case 2:     # Product
                self.put_to_opcode(self.memory["A"] * self.memory["B"], output_addr)

            case 3:     # Stores input
                if self.prompt_inputs: inp = int(input())
                else:                  inp = self.input  # Uses what is in self.input

                self.put_to_opcode(inp, output_addr)

            case 4:     # Outputs
                self.output = self.search_memory_on_modes(output_addr, self.modes[0])

                # Finished a test
                if self.show_outputs: print(self.output)

            case 5:     # Jump-if-true
                if self.memory["A"] != 0:
                    self.inst_pointer = self.search_memory_on_modes(self.memory["B"], self.modes[1])
                    return 1

            case 6:     # Jump-if-false
                if self.memory["A"] == 0:
                    self.inst_pointer = self.search_memory_on_modes(self.memory["B"], self.modes[1])
                    return 1

            case 7:     # Less than
                if self.memory["A"] < self.memory["B"]:
                    self.put_to_opcode(1, output_addr)
                else:
                    self.put_to_opcode(0, output_addr)

            case 8:     # Equals
                if self.memory["A"] == self.memory["B"]:
                    self.put_to_opcode(1, output_addr)
                else:
                    self.put_to_opcode(0, output_addr)

            case 9:     # Modifies relative base offset
                self.rel_base_off += self.search_memory_on_modes(self.memory["A"], self.modes[0])

        return 0

    def search_memory_on_modes(self, mem: int, mode: Mode) -> int:
        """
        Returns a value from memory base a mode and how many dereferences it needs.
        Number of dereferences in the form of a list of sets (self.n_dereferences) i.e., [{a}, {b, c}]
        Position 0 (mode a) will be dereferenced 0 times
        Position 1 (modes b and c) will be dereferenced once
        """
        
        out = mem
        n_deref = 0
        for i, se in enumerate(self.n_dereferences):
            if mode in se: n_deref = i
        
        for i in range(0, n_deref):
            out = self.get_from_opcode(out)

        return out

    def get_from_opcode(self, index: int) -> int:
        """
        Returns value at index index in opcode (if existent) else
        in self.extra_mem
        """

        if index < len(self.opcode):
            return self.opcode[index]
        
        if index not in self.extra_mem.keys():
            self.extra_mem[index] = 0

        return self.extra_mem[index]

    def put_to_opcode(self, value: int, index: int) -> None:
        """
        Puts a value into index in self.opcode
        """

        if index < len(self.opcode):
            self.opcode[index] = value
            return
        
        self.extra_mem[index] = value

    def read_input_file(self):
        with open(self.path_input) as data:
            self.base_opcode = data.read().split(",")
            self.base_opcode = [int(code) for code in self.base_opcode]
            self.opcode = self.base_opcode.copy()

    def reset_memory(self) -> None:
        self.opcode       = self.base_opcode.copy()     
        self.inst_pointer = self.init_inst_pointer 
        self.rel_base_off = 0

    def get_output(self) -> int:
        return self.output

    def search_for_output(self, desired_out: int, max_noun: int, max_verb: int) -> (int, int):
        """
        Loops through values of addresses 1 and 2 to find the pair
        that yields the desired output at address 0
        """
        for noun in range(max_noun + 1):
            for verb in range(max_verb + 1):
                self.reset_memory()
                self.opcode[1] = noun
                self.opcode[2] = verb

                self.run()

                if self.opcode[0] == desired_out:
                    return (noun, verb)

        error_msg = f"""
        No pair of (noun, verb) such that noun in [0, {max_noun}] and
        verb in [0, {max_verb}] yield the desired output
        """
        raise ValueError(error_msg)

    def get_opcode_and_modes(self, code: int) -> (list[Mode], int):
        """
        Returns parsed information regarding modes and instruction.
        Also takes care of how much to increase the pointer after
        current instruction is done.
        Instruction: CBAZZ with C, B and A being memory addresses and ZZ an instruction
        """    

        if code in self.halt_inst: return None, code

        str_code = str(code)

        str_code = "0" * (self.inst_max_len - len(str_code)) + str_code
        instruction = int(str_code[-2:])
        self.jump = self.n_arguments[instruction] + 1
        
        modes = []

        for i in range(self.modes_len-1, -1, -1):
            try:
                match str_code[i]:
                    case "0":   modes.append(Mode.zero)
                    case "1":   modes.append(Mode.one)
                    case "2":   modes.append(Mode.two)
            except IndexError as e:     # Trying to access 3 addresses when only 1 or 2 are present
                modes.append(None)

        return modes, instruction