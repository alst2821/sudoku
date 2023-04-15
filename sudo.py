# representation of a board
# squares, vert, horz

class board:
    def __init__(self):
        self.vgroups = []
        self.squares = []
        self.hgroups = []
        self.elems = [None]*81
        for i in range(9):
            self.vgroups.append(group("VERT",i+1))
            self.hgroups.append(group("HORZ",i+1))
            self.squares.append(group("SQUARE",i+1))
        for row in range(1,10):
            for col in range(1,10):
                index = (row-1)*9+col-1
                e = elem(self,row,col)
                #print(row,col, index)
                self.elems[index]=e
                e.getSquare().elems.append(e)
                e.getVert().elems.append(e)
                e.getHorz().elems.append(e)

    def getElem(self, row, col):
        index = (row-1)*9+col-1
        return self.elems[index]

    def countDefined(self):
        return len([e for e in self.elems if e.defined])

    def __repr__(self):
        repString = f"board with {self.countDefined()} elems"
        for row in range(1,10):
            rowString = "\n"
            for col in range(1,10):
                e = self.getElem(row,col)
                rowString += e.display()
            repString += rowString
        return repString

    def print(self):
        print("===")
        print(self.__repr__())
        print("===")

    def getFills(self):
        allgroups = []
        allgroups.extend(self.vgroups)
        allgroups.extend(self.hgroups)
        allgroups.extend(self.squares)

        # keep track of elems to detect conflict
        elems = set()
        fills = set()
        for g in allgroups:
            d=g.makeDict()
            for value in d:
                if len(d[value]) == 1:
                    t = (value, d[value][0])
                    if d[value][0] in elems:
                        if t in fills:
                            #the value is the same
                            pass
                        else:
                            s = f"conflict for {d[value][0]} value {value}"
                            for v,e in fills:
                                print(v,e)
                            raise NameError(s)
                    elems.add(d[value][0])
                    fills.add(t)
        return fills

    def missReport(self, name="b"):
        fills = self.getFills()
        for val, ee in fills:
            print(f"{name}.getElem({ee.row},{ee.col}).setValue({val})")

    def fillLevel1(self):
        fills = self.getFills()
        while len(fills) > 0:
            for val, ee in fills:
                self.getElem(ee.row,ee.col).setValue(val)
            if len(self.getLevel(0)) > 0:
                print("conflict detected")
            fills = self.getFills()

    def createReport(self):
        for e in self.elems:
            if e.defined:
                print(f"b.getElem({e.row},{e.col}).setValue({e.value})")

    def clone(self):
        bb = board()
        for e in self.elems:
            if e.defined:
                bb.getElem(e.row,e.col).setValue(e.value)
        return bb

    def getLevel(self, lvl):
        return [e for e in self.elems \
                if not e.defined \
                   and len(e.possible) == lvl]

    def showLevel(self, lvl):
        for e in self.getLevel(lvl):
            print(e, e.possible)

    def full(self):
        for e in self.elems:
            if not e.defined:
                return False
        return True

class elem:
    """ represent a square in a sudoku puzzle"""
    # row is 1..9
    # col is 1..9
    def __init__(self, board, row, col):
        "initialise"
        self.board = board
        self.row=row
        self.col=col
        self.value = None
        self.defined = False
        self.possible = UNIVERSE

    def getSquare(self):
        vpart = (self.row-1)//3
        hpart = (self.col-1)//3
        index = hpart + 3*vpart
        return self.board.squares[index]

    def getVert(self):
        return self.board.vgroups[self.col-1]

    def getHorz(self):
        return self.board.hgroups[self.row-1]

    def setValue(self, value):
        assert not self.defined, "already defined"
        self.defined = True
        self.value = value
        self.possible = None
        self.getSquare().setValue(value)
        self.getVert().setValue(value)
        self.getHorz().setValue(value)

    def display(self):
        if self.defined:
            return "%d " % self.value
        return "  "

    def resetValue(self):
        if self.defined:
            self.getSquare().setValue(self.value)
            self.getVert().setValue(self.value)
            self.getHorz().setValue(self.value)

    def __repr__(self):
        return "elem[row %d, col %d]" % (self.row, self.col)

UNIVERSE = set([1,2,3,4,5,6,7,8,9])

class group:
    # grouptype can be VERT, HORZ, SQUARE
    def __init__(self, grouptype, no):
        self.grouptype = grouptype
        self.no = no
        self.existing = set()
        self.missing = UNIVERSE
        self.elems = []

    def setValue(self, value):
        #value should be in missing set
        #assert value in self.missing, "Error setting value %d" % value
        self.existing.add(value)
        self.missing = set.difference(UNIVERSE, self.existing)
        for e in self.elems:
            if not e.defined:
                e.possible = set.difference(e.possible,self.existing)

    def __repr__(self):
        return "group %s, no %d" % (self.grouptype, self.no)

    def missCount(self):
        return len(self.missing)

    def makeDict(self):
        """create a dictionary of elements in the group that can take a
         given value """
        d = dict()
        for m in self.missing:
            d[m] = []
        for e in self.elems:
            if not e.defined:
                for k in d:
                    if k in e.possible:
                        d[k].append(e)
        return d

def createB():
    b = board()
#
    b.getElem(1,4).setValue(2)
    b.getElem(1,9).setValue(3)
#
    b.getElem(2,3).setValue(8)
    b.getElem(2,6).setValue(6)
    b.getElem(2,7).setValue(2)
    b.getElem(2,8).setValue(4)
#
    b.getElem(3,4).setValue(9)
    b.getElem(3,5).setValue(3)
    b.getElem(3,8).setValue(1)
#
    b.getElem(4,2).setValue(5)
    b.getElem(4,3).setValue(7)
    b.getElem(4,7).setValue(6)
    b.getElem(4,9).setValue(1)
#
    b.getElem(5,2).setValue(2)
    b.getElem(5,5).setValue(1)
    b.getElem(5,8).setValue(5)
#
    b.getElem(6,1).setValue(1)
    b.getElem(6,3).setValue(6)
    b.getElem(6,7).setValue(8)
    b.getElem(6,8).setValue(7)
#
    b.getElem(7,2).setValue(9)
    b.getElem(7,5).setValue(8)
    b.getElem(7,6).setValue(5)
#
    b.getElem(8,2).setValue(8)
    b.getElem(8,3).setValue(3)
    b.getElem(8,4).setValue(4)
    b.getElem(8,7).setValue(9)
#
    b.getElem(9,1).setValue(4)
    b.getElem(9,6).setValue(9)
    return b

def createA():
    b = board()
#
    b.getElem(1,2).setValue(3)
#
    b.getElem(2,3).setValue(8)
    b.getElem(2,6).setValue(5)
    b.getElem(2,8).setValue(1)
#
    b.getElem(3,1).setValue(7)
    b.getElem(3,5).setValue(2)
    b.getElem(3,6).setValue(6)
    b.getElem(3,7).setValue(9)
    b.getElem(3,9).setValue(5)
#
    b.getElem(4,2).setValue(5)
    b.getElem(4,4).setValue(6)
    b.getElem(4,5).setValue(7)
#
    b.getElem(5,3).setValue(3)
    b.getElem(5,7).setValue(1)
#
    b.getElem(6,5).setValue(9)
    b.getElem(6,6).setValue(3)
    b.getElem(6,8).setValue(5)
#
    b.getElem(7,1).setValue(4)
    b.getElem(7,3).setValue(2)
    b.getElem(7,4).setValue(5)
    b.getElem(7,5).setValue(6)
    b.getElem(7,9).setValue(7)
#
    b.getElem(8,2).setValue(6)
    b.getElem(8,4).setValue(9)
    b.getElem(8,7).setValue(2)
#
    b.getElem(9,8).setValue(8)
    return b


def main():
    print("hello")
    b = createB()
    for e in b.elems:
        e.resetValue()
    b.print()


if __name__ == "__main__":
    main()
