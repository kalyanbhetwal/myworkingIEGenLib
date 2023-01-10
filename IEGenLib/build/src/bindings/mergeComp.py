import iegenlib
import gc  
import inspect 
from pprint import pprint


gc.disable()
#spsComp1 = iegenlib.Computation()

def comp1():
    spsComp1 = iegenlib.Computation()
    spsComp1.addDataSpace("C","int")
    dataReads = iegenlib.PairVector([])
    dataWrites =  iegenlib.PairVector([("foo","{[0]->[0]}")])
    stmt1 = iegenlib.Stmt("foo=1;",
                    "{[0]}",
                    "{[0]->[0]}",
                    dataReads,
                    dataWrites)
    #print(stmt1)
    spsComp1.addStmt(stmt1)
    return spsComp1


def comp2():
    spsComp2 = iegenlib.Computation()
    spsComp2.addDataSpace("C","int")
    dataReads = iegenlib.PairVector([])
    dataWrites =  iegenlib.PairVector([("foo","{[0]->[0]}")])
    stmt1 = iegenlib.Stmt("bar=1;",
                    "{[0]}",
                    "{[0]->[0]}",
                    dataReads,
                    dataWrites)
    spsComp2.addStmt(stmt1)
    return spsComp2
    
compx = iegenlib.Computation()
compx = comp1()

compy = iegenlib.Computation()
compy = comp2()

compx.appendComputation(compy, "{[0]}","{[0]->[1]}")
print(compx.printInfo())
#print(compy.codeGen())
#pprint(inspect.getmembers(comp))
#comp.printInfo()