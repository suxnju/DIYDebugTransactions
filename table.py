def STOP(self):
    '''
        00 \\
        STOP() \\
        halts execution of the contract
    '''
    raise ValueError('Not implement STOP error!')

def ADD(self):
    '''
        01 \\
        a+b \\
        (u)int256 addition modulo 2**256
    '''
    raise ValueError('Not implement ADD error!')

def MUL(self):
    '''
        02 \\
        a*b \\
        (u)int256 multiplication modulo 2**256
    '''
    raise ValueError('Not implement MUL error!')

def SUB(self):
    '''
        03 \\
        a-b \\
        (u)int256 subtraction modulo 2**256
    '''
    raise ValueError('Not implement SUB error!')

def DIV(self):
    '''
        04 \\
        a//b \\
        uint256 division
    '''
    raise ValueError('Not implement DIV error!')

def SDIV(self):
    '''
        05 \\
        a//b \\
        int256 division
    '''
    raise ValueError('Not implement SDIV error!')

def MOD(self):
    '''
        06 \\
        a%b \\
        uint256 modulus
    '''
    raise ValueError('Not implement MOD error!')

def SMOD(self):
    '''
        07 \\
        a%b \\
        int256 modulus
    '''
    raise ValueError('Not implement SMOD error!')

def ADDMOD(self):
    '''
        08 \\
        (a+b)%N \\
        (u)int256 addition modulo N
    '''
    raise ValueError('Not implement ADDMOD error!')

def MULMOD(self):
    '''
        09 \\
        (a*b)%N \\
        (u)int256 multiplication modulo N
    '''
    raise ValueError('Not implement MULMOD error!')

def EXP(self):
    '''
        0A \\
        a**b \\
        uint256 exponentiation modulo 2**256
    '''
    raise ValueError('Not implement EXP error!')

def SIGNEXTEND(self):
    '''
        0B \\
        y=SIGNEXTEND(x,b) \\
        sign extends x from (b + 1) * 8 bits to 256 bits.
    '''
    raise ValueError('Not implement SIGNEXTEND error!')

def LT(self):
    '''
        10 \\
        a<b \\
        uint256 comparison
    '''
    raise ValueError('Not implement LT error!')

def GT(self):
    '''
        11 \\
        a>b \\
        uint256 comparison
    '''
    raise ValueError('Not implement GT error!')

def SLT(self):
    '''
        12 \\
        a<b \\
        int256 comparison
    '''
    raise ValueError('Not implement SLT error!')

def SGT(self):
    '''
        13 \\
        a>b \\
        int256 comparison
    '''
    raise ValueError('Not implement SGT error!')

def EQ(self):
    '''
        14 \\
        a==b \\
        (u)int256 equality
    '''
    raise ValueError('Not implement EQ error!')

def ISZERO(self):
    '''
        15 \\
        a==0 \\
        (u)int256 is zero
    '''
    raise ValueError('Not implement ISZERO error!')

def AND(self):
    '''
        16 \\
        a&b \\
        256-bit bitwise and
    '''
    raise ValueError('Not implement AND error!')

def OR(self):
    '''
        17 \\
        a|b \\
        256-bit bitwise or
    '''
    raise ValueError('Not implement OR error!')

def XOR(self):
    '''
        18 \\
        a^b \\
        256-bit bitwise xor
    '''
    raise ValueError('Not implement XOR error!')

def NOT(self):
    '''
        19 \\
        ~a \\
        256-bit bitwise not
    '''
    raise ValueError('Not implement NOT error!')

def BYTE(self):
    '''
        1A \\
        y=(x>>(248-i*8))&0xFF \\
        ith byte of (u)int256 x, counting from most significant byte
    '''
    raise ValueError('Not implement BYTE error!')

def SHL(self):
    '''
        1B \\
        value<<shift \\
        256-bit shift left
    '''
    raise ValueError('Not implement SHL error!')

def SHR(self):
    '''
        1C \\
        value>>shift \\
        256-bit shift right
    '''
    raise ValueError('Not implement SHR error!')

def SAR(self):
    '''
        1D \\
        value>>shift \\
        int256 shift right
    '''
    raise ValueError('Not implement SAR error!')

def SHA3(self):
    '''
        20 \\
        hash=keccak256(memory[offset:offset+length]) \\
        keccak256
    '''
    raise ValueError('Not implement SHA3 error!')

def ADDRESS(self):
    '''
        30 \\
        address(this) \\
        address of the executing contract
    '''
    raise ValueError('Not implement ADDRESS error!')

def BALANCE(self):
    '''
        31 \\
        address(addr).balance \\
        address balance in wei
    '''
    raise ValueError('Not implement BALANCE error!')

def ORIGIN(self):
    '''
        32 \\
        tx.origin \\
        transaction origin address
    '''
    raise ValueError('Not implement ORIGIN error!')

def CALLER(self):
    '''
        33 \\
        msg.caller \\
        message caller address
    '''
    raise ValueError('Not implement CALLER error!')

def CALLVALUE(self):
    '''
        34 \\
        msg.value \\
        message funds in wei
    '''
    raise ValueError('Not implement CALLVALUE error!')

def CALLDATALOAD(self):
    '''
        35 \\
        msg.data[i:i+32] \\
        reads a (u)int256 from message data
    '''
    raise ValueError('Not implement CALLDATALOAD error!')

def CALLDATASIZE(self):
    '''
        36 \\
        msg.data.size \\
        message data length in bytes
    '''
    raise ValueError('Not implement CALLDATASIZE error!')

def CALLDATACOPY(self):
    '''
        37 \\
        memory[destOffset:destOffset+length]=msg.data[offset:offset+length] \\
        copy message data
    '''
    raise ValueError('Not implement CALLDATACOPY error!')

def CODESIZE(self):
    '''
        38 \\
        address(this).code.size \\
        length of the executing contract's code in bytes
    '''
    raise ValueError('Not implement CODESIZE error!')

def CODECOPY(self):
    '''
        39 \\
        memory[destOffset:destOffset+length]=address(this).code[offset:offset+length] \\
        copy executing contract's bytecode
    '''
    raise ValueError('Not implement CODECOPY error!')

def GASPRICE(self):
    '''
        3A \\
        tx.gasprice \\
        gas price of the executing transaction, in wei per unit of gas
    '''
    raise ValueError('Not implement GASPRICE error!')

def EXTCODESIZE(self):
    '''
        3B \\
        address(addr).code.size \\
        length of the contract bytecode at addr, in bytes
    '''
    raise ValueError('Not implement EXTCODESIZE error!')

def EXTCODECOPY(self):
    '''
        3C \\
        memory[destOffset:destOffset+length]=address(addr).code[offset:offset+length] \\
        copy contract's bytecode
    '''
    raise ValueError('Not implement EXTCODECOPY error!')

def RETURNDATASIZE(self):
    '''
        3D \\
        size=RETURNDATASIZE() \\
        the size of the returned data from the last external call, in bytes
    '''
    raise ValueError('Not implement RETURNDATASIZE error!')

def RETURNDATACOPY(self):
    '''
        3E \\
        memory[destOffset:destOffset+length]=RETURNDATA[offset:offset+length] \\
        copy returned data
    '''
    raise ValueError('Not implement RETURNDATACOPY error!')

def EXTCODEHASH(self):
    '''
        3F \\
        hash=address(addr).exists?keccak256(address(addr).code):0 \\
        hash of the contract bytecode at addr, see EIP-1052
    '''
    raise ValueError('Not implement EXTCODEHASH error!')

def BLOCKHASH(self):
    '''
        40 \\
        hash=block.blockHash(blockNumber) \\
        hash of the specific block, only valid for the 256 most recent blocks, excluding the current one
    '''
    raise ValueError('Not implement BLOCKHASH error!')

def COINBASE(self):
    '''
        41 \\
        block.coinbase \\
        address of the current block's miner
    '''
    raise ValueError('Not implement COINBASE error!')

def TIMESTAMP(self):
    '''
        42 \\
        block.timestamp \\
        current block's Unix timestamp in seconds
    '''
    raise ValueError('Not implement TIMESTAMP error!')

def NUMBER(self):
    '''
        43 \\
        block.number \\
        current block's number
    '''
    raise ValueError('Not implement NUMBER error!')

def DIFFICULTY(self):
    '''
        44 \\
        block.difficulty \\
        current block's difficulty
    '''
    raise ValueError('Not implement DIFFICULTY error!')

def GASLIMIT(self):
    '''
        45 \\
        block.gaslimit \\
        current block's gas limit
    '''
    raise ValueError('Not implement GASLIMIT error!')

def POP(self):
    '''
        50 \\
        POP() \\
        pops a (u)int256 off the stack and discards it
    '''
    raise ValueError('Not implement POP error!')

def MLOAD(self):
    '''
        51 \\
        value=memory[offset:offset+32] \\
        reads a (u)int256 from memory
    '''
    raise ValueError('Not implement MLOAD error!')

def MSTORE(self):
    '''
        52 \\
        memory[offset:offset+32]=value \\
        writes a (u)int256 to memory
    '''
    raise ValueError('Not implement MSTORE error!')

def MSTORE8(self):
    '''
        53 \\
        memory[offset]=value&0xFF \\
        writes a uint8 to memory
    '''
    raise ValueError('Not implement MSTORE8 error!')

def SLOAD(self):
    '''
        54 \\
        value=storage[key] \\
        reads a (u)int256 from storage
    '''
    raise ValueError('Not implement SLOAD error!')

def SSTORE(self):
    '''
        55 \\
        storage[key]=value \\
        writes a (u)int256 to storage
    '''
    raise ValueError('Not implement SSTORE error!')

def JUMP(self):
    '''
        56 \\
        $pc=destination \\
        unconditional jump
    '''
    raise ValueError('Not implement JUMP error!')

def JUMPI(self):
    '''
        57 \\
        $pc=cond?destination:$pc+1 \\
        conditional jump if condition is truthy
    '''
    raise ValueError('Not implement JUMPI error!')

def PC(self):
    '''
        58 \\
        $pc \\
        program counter
    '''
    raise ValueError('Not implement PC error!')

def MSIZE(self):
    '''
        59 \\
        size=MSIZE() \\
        size of memory for this contract execution, in bytes
    '''
    raise ValueError('Not implement MSIZE error!')

def GAS(self):
    '''
        5A \\
        gasRemaining=GAS() \\
        remaining gas
    '''
    raise ValueError('Not implement GAS error!')

def JUMPDEST(self):
    '''
        5B \\
         \\
        metadata to annotate possible jump destinations
    '''
    raise ValueError('Not implement JUMPDEST error!')

def PUSH1(self):
    '''
        60 \\
        PUSH(uint8) \\
        pushes a 1-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH1 error!')

def PUSH2(self):
    '''
        61 \\
        PUSH(uint16) \\
        pushes a 2-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH2 error!')

def PUSH3(self):
    '''
        62 \\
        PUSH(uint24) \\
        pushes a 3-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH3 error!')

def PUSH4(self):
    '''
        63 \\
        PUSH(uint32) \\
        pushes a 4-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH4 error!')

def PUSH5(self):
    '''
        64 \\
        PUSH(uint40) \\
        pushes a 5-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH5 error!')

def PUSH6(self):
    '''
        65 \\
        PUSH(uint48) \\
        pushes a 6-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH6 error!')

def PUSH7(self):
    '''
        66 \\
        PUSH(uint56) \\
        pushes a 7-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH7 error!')

def PUSH8(self):
    '''
        67 \\
        PUSH(uint64) \\
        pushes a 8-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH8 error!')

def PUSH9(self):
    '''
        68 \\
        PUSH(uint72) \\
        pushes a 9-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH9 error!')

def PUSH10(self):
    '''
        69 \\
        PUSH(uint80) \\
        pushes a 10-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH10 error!')

def PUSH11(self):
    '''
        6A \\
        PUSH(uint88) \\
        pushes a 11-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH11 error!')

def PUSH12(self):
    '''
        6B \\
        PUSH(uint96) \\
        pushes a 12-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH12 error!')

def PUSH13(self):
    '''
        6C \\
        PUSH(uint104) \\
        pushes a 13-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH13 error!')

def PUSH14(self):
    '''
        6D \\
        PUSH(uint112) \\
        pushes a 14-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH14 error!')

def PUSH15(self):
    '''
        6E \\
        PUSH(uint120) \\
        pushes a 15-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH15 error!')

def PUSH16(self):
    '''
        6F \\
        PUSH(uint128) \\
        pushes a 16-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH16 error!')

def PUSH17(self):
    '''
        70 \\
        PUSH(uint136) \\
        pushes a 17-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH17 error!')

def PUSH18(self):
    '''
        71 \\
        PUSH(uint144) \\
        pushes a 18-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH18 error!')

def PUSH19(self):
    '''
        72 \\
        PUSH(uint152) \\
        pushes a 19-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH19 error!')

def PUSH20(self):
    '''
        73 \\
        PUSH(uint160) \\
        pushes a 20-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH20 error!')

def PUSH21(self):
    '''
        74 \\
        PUSH(uint168) \\
        pushes a 21-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH21 error!')

def PUSH22(self):
    '''
        75 \\
        PUSH(uint176) \\
        pushes a 22-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH22 error!')

def PUSH23(self):
    '''
        76 \\
        PUSH(uint184) \\
        pushes a 23-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH23 error!')

def PUSH24(self):
    '''
        77 \\
        PUSH(uint192) \\
        pushes a 24-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH24 error!')

def PUSH25(self):
    '''
        78 \\
        PUSH(uint200) \\
        pushes a 25-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH25 error!')

def PUSH26(self):
    '''
        79 \\
        PUSH(uint208) \\
        pushes a 26-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH26 error!')

def PUSH27(self):
    '''
        7A \\
        PUSH(uint216) \\
        pushes a 27-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH27 error!')

def PUSH28(self):
    '''
        7B \\
        PUSH(uint224) \\
        pushes a 28-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH28 error!')

def PUSH29(self):
    '''
        7C \\
        PUSH(uint232) \\
        pushes a 29-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH29 error!')

def PUSH30(self):
    '''
        7D \\
        PUSH(uint240) \\
        pushes a 30-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH30 error!')

def PUSH31(self):
    '''
        7E \\
        PUSH(uint248) \\
        pushes a 31-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH31 error!')

def PUSH32(self):
    '''
        7F \\
        PUSH(uint256) \\
        pushes a 32-byte value onto the stack
    '''
    raise ValueError('Not implement PUSH32 error!')

def DUP1(self):
    '''
        80 \\
        PUSH(value) \\
        clones the last value on the stack
    '''
    raise ValueError('Not implement DUP1 error!')

def DUP2(self):
    '''
        81 \\
        PUSH(value) \\
        clones the 2nd last value on the stack
    '''
    raise ValueError('Not implement DUP2 error!')

def DUP3(self):
    '''
        82 \\
        PUSH(value) \\
        clones the 3rd last value on the stack
    '''
    raise ValueError('Not implement DUP3 error!')

def DUP4(self):
    '''
        83 \\
        PUSH(value) \\
        clones the 4th last value on the stack
    '''
    raise ValueError('Not implement DUP4 error!')

def DUP5(self):
    '''
        84 \\
        PUSH(value) \\
        clones the 5th last value on the stack
    '''
    raise ValueError('Not implement DUP5 error!')

def DUP6(self):
    '''
        85 \\
        PUSH(value) \\
        clones the 6th last value on the stack
    '''
    raise ValueError('Not implement DUP6 error!')

def DUP7(self):
    '''
        86 \\
        PUSH(value) \\
        clones the 7th last value on the stack
    '''
    raise ValueError('Not implement DUP7 error!')

def DUP8(self):
    '''
        87 \\
        PUSH(value) \\
        clones the 8th last value on the stack
    '''
    raise ValueError('Not implement DUP8 error!')

def DUP9(self):
    '''
        88 \\
        PUSH(value) \\
        clones the 9th last value on the stack
    '''
    raise ValueError('Not implement DUP9 error!')

def DUP10(self):
    '''
        89 \\
        PUSH(value) \\
        clones the 10th last value on the stack
    '''
    raise ValueError('Not implement DUP10 error!')

def DUP11(self):
    '''
        8A \\
        PUSH(value) \\
        clones the 11th last value on the stack
    '''
    raise ValueError('Not implement DUP11 error!')

def DUP12(self):
    '''
        8B \\
        PUSH(value) \\
        clones the 12th last value on the stack
    '''
    raise ValueError('Not implement DUP12 error!')

def DUP13(self):
    '''
        8C \\
        PUSH(value) \\
        clones the 13th last value on the stack
    '''
    raise ValueError('Not implement DUP13 error!')

def DUP14(self):
    '''
        8D \\
        PUSH(value) \\
        clones the 14th last value on the stack
    '''
    raise ValueError('Not implement DUP14 error!')

def DUP15(self):
    '''
        8E \\
        PUSH(value) \\
        clones the 15th last value on the stack
    '''
    raise ValueError('Not implement DUP15 error!')

def DUP16(self):
    '''
        8F \\
        PUSH(value) \\
        clones the 16th last value on the stack
    '''
    raise ValueError('Not implement DUP16 error!')

def SWAP1(self):
    '''
        90 \\
        a,b=b,a \\
        swaps the last two values on the stack
    '''
    raise ValueError('Not implement SWAP1 error!')

def SWAP2(self):
    '''
        91 \\
        a,b=b,a \\
        swaps the top of the stack with the 3rd last element
    '''
    raise ValueError('Not implement SWAP2 error!')

def SWAP3(self):
    '''
        92 \\
        a,b=b,a \\
        swaps the top of the stack with the 4th last element
    '''
    raise ValueError('Not implement SWAP3 error!')

def SWAP4(self):
    '''
        93 \\
        a,b=b,a \\
        swaps the top of the stack with the 5th last element
    '''
    raise ValueError('Not implement SWAP4 error!')

def SWAP5(self):
    '''
        94 \\
        a,b=b,a \\
        swaps the top of the stack with the 6th last element
    '''
    raise ValueError('Not implement SWAP5 error!')

def SWAP6(self):
    '''
        95 \\
        a,b=b,a \\
        swaps the top of the stack with the 7th last element
    '''
    raise ValueError('Not implement SWAP6 error!')

def SWAP7(self):
    '''
        96 \\
        a,b=b,a \\
        swaps the top of the stack with the 8th last element
    '''
    raise ValueError('Not implement SWAP7 error!')

def SWAP8(self):
    '''
        97 \\
        a,b=b,a \\
        swaps the top of the stack with the 9th last element
    '''
    raise ValueError('Not implement SWAP8 error!')

def SWAP9(self):
    '''
        98 \\
        a,b=b,a \\
        swaps the top of the stack with the 10th last element
    '''
    raise ValueError('Not implement SWAP9 error!')

def SWAP10(self):
    '''
        99 \\
        a,b=b,a \\
        swaps the top of the stack with the 11th last element
    '''
    raise ValueError('Not implement SWAP10 error!')

def SWAP11(self):
    '''
        9A \\
        a,b=b,a \\
        swaps the top of the stack with the 12th last element
    '''
    raise ValueError('Not implement SWAP11 error!')

def SWAP12(self):
    '''
        9B \\
        a,b=b,a \\
        swaps the top of the stack with the 13th last element
    '''
    raise ValueError('Not implement SWAP12 error!')

def SWAP13(self):
    '''
        9C \\
        a,b=b,a \\
        swaps the top of the stack with the 14th last element
    '''
    raise ValueError('Not implement SWAP13 error!')

def SWAP14(self):
    '''
        9D \\
        a,b=b,a \\
        swaps the top of the stack with the 15th last element
    '''
    raise ValueError('Not implement SWAP14 error!')

def SWAP15(self):
    '''
        9E \\
        a,b=b,a \\
        swaps the top of the stack with the 16th last element
    '''
    raise ValueError('Not implement SWAP15 error!')

def SWAP16(self):
    '''
        9F \\
        a,b=b,a \\
        swaps the top of the stack with the 17th last element
    '''
    raise ValueError('Not implement SWAP16 error!')

def LOG0(self):
    '''
        A0 \\
        LOG0(memory[offset:offset+length]) \\
        fires an event
    '''
    raise ValueError('Not implement LOG0 error!')

def LOG1(self):
    '''
        A1 \\
        LOG1(memory[offset:offset+length],topic0) \\
        fires an event
    '''
    raise ValueError('Not implement LOG1 error!')

def LOG2(self):
    '''
        A2 \\
        LOG2(memory[offset:offset+length],topic0,topic1) \\
        fires an event
    '''
    raise ValueError('Not implement LOG2 error!')

def LOG3(self):
    '''
        A3 \\
        LOG3(memory[offset:offset+length],topic0,topic1,topic2) \\
        fires an event
    '''
    raise ValueError('Not implement LOG3 error!')

def LOG4(self):
    '''
        A4 \\
        LOG4(memory[offset:offset+length],topic0,topic1,topic2,topic3) \\
        fires an event
    '''
    raise ValueError('Not implement LOG4 error!')

def PUSH(self):
    '''
        B0 \\
        ??? \\
        ???
    '''
    raise ValueError('Not implement PUSH error!')

def DUP(self):
    '''
        B1 \\
        ??? \\
        ???
    '''
    raise ValueError('Not implement DUP error!')

def SWAP(self):
    '''
        B2 \\
        ??? \\
        ???
    '''
    raise ValueError('Not implement SWAP error!')

def CREATE(self):
    '''
        F0 \\
        addr=newmemory[offset:offset+length].value(value) \\
        creates a child contract
    '''
    raise ValueError('Not implement CREATE error!')

def CALL(self):
    '''
        F1 \\
        success,memory[retOffset:retOffset+retLength]=address(addr).call.gas(gas).value(value)(memory[argsOffset:argsOffset+argsLength]) \\
        calls a method in another contract
    '''
    raise ValueError('Not implement CALL error!')

def CALLCODE(self):
    '''
        F2 \\
        success,memory[retOffset:retOffset+retLength]=address(addr).callcode.gas(gas).value(value)(memory[argsOffset:argsOffset+argsLength]) \\
        ???
    '''
    raise ValueError('Not implement CALLCODE error!')

def RETURN(self):
    '''
        F3 \\
        returnmemory[offset:offset+length] \\
        returns from this contract call
    '''
    raise ValueError('Not implement RETURN error!')

def DELEGATECALL(self):
    '''
        F4 \\
        success,memory[retOffset:retOffset+retLength]=address(addr).delegatecall.gas(gas)(memory[argsOffset:argsOffset+argsLength]) \\
        calls a method in another contract, using the storage of the current contract
    '''
    raise ValueError('Not implement DELEGATECALL error!')

def CREATE2(self):
    '''
        F5 \\
        addr=newmemory[offset:offset+length].value(value) \\
        creates a child contract with a deterministic address, see EIP-1014
    '''
    raise ValueError('Not implement CREATE2 error!')

def STATICCALL(self):
    '''
        FA \\
        success,memory[retOffset:retOffset+retLength]=address(addr).staticcall.gas(gas)(memory[argsOffset:argsOffset+argsLength]) \\
        calls a method in another contract with state changes such as contract creation, event emission, storage modification and contract destruction disallowed, see EIP-214
    '''
    raise ValueError('Not implement STATICCALL error!')

def REVERT(self):
    '''
        FD \\
        revert(memory[offset:offset+length]) \\
        reverts with return data
    '''
    raise ValueError('Not implement REVERT error!')

def SELFDESTRUCT(self):
    '''
        FF \\
        selfdestruct(address(addr)) \\
        destroys the contract and sends all funds to addr.
    '''
    raise ValueError('Not implement SELFDESTRUCT error!')

