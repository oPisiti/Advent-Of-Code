from enum import Enum
class Mode(Enum):
    zero = "Position Mode"     
    one  = "Immediate Mode"     

class IntCodeComputer():
    def __init__(self, path: str, input_ = 1):
        self.base_opcode       = ...
        self.init_inst_pointer = 0
        
        # Code
        self.path_input  = path
        self.opcode      = ...
        self.read_input_file()        
        
        # Possible instructions
        self.opcode_len = 2         # How many digits for an opcode, i.e. 02, 01, 99
        self.valid_inst = {1, 2, 3, 4}
        self.halt_inst  = {99}
        
        self.jump_after_inst = {    # How many addresses to jump given each instruction
            1: 4,
            2: 4,
            3: 2,
            4: 2
        }
        self.jump            = None
        self.inst_pointer    = self.init_inst_pointer

        # Modes
        self.inst_max_len = 5   # How many digits in instruction (including param modes)
        self.modes_len    = self.inst_max_len - self.opcode_len
        self.modes        = [Mode.zero for _ in range(self.modes_len)]

        # Memory
        # Given opcode CBAZZ, ABC are memory and ZZ is the instruction
        self.memory = {
            "A": None,
            "B": None,
            "C": None
        }

        # IO
        self.input  = input_
        self.output = None


    def run(self) -> None:
        """
        Executes opcode
        """

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
                
                # Simple instructions like 3 and 4 only memory A needs to be updated
                if mem_index >= (self.inst_pointer + self.jump_after_inst[curr_inst]): break

                # Last memory (where to write) should only be dereferenced once at this stage
                # It will be again dereferenced in "operations".
                if i == self.jump_after_inst[curr_inst] - 2:
                    self.memory[key] = self.opcode[mem_index]
                    continue

                # Instructions that need to read more than one memory address
                match self.modes[i]:
                    case Mode.zero:
                        self.memory[key] = self.opcode[self.opcode[mem_index]]
                    case Mode.one:
                        self.memory[key] = self.opcode[mem_index]
                    case _:
                        raise ValueError(f"Mode '{self.modes[i]}' not supported")
      
            # Operations
            output_addr = self.memory["C"] if self.jump_after_inst[curr_inst] == 4 else self.memory["A"]
            match curr_inst:
                case 1:     # Addition                 
                    self.opcode[output_addr] = self.memory["A"] + self.memory["B"]
                case 2:     # Product
                    self.opcode[output_addr] = self.memory["A"] * self.memory["B"]
                case 3:     # Stores input
                    self.opcode[output_addr] = self.input
                case 4:     # Outputs
                    self.output = self.opcode[output_addr]

                    # Finished a test
                    print(f'Output: {self.output}')

            # Jumping. P.S.: self.jump is updated every instruction by self.get_opcode_and_modes()
            self.inst_pointer += self.jump

    def read_input_file(self):
        with open(self.path_input) as data:
            self.base_opcode = data.read().split(",")
            self.base_opcode = [int(code) for code in self.base_opcode]
            self.opcode = self.base_opcode.copy()

    def reset_memory(self) -> None:
        self.opcode       = self.base_opcode.copy()     
        self.inst_pointer = self.init_inst_pointer 

    def get_output(self) -> int:
        return self.opcode[0]

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

                if self.get_output() == desired_out:
                    return (noun, verb)

        error_msg = f"""
        No pair of (noun, verb) such that noun in [0, {max_noun}] and
        verb in [0, {max_verb}] yield the desired output
        """
        raise ValueError(error_msg)

    def get_opcode_and_modes(self, code: int) -> (list[Mode], int):
        """
        Returns parsed information regarding modes and opcode.
        Also takes care of how much to increase the pointer after
        current instruction is done.
        Opcode: CBAZZ with C, B and A being memory addresses and ZZ an instruction
        """    

        if code in self.halt_inst: return None, code

        str_code = str(code)

        str_code = "0" * (self.inst_max_len - len(str_code)) + str_code
        instruction = int(str_code[-2:])
        self.jump = self.jump_after_inst[instruction]
        
        modes = []

        for i in range(self.modes_len-1, -1, -1):
            try:
                modes.append(Mode.zero if str_code[i] == "0" else Mode.one)
            except IndexError as e:     # Trying to access 3 addresses when only 1 is present
                modes.append(None)

        # Mode of memory A is always zero. "Parameters that an instruction writes to will never be in immediate mode."
        # modes[0] = Mode.zero

        return modes, instruction