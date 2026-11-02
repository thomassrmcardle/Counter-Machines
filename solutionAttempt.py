countLimit = 10000

def CounterMachine(Instructions,Registers):
    Index = 1
    CurrentInstr = Instructions[Index-1][1]
    Count = 0
    while CurrentInstr != 'HALT' and Count < countLimit:
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

attempt = [
    [2, 'TEST', 1, 4],
    [3, 'TEST', 2, 5],
    
    [4, 'DEC', 1],
    [5, 'GOTO', 1],

    [6, 'DEC', 2],
    [7, 'GOTO', 1],
    
    [8, 'HALT']
]

CounterMachine(attempt, [0,0])