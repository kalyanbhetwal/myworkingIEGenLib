import iegenlib
import gc  
import inspect 
from pprint import pprint
gc.disable()


parflowio = iegenlib.Computation()
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
parflowio.addDataSpace("fp", "FILE*")
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

parflowio.addDataSpace("mean", "double*")
parflowio.addDataSpace("sum", "double")

parflowio.addDataSpace("_offsets", "long")

parflowio.addDataSpace("writeBuf", "double")

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


    dataReads2 =  iegenlib.PairVector([ ("m_nx","{[0]->[0]}"),\
                                        ("m_ny","{[0]->[0]}"),\
                                        ("m_nz","{[0]->[0]}")])
    dataWrites2 = iegenlib.PairVector([("m_data","{[0]->[0]}")])



    s2 = iegenlib.Stmt("m_data = (double*)malloc(sizeof(double)*m_nx*m_ny*m_nz);",
                        "{[0]}",
                        "{[0]->[2]}",
                        dataReads2,
                        dataWrites2)
    parflowio.addStmt(s2)


    dataReads3 = iegenlib.PairVector([("m_numSubgrids","{[nsg]->[0]}")])
    dataWrites3 =  iegenlib.PairVector([("x","{[nsg]->[0]}"),\
                                        ("y","{[nsg]->[0]}"),\
                                        ("z" ,"{[nsg]->[0]}"),\
                                        ("nx","{[nsg]->[0]}"),\
                                        ("ny","{[nsg]->[0]}"),\
                                        ("nz","{[nsg]->[0]}"),\
                                        ("rx","{[nsg]->[0]}"),\
                                        ("ry","{[nsg]->[0]}"),\
                                         ("rz","{[nsg]->[0]}")])

    s3 = iegenlib.Stmt("READINT(x,m_fp,errcheck);READINT(y,m_fp,errcheck);READINT(z,m_fp,errcheck);READINT(nx,m_fp,errcheck);READINT(ny,m_fp,errcheck);READINT(nz,m_fp,errcheck);READINT(rx,m_fp,errcheck);READINT(ry,m_fp,errcheck);READINT(rz,m_fp,errcheck);",
                        "{[nsg]:0 <= nsg < m_numSubgrids}",
                        "{[nsg]->[3,nsg,0]}",
                        dataReads3,
                        dataWrites3)
    parflowio.addStmt(s3)  


    dataReads4 = iegenlib.PairVector([("qq" ,"{[nsg]->[0]}")])
    dataWrites4 =  iegenlib.PairVector([ ("m_numSubgrids","{[nsg]->[0]}"),\
                                        ("m_ny","{[nsg]->[0]}"),\
                                        ("m_nx","{[nsg]->[0]}"),\
                                        ("x","{[nsg]->[0]}"),\
                                        ("y","{[nsg]->[0]}"),\
                                         ("z","{[nsg]->[0]}")])


    s4 = iegenlib.Stmt("qq = z*m_nx*m_ny + y*m_nx + x;",
                        "{[nsg]:0 <= nsg < m_numSubgrids}",
                        "{[nsg]->[3,nsg,1]}",
                        dataReads4,
                        dataWrites4)
    parflowio.addStmt(s4)  



   
    dataReads5 =  iegenlib.PairVector([ ("m_numSubgrids","{[nsg]->[0]}"),\
                                        ("m_ny","{[nsg]->[0]}"),\
                                        ("m_nx","{[nsg]->[0]}"),\
                                        ("nx","{[nsg]->[0]}"),\
                                        ("ny","{[nsg]->[0]}"),\
                                         ("nz","{[nsg]->[0]}"),\
                                        ("m_data","{[nsg,k,i]->[0]}"),\
                                        ("qq","{[nsg,k,i]->[0]}")])

    dataWrites5 = iegenlib.PairVector([("m_fp", "{[nsg] -> [0]}"),\
                ("buf", "{[nsg,k,i] -> [0]}"),\
                ("index", "{[nsg,k,i] -> [0]}")])
                
    s5 = iegenlib.Stmt("index = qq+k*m_nx*m_ny+i*m_nx; buf = (uint64_t*)&(m_data[index]);read_count = fread(buf,8,nx,m_fp);",
                        "{[nsg,k,i] : 0 <= k < nz && 0<=i<ny && 0 <= nsg < m_numSubgrids}",
                        "{[nsg,k,i]->[3, nsg,2, k, 0,i,0]}",
                        dataReads5,
                        dataWrites5)
    parflowio.addStmt(s5)  


    
    dataReads6 =  iegenlib.PairVector([ ("m_numSubgrids","{[nsg]->[0]}"),\
                                        ("buf","{[nsg,k,i]->[0]}"),\
                                        ("nx","{[nsg,k,i,j]->[0]}"),\
                                        ("ny","{[nsg,k,i,j]->[0]}"),\
                                         ("nz","{[nsg,k,i,j]->[0]}"),\
                                        ("index","{[nsg,k,i,j]->[0]}")])

    dataWrites6 = iegenlib.PairVector([ ("tmp", "{[nsg,k,i,j] -> [0]}"),\
                                        ("m_data", "{[nsg,k,i,j] -> [0]}")])


    s6 = iegenlib.Stmt("tmp = buf[j];  tmp = bswap64(tmp);  m_data[index+j] = *(double*)(&tmp);",
                        "{[nsg,k,i,j] :0 <= k < nz && 0<=i<ny && 0 <= nsg < m_numSubgrids && 0<=j<nx }",
                        "{[nsg,k,i,j]->[3, nsg,2, k, 0,i,1,j,0]}",
                        dataReads6,
                        dataWrites6)
    parflowio.addStmt(s6)  
    return parflowio
    #print(parflowio.codeGenMemoryManagementString())
    #print(parflowio.codeGen())


def compute_mean():
    parflowio_mean = iegenlib.Computation()

    dataReads1 =  iegenlib.PairVector([])
    dataWrites1 = iegenlib.PairVector([("mean","{[0]->[0]}")])



    s1 = iegenlib.Stmt("m_data = (double*)malloc(sizeof(double)m_ny*m_nz);",
                        "{[0]}",
                        "{[0]->[0]}",
                        dataReads1,
                        dataWrites1)
    parflowio_mean.addStmt(s1)
    

    dataReads3 =  iegenlib.PairVector([])
    dataWrites3 = iegenlib.PairVector([("sum","{[0]->[0]}")])



    s3 = iegenlib.Stmt("sum=0;",
                        "{[y,x]:0<=y<m_ny && 0<=x<m_nx}",
                        "{[y,x]->[0,y,0,x,0]}",
                        dataReads3,
                        dataWrites3)
    parflowio_mean.addStmt(s3)


    dataReads4 =  iegenlib.PairVector([("m_data","{[0]->[0]}")])
    dataWrites4 = iegenlib.PairVector([("sum","{[0]->[0]}")])

    s4 = iegenlib.Stmt("sum+=m_data[(long long)(z)*m_ny*m_nx+y*m_nx+x];",
                        "{[y,x,z]:0<=y<m_ny && 0<=x<m_nx && 0<=z<m_nz}",
                        "{[y,x,z]->[0,y,0,x,1,z,0]}",
                        dataReads4,
                        dataWrites4)
    parflowio_mean.addStmt(s4)



    dataReads5 =  iegenlib.PairVector([("m_data","{[0]->[0]}")])
    dataWrites5 = iegenlib.PairVector([("sum","{[0]->[0]}")])

    s5 = iegenlib.Stmt("mean[x+y*m_nx] = sum/m_nz;",
                        "{[y,x]:0<=y<m_ny && 0<=x<m_nx}",
                        "{[y,x]->[0,y,0,x,2]}",
                        dataReads5,
                        dataWrites5)
    parflowio_mean.addStmt(s5)

    return parflowio_mean


def writeFile(filename):
    parflowio_write = iegenlib.Computation()

    dataReads1 =  iegenlib.PairVector([])
    dataWrites1 = iegenlib.PairVector([("_offsets","{[0]->[0]}")])

    s1 = iegenlib.Stmt("_offsets = (long*)malloc(sizeof(long)(m_p*m_q*m_r) + 1);",
                        "{[0]}",
                        "{[0]->[0]}",
                        dataReads1,
                        dataWrites1)
    parflowio_write.addStmt(s1)

    dataReads2 = iegenlib.PairVector([])
    dataWrites2 =  iegenlib.PairVector([("fp","{[0]->[0]}")])

    s2 = iegenlib.Stmt("fp = std::fopen(filename.c_str(), 'wb');",
                        "{[0]}",
                        "{[0]->[1]}",
                        dataReads2,
                        dataWrites2)
    parflowio_write.addStmt(s2) 

    dataReads3 =  iegenlib.PairVector([("fp","{[0]->[0]}"),\
                                    ("m_p", "{[0]->[0]}"),\
                                    ("m_q", "{[0]->[0]}"),\
                                    ("m_r", "{[0]->[0]}"),\
                                    ("m_X", "{[0]->[0]}"),\
                                    ("m_Y", "{[0]->[0]}"),\
                                    ("m_Z", "{[0]->[0]}"),\
                                    ("m_nx", "{[0]->[0]}"),\
                                    ("m_ny", "{[0]->[0]}"),\
                                    ("m_nz", "{[0]->[0]}"),\
                                    ("m_dX", "{[0]->[0]}"),\
                                    ("m_dY", "{[0]->[0]}"),\
                                    ("m_dZ", "{[0]->[0]}"),\
                                    ("m_numSubgrids", "{[0]->[0]}")\
                                     ])
    dataWrites3 = iegenlib.PairVector([("m_numSubgrids", "{[0]->[0]}"),\
                    ("max_x_extent", "{[0]->[0]}"),\
                    ("fp", "{[0]->[0]}")])

    s3 = iegenlib.Stmt("m_numSubgrids = m_p * m_q * m_r;    WRITEDOUBLE(m_X,fp);    WRITEDOUBLE(m_Y,fp);    WRITEDOUBLE(m_Z,fp);    WRITEINT(m_nx,fp);    WRITEINT(m_ny,fp);    WRITEINT(m_nz,fp);    WRITEDOUBLE(m_dX,fp);    WRITEDOUBLE(m_dY,fp);    WRITEDOUBLE(m_dZ,fp);    WRITEINT(m_numSubgrids,fp);max_x_extent =calcExtent(m_nx,m_p,0);",
                        "{[0]}",
                        "{[0]->[2]}",
                        dataReads3,
                        dataWrites3)
    parflowio_write.addStmt(s3)
 
    dataReads4 = iegenlib.PairVector([("max_x_extent","{[0]->[0]}")]) 
    dataWrites4 =  iegenlib.PairVector([("writeBuf","{[0]->[0]}")])

    s4 = iegenlib.Stmt("writeBuf = (long*)malloc(sizeof(long)*max_x_extent);",
                        "{[0]}",
                        "{[0]->[3]}",
                        dataReads4,
                        dataWrites4)
    parflowio_write.addStmt(s4)

    # nsg=0; byte_offsets[0] = 0;sg_count = 1;
 
    dataReads5 = iegenlib.PairVector([("nsg","{[0]->[0]}"),\
                                    ("byte_offsets","{[0]->[0]}"),\
                                     ("sg_count","{[0]->[0]}")]) 
    dataWrites5 =  iegenlib.PairVector([("writeBuf","{[0]->[0]}")])

    s5 = iegenlib.Stmt("nsg=0; byte_offsets[0] = 0;sg_count = 1;",
                        "{[0]}",
                        "{[0]->[4]}",
                        dataReads5,
                        dataWrites5)
    parflowio_write.addStmt(s5)

 
    dataReads6 = iegenlib.PairVector([("m_X", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("m_Y", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("m_Z", "{[nsg_z, nsg_y, nsg_x]->[0]}"),
                                   ("m_nx", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("m_p", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("nsg_x", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("m_ny", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("m_q", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("nsg_y", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("m_nz", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("m_r", "{[nsg_z, nsg_y, nsg_x]->[0]}"),\
                                   ("nsg_z", "{[nsg_z, nsg_y, nsg_x]->[0]}")
                                   ]) 
    dataWrites6 =  iegenlib.PairVector([("fp", "{[nsg_z, nsg_y, nsg_x]->[0]}")])

    s6 = iegenlib.Stmt("x = m_X + calcOffset(m_nx,m_p,nsg_x);y = m_Y + calcOffset(m_ny,m_q,nsg_y);z = m_Z + calcOffset(m_nz,m_r,nsg_z);WRITEINT(x, fp);WRITEINT(y, fp);WRITEINT(z, fp);x_extent =calcExtent(m_nx,m_p,nsg_x);WRITEINT(x_extent, fp);WRITEINT(calcExtent(m_ny,m_q,nsg_y), fp);WRITEINT(calcExtent(m_nz,m_r,nsg_z), fp);WRITEINT(1, fp);WRITEINT(1, fp);WRITEINT(1, fp);",
                        "{[nsg_z, nsg_y, nsg_x]: 0<= nsg_z< m_r &&  0<= nsg_y< m_q &&  0<= nsg_x< m_p  }",
                        "{[nsg_z, nsg_y, nsg_x]->[5,nsg_z,0,nsg_y,0,nsg_x,0]}",
                        dataReads6,
                        dataWrites6)
    parflowio_write.addStmt(s6)


 
    dataReads7 = iegenlib.PairVector([("nsg","{[0]->[0]}"),\
                                    ("byte_offsets","{[0]->[0]}"),\
                                     ("sg_count","{[0]->[0]}")]) 
    dataWrites7 =  iegenlib.PairVector([("writeBuf","{[0]->[0]}")])

    s7 = iegenlib.Stmt("buf = (uint64_t*)&(m_data[iz*m_nx*m_ny+iy*m_nx+calcOffset(m_nx,m_p,nsg_x)]);",
                        "{[nsg_z, nsg_y, nsg_x, iz, iy]: 0<= nsg_z< m_r &&  0<= nsg_y< m_q &&  0<= nsg_x< m_p   && calcOffset(m_nz,m_r,nsg_z)  <=iz< calcOffset(m_nz,m_r,nsg_z) && calcOffset(m_ny,m_q,nsg_y) <=iz< calcOffset(m_ny,m_q,nsg_y)}",
                        "{[nsg_z, nsg_y, nsg_x, iz, iy]->[5,nsg_z,0,nsg_y,0,nsg_x,1,iz,0,iy,0]}",
                        dataReads7,
                        dataWrites7)
    parflowio_write.addStmt(s7)

    return parflowio_write
    

parflowiox_readFile = iegenlib.Computation()
parflowiox_readFile = readFile("test.pfb")

parflowiox_mean = iegenlib.Computation()
parflowiox_mean = compute_mean()

result = parflowiox_readFile.appendComputation(parflowiox_mean, "{[0]}","{[0]->[4]}")
#print(result.tuplePosition,  result.returnValues)


parflowiox_writeFile = iegenlib.Computation()
parflowiox_writeFile = writeFile("hello.pfb")

update_ES = "{[0]->[" +str((result.tuplePosition+1))+"]}"
result2 = parflowiox_readFile.appendComputation(parflowiox_writeFile, "{[0]}",update_ES)
print(parflowiox_readFile.codeGen())