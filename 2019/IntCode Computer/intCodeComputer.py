class IntCodeComputer():
    def __init__(self, path: str):
        self.base_opcode       = ...
        self.base_jump         = 4
        self.init_inst_pointer = 0
        
        self.path_input  = path
        self.opcode      = ...
        self.read_input_file()        

        self.valid_inst   = {1, 2}
        self.halt_inst    = {99}

        self.jump         = self.base_jump
        self.inst_pointer = self.init_inst_pointer

    def run(self) -> None:
        """
        Executes opcode
        """

        curr_inst = self.opcode[0]
        while curr_inst not in self.halt_inst:
            curr_inst = self.opcode[self.inst_pointer]

            if curr_inst in self.halt_inst:
                return
            if curr_inst not in self.valid_inst:
                raise ValueError(f"Instruction '{curr_inst}' not valid")

            # Operations
            memA, memB  = self.opcode[self.opcode[self.inst_pointer+1]], self.opcode[self.opcode[self.inst_pointer+2]]
            output_addr = self.opcode[self.inst_pointer+3]
            match curr_inst:
                case 1:   # Addition
                    self.opcode[output_addr] = memA + memB
                case 2:   # Product
                    self.opcode[output_addr] = memA * memB

            self.inst_pointer += self.jump

    def read_input_file(self):
        with open(self.path_input) as data:
            self.base_opcode = data.read().split(",")
            self.base_opcode = [int(code) for code in self.base_opcode]
            self.opcode = self.base_opcode.copy()

    def reset_memory(self) -> None:
        self.opcode       = self.base_opcode.copy()
        self.jump         = self.base_jump         
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
