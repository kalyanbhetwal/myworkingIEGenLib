import iegenlib
import gc  
import inspect 
from pprint import pprint
gc.disable()


parflowio = iegenlib.Computation()
parflowio.addDataSpace("C","int")
parflowio.addDataSpace("nsg", "int")
parflowio.addDataSpace("x", "int")
parflowio.addDataSpace("y", "int")
parflowio.addDataSpace("z", "int")
parflowio.addDataSpace("nx", "int")
parflowio.addDataSpace("ny", "int")
parflowio.addDataSpace("nz", "int")
parflowio.addDataSpace("rx", "int")
parflowio.addDataSpace("ry", "int")
parflowio.addDataSpace("rz", "int")
parflowio.addDataSpace("errcheck", "int")
parflowio.addDataSpace("x_overlap", "int")
parflowio.addDataSpace("clip_x", "int")
parflowio.addDataSpace("extent_x", "int")
parflowio.addDataSpace("qq", "int")
parflowio.addDataSpace("tmp", "uint64_t")
parflowio.addDataSpace("buf", "uint64_t")

parflowio.addDataSpace("m_p", "int")
parflowio.addDataSpace("m_q", "int")
parflowio.addDataSpace("m_r", "int")
parflowio.addDataSpace("fp", "file*")
parflowio.addDataSpace("m_X", "double")
parflowio.addDataSpace("m_Y", "double")
parflowio.addDataSpace("m_Z", "double")
parflowio.addDataSpace("m_nx","uint64_t")
parflowio.addDataSpace("m_ny", "uint64_t")
parflowio.addDataSpace("m_nz", "int")
parflowio.addDataSpace("m_dX", "double")
parflowio.addDataSpace("m_dY", "double")
parflowio.addDataSpace("m_dZ", "double")
parflowio.addDataSpace("m_numSubgrids", "double")
parflowio.addDataSpace("max_x_extent", "int")
parflowio.addDataSpace("byte_offsets", "long*")
parflowio.addDataSpace("sg_count", "long long")
parflowio.addDataSpace("x_extent", "int")
parflowio.addDataSpace("m_fp", "file*")
parflowio.addDataSpace("m_data", "double*")

def readFile(fileName):

    dataReads0 = iegenlib.PairVector([])
    dataWrites0 =  iegenlib.PairVector([("m_fp","{[0]->[0]}")])


    s0 = iegenlib.Stmt("m_fp = fopen( m_filename.c_str(), 'rb');",
                        "{[0]}",
                        "{[0]->[0]}",
                        dataReads0,
                        dataWrites0)
    parflowio.addStmt(s0);  

    dataReads1 = iegenlib.PairVector([])
    dataWrites1 =  iegenlib.PairVector([("m_X","{[0]->[0]}"),\
                                        ("m_Y","{[0]->[0]}"),\
                                        ("m_Z","{[0]->[0]}"),\
                                        ("m_nx","{[0]->[0]}"),\
                                        ("m_ny","{[0]->[0]}"),\
                                        ("m_nz","{[0]->[0]}"),\
                                        ("m_dX","{[0]->[0]}"),\
                                        ("m_dY","{[0]->[0]}"),\
                                        ("m_dZ","{[0]->[0]}"),\
                                       ("m_numSubgrids","{[0]->[0]}")])

    s1 = iegenlib.Stmt("READDOUBLE(m_X,m_fp,errcheck);    READDOUBLE(m_Y,m_fp,errcheck);    READDOUBLE(m_Z,m_fp,errcheck);    READINT(m_nx,m_fp,errcheck);    READINT(m_ny,m_fp,errcheck);    READINT(m_nz,m_fp,errcheck);    READDOUBLE(m_dX,m_fp,errcheck);    READDOUBLE(m_dY,m_fp,errcheck);    READDOUBLE(m_dZ,m_fp,errcheck);    READINT(m_numSubgrids,m_fp,errcheck);",
                        "{[0]}",
                        "{[0]->[1]}",
                        dataReads1,
                        dataWrites1      
                            )

    parflowio.addStmt(s1)

    dataReads2 = iegenlib.PairVector([])
    dataWrites2 =  iegenlib.PairVector([ ("m_nx","{[0]->[0]}"),\
                                        ("m_ny","{[0]->[0]}"),\
                                        ("m_nz","{[0]->[0]}")])



    s2 = iegenlib.Stmt("m_data = (double*)std::malloc(sizeof(double)*m_nx*m_ny*m_nz);",
                        "{[0]}",
                        "{[0]->[2]}",
                        dataReads2,
                        dataWrites2)
    parflowio.addStmt(s2)


    dataReads3 = iegenlib.PairVector([])
    dataWrites3 =  iegenlib.PairVector([("x","{[nsg]->[0]}"),\
                                        ("y","{[nsg]->[0]}"),\
                                        ("z","{[nsg]->[0]}"),\
                                        ("nx","{[nsg]->[0]}"),\
                                        ("ny","{[nsg]->[0]}"),\
                                        ("nz","{[nsg]->[0]}"),\
                                        ("rx","{[nsg]->[0]}"),\
                                        ("ry","{[nsg]->[0]}"),\
                                         ("rz","{[nsg]->[0]}")])

    s3 = iegenlib.Stmt("READINT(x,m_fp,errcheck);READINT(y,m_fp,errcheck);READINT(z,m_fp,errcheck);READINT(nx,m_fp,errcheck);READINT(ny,m_fp,errcheck);READINT(nz,m_fp,errcheck);READINT(rx,m_fp,errcheck);READINT(ry,m_fp,errcheck);READINT(rz,m_fp,errcheck);",
                        "{[nsg]:0 <= nsg < m_numSubgrids}",
                        "{[0]->[3,nsg,0]}",
                        dataReads3,
                        dataWrites3)
    parflowio.addStmt(s3)  


    dataReads4 = iegenlib.PairVector([])
    dataWrites4 =  iegenlib.PairVector([ ("m_numSubgrids","{[nsg]->[0]}"),\
                                        ("m_ny","{[nsg]->[0]}"),\
                                        ("m_nx","{[nsg]->[0]}"),\
                                        ("x","{[nsg]->[0]}"),\
                                        ("y","{[nsg]->[0]}"),\
                                         ("z","{[nsg]->[0]}")])


    s4 = iegenlib.Stmt("qq = z*m_nx*m_ny + y*m_nx + x;",
                        "{[nsg]:0 <= nsg < m_numSubgrids}",
                        "{[0]->[3,nsg,1]}",
                        dataReads4,
                        dataWrites4)
    parflowio.addStmt(s4)  



    dataReads5 = iegenlib.PairVector([])
    dataWrites5 =  iegenlib.PairVector([ ("m_numSubgrids","{[nsg]->[0]}"),\
                                        ("m_ny","{[nsg]->[0]}"),\
                                        ("m_nx","{[nsg]->[0]}"),\
                                        ("nx","{[nsg]->[0]}"),\
                                        ("ny","{[nsg]->[0]}"),\
                                         ("nz","{[nsg]->[0]}"),\
                                        ("m_data","{[nsg,k,i]->[0]}"),\
                                        ("qq","{[nsg,k,i]->[0]}")])


    s5 = iegenlib.Stmt("index = qq+k*m_nx*m_ny+i*m_nx; buf = (uint64_t*)&(m_data[index]);read_count = fread(buf,8,nx,m_fp);",
                        "{[nsg,k,i] : 0 <= k < nz && 0<=i<ny && 0 <= nsg < m_numSubgrids}",
                        "{[nsg,k,i]->[3, nsg,2, k, 0,i,0]}",
                        dataReads5,
                        dataWrites5)
    parflowio.addStmt(s5)  


    dataReads6 = iegenlib.PairVector([])
    dataWrites6 =  iegenlib.PairVector([ ("m_numSubgrids","{[nsg]->[0]}"),\
                                        ("buf","{[nsg,k,i]->[0]}"),\
                                        ("nx","{[nsg,k,i,j]->[0]}"),\
                                        ("ny","{[nsg,k,i,j]->[0]}"),\
                                         ("nz","{[nsg,k,i,j]->[0]}"),\
                                        ("index","{[nsg,k,i,j]->[0]}")])


    s6 = iegenlib.Stmt("tmp = buf[j];  tmp = bswap64(tmp);  m_data[index+j] = *(double*)(&tmp);",
                        "{[nsg,k,i,j] :0 <= k < nz && 0<=i<ny && 0 <= nsg < m_numSubgrids && 0<=j<nx }",
                        "{[nsg,k,i,j]->[3, nsg,2, k, 0,i,1,j,0]}",
                        dataReads6,
                        dataWrites6)
    parflowio.addStmt(s6)  


    

    print(parflowio.codeGen())

    #print("hello_"+ fileName)


readFile("test.pfb")


