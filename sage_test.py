import random
import binary
import Euclidean

import sys
sys.setrecursionlimit(100000000)

########## 비트크기 정의
size = 128 #-bits
times = 300 # 반복횟수

a = []
b = []
for i in range(times):
    a.append(random.randrange(2**(size-1),(2**size)-1))
    b.append(random.randrange(2**(size-1),(2**size)-1))



## 유클리드
# for i in range(times):
#     d = Euclidean.itr_euclidean(a[i], b[i])
#     print("if gcd({},{}) != {} :".format(a[i],b[i],d))
#     print("\t print({},{})".format(a[i],b[i]))

# for i in range(times):
#     d = Euclidean.rec_euclidean(a[i], b[i])
#     print("if gcd({},{}) != {} :".format(a[i],b[i],d))
#     print("\t print({},{})".format(a[i],b[i]))

### 바이너리
# for i in range(times):
#     d = binary.rec_binary(a[i], b[i])
#     print("if gcd({},{}) != {} :".format(a[i],b[i],d))
#     print("\t print({},{})".format(a[i],b[i]))

# for i in range(times):
#     d = binary.itr_binary(a[i], b[i])
#     print("if gcd({},{}) != {} :".format(a[i],b[i],d))
#     print("\t print({},{})".format(a[i],b[i]))

### 바이너리 비트연산
for i in range(times):
    d = binary.rec_binary_bitop(a[i], b[i])
    print("if gcd({},{}) != {} :".format(a[i],b[i],d))
    print("\t print({},{})".format(a[i],b[i]))

for i in range(times):
    d = binary.itr_binary_bitop(a[i], b[i])
    print("if gcd({},{}) != {} :".format(a[i],b[i],d))
    print("\t print({},{})".format(a[i],b[i]))