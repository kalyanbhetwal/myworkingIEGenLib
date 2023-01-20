import iegenlib
import gc   
gc.disable()

spsComp = iegenlib.Computation()
spsComp.addDataSpace("C","int")

def fileRead():

    dataReads = iegenlib.PairVector([("C","{[0]->[0]}")])
    dataWrites =  iegenlib.PairVector([("C","{[0]->[0]}")])


    stmt1 = iegenlib.Stmt("C[t]=0;",
                        "{[t]:0<t<N}",
                        "{[t]->[0,t,0]}",
                        dataReads,
                        dataWrites      
                            )

    spsComp.addStmt(stmt1)

def fileComp():   
    dataReads = iegenlib.PairVector([("C","{[0]->[0]}")])
    dataWrites =  iegenlib.PairVector([("C","{[0]->[0]}")]) 
    stmt2 = iegenlib.Stmt("C[t] = C[t]+5;",
                    "{[t]:0<t<N }",
                    "{[t]->[1,t,0]}",
                    dataReads,
                    dataWrites
                    )

    spsComp.addStmt(stmt2)

def genCode():
    print(spsComp.codeGen())
    
