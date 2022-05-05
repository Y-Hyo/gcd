import random
import binary
import Euclidean
import time
import sys
sys.setrecursionlimit(100000000)

a = []
b = []

########## 비트크기 정의
size = 128 #-bits
times = 100000 # 반복횟수

for i in range(times):
    a.append(random.randrange(2**(size-1),2**(size)-1))
    b.append(random.randrange(2**(size-1),2**(size)-1))



#euclide-itr
start = time.time()
for i in range(0,times):
    Euclidean.itr_euclidean(a[i], b[i])
end =time.time()
print("euclidean-ite {}-bit".format(size))
print((end-start)/times)

#euclide-rec
start = time.time()
for i in range(0,times):
    Euclidean.rec_euclidean(a[i], b[i])
end =time.time()
print("euclidean-rec {}-bit".format(size))
print((end-start)/times)

print( )

#binary-itr
start = time.time()
for i in range(0,times):
    binary.itr_binary(a[i], b[i])
end =time.time()
print("binary-itr {}-bit".format(size))
print((end-start)/times)

#binary-rec
start = time.time()
for i in range(0,times):
    binary.rec_binary(a[i], b[i])
end =time.time()
print("euclidean-rec {}-bit".format(size))
print((end-start)/times)

print()
#binary-itr-bit operation
start = time.time()
for i in range(0,times):
    binary.itr_binary_bitop(a[i], b[i])
end =time.time()
print("binary-itr bit opertion {}-bit".format(size))
print((end-start)/times)

#binary-rec
start = time.time()
for i in range(0,times):
    binary.rec_binary_bitop(a[i], b[i])
end =time.time()
print("euclidean-rec bit operation {}-bit".format(size))
print((end-start)/times)