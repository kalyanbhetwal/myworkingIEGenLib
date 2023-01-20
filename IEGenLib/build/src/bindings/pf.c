#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <byteswap.h>

#define WRITEINT(V,f) {uint32_t temp = bswap32(V); \
                         fwrite(&temp, 4, 1, f);}
#define READINT(V,f,err) {uint32_t buf; \
                         err = fread(&buf, 4, 1, f);\
                         uint32_t temp =  bswap32(buf);\
                         V = (int)temp;}
#define WRITEDOUBLE(V,f) {uint64_t t1 = *(uint64_t*)&V;\
                         t1 =  bswap64(t1); \
                         fwrite(&t1, 8, 1, f);}
#define READDOUBLE(V,f,err) {uint64_t buf; \
                         err = fread(&buf, 8, 1, f);\
                         uint64_t temp =  bswap64(buf);\
                         V = *(double*)&temp;}

#undef s0
#undef s_0
#undef s1
#undef s_1
#undef s2
#undef s_2
#undef s3
#undef s_3
#undef s4
#undef s_4
#undef s5
#undef s_5
#undef s6
#undef s_6
#define s_0(__x0)   m_fp = fopen( "hello.pfb", 'rb'); 
#define s0(c_0)   s_0(0);
#define s_1(__x0)   READDOUBLE(m_X,m_fp,errcheck);    READDOUBLE(m_Y,m_fp,errcheck);    READDOUBLE(m_Z,m_fp,errcheck);    READINT(m_nx,m_fp,errcheck);    READINT(m_ny,m_fp,errcheck);    READINT(m_nz,m_fp,errcheck);    READDOUBLE(m_dX,m_fp,errcheck);    READDOUBLE(m_dY,m_fp,errcheck);    READDOUBLE(m_dZ,m_fp,errcheck);    READINT(m_numSubgrids,m_fp,errcheck); 
#define s1(c_0)   s_1(0);
#define s_2(__x0)   m_data = (double*)malloc(sizeof(double)*m_nx*m_ny*m_nz); 
#define s2(c_0)   s_2(0);
#define s_3($nsg$)   READINT(x,m_fp,errcheck);READINT(y,m_fp,errcheck);READINT(z,m_fp,errcheck);READINT(nx,m_fp,errcheck);READINT(ny,m_fp,errcheck);READINT(nz,m_fp,errcheck);READINT(rx,m_fp,errcheck);READINT(ry,m_fp,errcheck);READINT(rz,m_fp,errcheck); 
#define s3(c_0, nsg, c_2)   s_3(nsg);
#define s_4($nsg$)   qq = z*m_nx*m_ny + y*m_nx + x; 
#define s4(c_0, nsg, c_2)   s_4(nsg);
#define s_5($nsg$, k, i)   index = qq+k*m_nx*m_ny+i*m_nx; buf = (uint64_t*)&(m_data[index]);read_count = fread(buf,8,nx,m_fp); 
#define s5(c_0, nsg, c_2, k, c_4, i, c_6)   s_5(nsg, k, i);
#define s_6($nsg$, k, i, j)   tmp = buf[j];  tmp = bswap64(tmp);  m_data[index+j] = *(double*)(&tmp); 
#define s6(c_0, nsg, c_2, k, c_4, i, c_6, j, c_8)   s_6(nsg, k, i, j);

int main(void){

    uint64_t*buf;
    long* byte_offsets;
    int clip_x;
    int errcheck;
    int extent_x;
    FILE* fp;
    double m_X;
    double m_Y;
    double m_Z;
    double m_dX;
    double m_dY;
    double m_dZ;
    double* m_data;
    FILE* m_fp;
    double m_numSubgrids;
    uint64_t m_nx;
    uint64_t m_ny;
    int m_nz;
    int m_p;
    int m_q;
    int m_r;
    int max_x_extent;
    int nsg;
    int nx;
    int ny;
    int nz;
    int qq;
    int rx;
    int ry;
    int rz;
    long long sg_count;
    uint64_t tmp;
    int x;
    int x_extent;
    int x_overlap;
    int y;
    int z;
    int t1, t2, t3, t4, t5, t6, t7, t8;
    long long index;
    int read_count;

t1 = 0; 
t2 = 0; 
t3 = 0; 
t4 = 0; 

s0(0);
s1(1);
s2(2);
for(t2 = 0; t2 <= m_numSubgrids-1; t2++) {
  s3(3,t2,0);
  s4(3,t2,1);
  if (ny >= 1) {
    for(t4 = 0; t4 <= nz-1; t4++) {
      for(t6 = 0; t6 <= ny-1; t6++) {
        s5(3,t2,2,t4,0,t6,0);
        for(t8 = 0; t8 <= nx-1; t8++) {
          s6(3,t2,2,t4,0,t6,1,t8,0);
        }
      }
    }
  }
}
}
#undef s0
#undef s_0
#undef s1
#undef s_1
#undef s2
#undef s_2
#undef s3
#undef s_3
#undef s4
#undef s_4
#undef s5
#undef s_5
#undef s6
#undef s_6
