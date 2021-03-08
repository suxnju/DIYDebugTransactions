### References:
### https://ethervm.io/
### https://github.com/usyd-blockchain/vandal/blob/d2b004326fee33920c313e64d0970410b1933990/src/memtypes.py

# default 32 bytes per block
# 高位其实补的是0，SIGNEXTEND使得高位补符号位
from typing import List
import logging
SIZE = 32
UPPER = int('f'*32,16)

class STOP:
    def __init__(self):
        self.opcode = 0x0
        self.expression = "STOP()"
        self.notes = "halts execution of the contract"

class ADD:
    def __init__(self):
        self.opcode = 0x1
        self.expression = "a+b"
        self.notes = "(u)int256 addition modulo 2**256"

    def __call__(self,stack_input:List[int]) -> List[int]:
        assert len(stack_input) >= 2

        c = stack_input[0]+stack_input[1]
        if c>UPPER:
            logging.warning("Integer overflow")
        c = c%UPPER
        stack_output = [c] + stack_input[2:]
        return stack_output

class MUL:
    def __init__(self):
        self.opcode = 0x2
        self.expression = "a*b"
        self.notes = "(u)int256 multiplication modulo 2**256"

    def __call__(self,stack_input):
        assert len(stack_input) >= 2
        
        c = stack_input[0]*stack_input[1]
        if c>UPPER:
            logging.warning("Integer overflow")
        c = c%UPPER
        stack_output = [c] + stack_input[2:]
        return stack_output
    
class SUB:
    def __init__(self):
        self.opcode = 0x3
        self.expression = "a-b"
        self.notes = "(u)int256 subtraction modulo 2**256"

    def __call__(self,stack_input):
        assert len(stack_input) >= 2
        c = stack_input[0]-stack_input[1]
        c = c%UPPER

        stack_output = [c] + stack_input[2:]

        return stack_output

class DIV:
    def __init__(self):
        self.opcode = 0x4
        self.expression = "a//b"
        self.notes = "uint256 division"

    def __call__(self,stack_input):
        assert len(stack_input) >= 2

        # // division
        stack_output = [stack_input[0]//stack_input[1]] + stack_input[2:]
        return stack_output

class SDIV:
    def __init__(self):
        self.opcode = 0x5
        self.expression = "a//b"
        self.notes = "int256 division"

    def __call__(self,stack_input):
        assert len(stack_input) >= 2

        # // division
        stack_output = [stack_input[0]//stack_input[1]] + stack_input[2:]
        return stack_output

class MOD:
    def __init__(self):
        self.opcode = 0x6
        self.expression = "a\%b"
        self.notes = "uint256 modulus"

    def __call__(self,stack_input):
        assert len(stack_input) >= 2

        stack_output = [stack_input[0]%stack_input[1]] + stack_input[2:]
        return stack_output

class SMOD:
    def __init__(self):
        self.opcode = 0x7
        self.expression = "a\%b"
        self.notes = "int256 modulus"

    def __call__(self,stack_input):
        assert len(stack_input) >= 2

        stack_output = [stack_input[0]%stack_input[1]] + stack_input[2:]
        return stack_output

class ADDMOD:
    def __init__(self):
        self.opcode = 0x8
        self.expression = "(a+b)%N"
        self.notes = "(u)int256 addition modulo N"

    def __call__(self,stack_input):
        assert len(stack_input) >= 3

        stack_output = [(stack_input[0]+stack_input[1])%stack_input[2]] + stack_input[3:]
        return stack_output

class MULMOD:
    def __init__(self):
        self.opcode = 0x9
        self.expression = "(a*b)%N"
        self.notes = "(u)int256 multiplication modulo N"

    def __call__(self,stack_input):
        assert len(stack_input) >= 3

        stack_output = [(stack_input[0]*stack_input[1])%stack_input[2]] + stack_input[3:]
        return stack_output

class EXP:
    def __init__(self):
        self.opcode = 0xA
        self.expression = "a**b"
        self.notes = "uint256 exponentiation modulo 2**256"

    def __call__(self,stack_input):
        assert len(stack_input) >= 2

        stack_output = [stack_input[0]**stack_input[1]] + stack_input[2:]
        return stack_output

class SIGNEXTEND:
    def __init__(self):
        self.opcode = 0xB
        self.expression = "y=SIGNEXTEND(x, b)"
        self.notes = "sign extends x from (b + 1) * 8 bits to 256 bits."

    def signextend(self,b,v):
        """
        Return v, but with the high bit of its b'th byte extended all the way
        to the most significant bit of the output.
        """
        pos = 8 * (b + 1)
        mask = int("1" * (256 - pos) + "0" * pos, 2)
        val = 1 if (v & (1 << (pos - 1))) > 0 else 0

        return (v & mask) if (val == 0) else (v | ~mask)

    def __call__(self,stack_input):
        assert len(stack_input) >= 2

        stack_output = [self.signextend(stack_input[0],stack_input[1])] + stack_input[2:]
        return stack_output

class LT:
    def __init__(self):
        self.opcode = 0x10
        self.expression = "a < b"
        self.notes = "uint256 comparison"

    def __call__(self,stack_input):
        assert len(stack_input) >= 2

        stack_output = [int(stack_input[0]<stack_input[1])] + stack_input[2:]
        return stack_output

class GT:
    def __init__(self):
        self.opcode = 0x11
        self.expression = "a > b"
        self.notes = "uint256 comparison"

    def __call__(self,stack_input):
        assert len(stack_input) >= 2

        stack_output = [int(stack_input[0]>stack_input[1])] + stack_input[2:]
        return stack_output

class SLT:
    def __init__(self):
        self.opcode = 0x12
        self.expression = "a < b"
        self.notes = "int256 comparison"

    def __call__(self,stack_input):
        assert len(stack_input) >= 2

        stack_output = [int(stack_input[0]<stack_input[1])] + stack_input[2:]
        return stack_output

class SGT:
    def __init__(self):
        self.opcode = 0x13
        self.expression = "a > b"
        self.notes = "int256 comparison"

    def __call__(self,stack_input):
        assert len(stack_input) >= 2

        stack_output = [int(stack_input[0]>stack_input[1])] + stack_input[2:]
        return stack_output

class EQ:
    def __init__(self):
        self.opcode = 0x14
        self.expression = "a == b"
        self.notes = "(u)int256 equality"

    def __call__(self,stack_input):
        assert len(stack_input) >= 2

        stack_output = [int(stack_input[0]==stack_input[1])] + stack_input[2:]
        return stack_output

class ISZERO:
    def __init__(self):
        self.opcode = 0x15
        self.expression = "a == 0"
        self.notes = "(u)int256 is zero"

    def __call__(self,stack_input):

        stack_output = [int(stack_input[0]==0)] + stack_input[2:]
        return stack_output

class AND:
    def __init__(self):
        self.opcode = 0x16
        self.expression = "a & b"
        self.notes = "256-bit bitwise and"

    def __call__(self,stack_input):
        assert len(stack_input) >= 2

        stack_output = [stack_input[0] & stack_input[1]] + stack_input[2:]
        return stack_output

class OR:
    def __init__(self):
        self.opcode = 0x17
        self.expression = "a | b"
        self.notes = "256-bit bitwise or"

    def __call__(self,stack_input):
        assert len(stack_input) >= 2

        stack_output = [stack_input[0] | stack_input[1]] + stack_input[2:]
        return stack_output

class XOR:
    def __init__(self):
        self.opcode = 0x18
        self.expression = "a ^ b"
        self.notes = "256-bit bitwise xor"

    def __call__(self,stack_input):
        assert len(stack_input) >= 2

        stack_output = [stack_input[0] ^ stack_input[1]] + stack_input[2:]
        return stack_output

class NOT:
    pass

if __name__ == "__main__":
    # output_stack = ADD()([1,2])
    output_stack = eval('ADD')()([1,2])

    print(output_stack)