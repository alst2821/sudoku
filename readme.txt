sudoku exercise

scripts to solve sudokus, with examples

Algorithm to solve:
1. build the board "b" , examples in guardian, times, daily, etc.
2. fill the board to level1
    b.fillLevel1()
    
3. if not complete, then search for 'level2' nodes
    b.showLevel(2)
    
4. clone board twice
   b1 = b.clone()
   b2 = b.clone()

5. Attempt a fill from first entry in list from step #3
   b1.getElem(row,col).setValue(val)
   b1.fillLevel1()

   Solved?
   if there's inconsistencies, there will be an exception raised
   i.e. NameError raised would alert of a conflict/collision

   if so, try using b2, using second option
   b2.getElem(row,col).setValue(val)
   b2.fillLevel1()
   
All examples were solved using this method.
Method not yet automated!


