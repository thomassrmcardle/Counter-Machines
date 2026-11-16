def CounterMachine(Instructions,Registers):
    Index = 1
    CurrentInstr = Instructions[Index-1][1]
    Count = 0
    while CurrentInstr != 'HALT' and Count < 1000:
        if CurrentInstr == 'INC' or CurrentInstr == 'DEC' or CurrentInstr == 'CLR':
            CurrentReg = Instructions[Index-1][2]
            PrintOut = Instructions[Index-1][1:3]
        if CurrentInstr == 'TEST':
            CurrentReg = Instructions[Index-1][2]
            PrintOut = Instructions[Index-1][1:4]
        if CurrentInstr == 'COPY':
            FirstReg = Instructions[Index-1][2]
            SecondReg = Instructions[Index-1][3]
            CurrentReg = max([FirstReg,SecondReg])
            PrintOut = Instructions[Index-1][1:4]
        if CurrentInstr == 'GOTO':
            CurrentReg = 0
            PrintOut = Instructions[Index-1][1:3]
        if CurrentReg > len(Registers):
            NewReg = [0 for i in range(CurrentReg)]
            for i in range(len(Registers)):
                NewReg[i] = Registers[i]
            Registers = NewReg
        if CurrentInstr == 'INC':
            OldValue = Registers[CurrentReg-1]
            Registers[CurrentReg-1] = OldValue + 1
            Index = Index + 1
        if CurrentInstr == 'DEC':
            OldValue = Registers[CurrentReg-1]
            if OldValue > 0:
                Registers[CurrentReg-1] = OldValue - 1
            Index = Index + 1
        if CurrentInstr == 'TEST':
            OldValue = Registers[CurrentReg-1]
            if OldValue == 0:
                Index = Instructions[Index-1][3]
            else:
                Index = Index + 1
        if CurrentInstr == 'COPY':
            FirstValue = Registers[FirstReg-1]
            Registers[SecondReg-1] = FirstValue
            Index = Index + 1
        if CurrentInstr == 'GOTO':
            Index = Instructions[Index-1][2]
        if CurrentInstr == 'CLR':
            Registers[CurrentReg-1] = 0
            Index = Index + 1
        Count = Count + 1
        print (Count, PrintOut, Registers)
        if Count%100000000 == 0:
           print (Count, PrintOut, Registers)
        CurrentInstr = Instructions[Index-1][1]
    Count = Count + 1
    print (Count, ['HALT'], Registers)

# Example values
x = 2
y = 3

# Register mappings
# 1 - x
# 2 - y

# Execution

multiplication = [
    [1, 'TEST', 1, 8], # Quit if one register is empty 
    [2, 'DEC', 1],
    [3, 'COPY', 2, 4],
    [4, 'TEST', 4, 1], # Stop when needed
    [5, 'DEC', 4],
    [6, 'INC', 3], # Use 3 to track the result
    [7, 'GOTO', 4], # While loop
    [8, 'HALT']
]

# 2 to the power of x
# [base, power, accumulator, addition]
powerOfX = [
    [1, 'TEST', 1, 11],
    [2, 'COPY', 1, 3],
    [3, 'TEST', 2, 11],
    [4, 'DEC', 2],
    [5, 'TEST', 2, 11],
    [6, 'COPY', 3, 4],
    [7, 'DEC', 4],
    [8, 'INC', 3],
    [9, 'TEST', 4, 3],
    [10, 'GOTO', 7],
    [11, 'HALT']
]

# x^y
# [x, y, counter, output]
yPowerOfX = [
    [1, 'COPY', 1, 3],
    [2, 'DEC', 3],
    [3, 'INC', 4],
    [5, 'TEST', 3, 2],
    [6, 'GOTO', 10],
    [10, 'HALT']
]

# 6. Remainded of x/y
# 4th register is the remainder.
remainder = [
    [1, 'COPY', 2, 3],
    [2, 'COPY', 1, 4],
    [3, 'DEC', 3],
    [4, 'DEC', 1],
    [5, 'TEST', 3, 1],
    [6, 'TEST', 1, 8],
    [7, 'GOTO', 3],
    [8, 'HALT'],
]

# 7. Sort X, Y, Z
# Registers 4, 5 and 6 show the results
sort = [

    [1, 'GOTO', 20],

    # Compare X and Y
    [2, 'COPY', 1, 7],
    [3, 'COPY', 2, 8],

    [4, 'DEC', 7],
    [5, 'DEC', 8],
    [6, 'TEST', 7, 10],
    [7, 'TEST', 8, 10],
    [8, 'GOTO', 4],

    [10, 'TEST', 8, 11],
    [11, 'GOTO', 14]

    # Compare the greater number to Z
    [12, 'COPY', 7, 4],
    [13, 'COPY', 8, 5],
    [14, 'GOTO', 18],

    [15, 'COPY', 8, 4],
    [16, 'COPY', 7, 5],
    [17, 'GOTO', 18],

    [18, 'COPY', 4, 7],
    [19, 'COPY', 3, 8],

    [20, 'DEC', 7],
    [21, 'DEC', 8],
    [22, 'TEST', 7, 25],
    [23, 'TEST', 8, 25],
    [24, 'GOTO', 18],

    [25, 'TEST', 7, 27]
    [26, 'GOTO', 31]

    # Order if Z is greatest
    [27, 'COPY', 5, 6],
    [28, 'COPY', 4, 5],
    [29, 'COPY', 3, 4],
    [30, 'GOTO', 60],

    # Else compare against the smaller of X and Y.
    [31, 'COPY', 5, 7]

    [60, 'HALT']

] 

CounterMachine(sort, [3, 1, 2])