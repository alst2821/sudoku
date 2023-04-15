import sudo

def createB():
    #sudoku no 6190
    # daily telegraph 10 Apr 2023 pg 16
    # board with 81 elems
    # 6 5 8 9 4 1 7 2 3 
    # 4 7 9 6 2 3 8 1 5 
    # 1 2 3 5 8 7 9 6 4 
    # 8 3 1 2 9 5 6 4 7 
    # 2 6 7 1 3 4 5 8 9 
    # 9 4 5 8 7 6 2 3 1 
    # 3 9 6 7 1 2 4 5 8 
    # 5 8 4 3 6 9 1 7 2 
    # 7 1 2 4 5 8 3 9 6 
    b = sudo.board()
    b.getElem(1,4).setValue(9)
    b.getElem(1,5).setValue(4)
    b.getElem(1,6).setValue(1)
    b.getElem(1,7).setValue(7)
    b.getElem(2,2).setValue(7)
    b.getElem(2,7).setValue(8)
    b.getElem(2,9).setValue(5)
    b.getElem(3,4).setValue(5)
    b.getElem(4,2).setValue(3)
    b.getElem(4,3).setValue(1)
    b.getElem(4,6).setValue(5)
    b.getElem(5,2).setValue(6)
    b.getElem(5,8).setValue(8)
    b.getElem(6,4).setValue(8)
    b.getElem(6,7).setValue(2)
    b.getElem(6,8).setValue(3)
    b.getElem(7,4).setValue(7)
    b.getElem(7,6).setValue(2)
    b.getElem(8,1).setValue(5)
    b.getElem(8,3).setValue(4)
    b.getElem(8,8).setValue(7)
    b.getElem(9,3).setValue(2)
    b.getElem(9,5).setValue(5)
    b.getElem(9,6).setValue(8)
    b.getElem(9,7).setValue(3)
    return b

