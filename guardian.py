import sudo

def createB():
    #sudoku no 6019
    # page 12 the guardian 7 apr 2023
    b = sudo.board()
    b.getElem(1,2).setValue(5)
    b.getElem(1,8).setValue(6)
    b.getElem(2,1).setValue(6)
    b.getElem(2,5).setValue(3)
    b.getElem(2,7).setValue(1)
    b.getElem(2,9).setValue(7)
    b.getElem(3,5).setValue(7)
    b.getElem(3,6).setValue(2)
    b.getElem(3,7).setValue(5)
    b.getElem(4,5).setValue(8)
    b.getElem(4,6).setValue(1)
    b.getElem(5,2).setValue(2)
    b.getElem(5,3).setValue(6)
    b.getElem(5,4).setValue(3)
    b.getElem(5,6).setValue(4)
    b.getElem(6,3).setValue(1)
    b.getElem(6,4).setValue(2)
    b.getElem(6,5).setValue(6)
    b.getElem(6,8).setValue(9)
    b.getElem(7,2).setValue(7)
    b.getElem(7,3).setValue(2)
    b.getElem(8,1).setValue(1)
    b.getElem(8,6).setValue(7)
    b.getElem(8,9).setValue(2)
    b.getElem(9,2).setValue(3)
    b.getElem(9,8).setValue(1)
    b.getElem(9,9).setValue(9)
    return b

def createC():
    b = sudo.board()
    boardDef="""2,5,2
                2,7,1
                2,8,7
                3,2,8
                3,3,1
                3,4,9
                3,6,3
                3,8,5
                4,5,5
                4,6,9
                4,7,3
                5,3,9
                5,6,4
                5,8,1
                6,1,6
                6,2,3
                6,7,4
                7,1,1
                7,2,7
                7,5,9
                7,7,2
                8,3,2
                8,4,7
                8,7,5
                9,1,4
                9,3,3
                9,4,2
"""
    for row, col, value in [l.split(",") for l in boardDef.split()]:
        b.getElem(int(row),int(col)).setValue(int(value))
    return b

def create6026():
    b = sudo.board()
    boardDef="""1,3,2
                2,1,1
    2,2,4
    2,7,3
    3,1,9
    3,5,6
    3,6,8
    3,8,5
    4,4,6
    4,7,1
    5,1,3
    5,2,7
    5,3,1
    5,7,5
    6,2,2
    6,4,4
    6,6,7
    7,5,7
    7,9,3
    8,4,1
    8,5,2
    8,8,8
    9,5,3
    9,7,9
    9,8,1
"""
    for row, col, value in [l.split(",") for l in boardDef.split()]:
        b.getElem(int(row),int(col)).setValue(int(value))
    return b

    
