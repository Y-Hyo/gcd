import random
import binary
import Euclidean
import time
import sys
sys.setrecursionlimit(10000)

a = []
b = []

########## 비트크기 정의
size = 3096 #-bits
for i in range(1000):
    a.append(random.randrange(2**(size-1),2**(size)-1))
    b.append(random.randrange(2**(size-1),2**(size)-1))



#euclide-itr
start = time.time()
for i in range(0,1000):
    Euclidean.itr_euclidean(a[i], b[i])
end =time.time()
print("euclidean-ite {}-bit".format(size))
print((end-start)/1000)

#euclide-rec
start = time.time()
for i in range(0,1000):
    Euclidean.rec_euclidean(a[i], b[i])
end =time.time()
print("euclidean-rec {}-bit".format(size))
print((end-start)/1000)

print( )

#binary-itr
start = time.time()
for i in range(0,1000):
    binary.itr_binary(a[i], b[i])
end =time.time()
print("binary-itr {}-bit".format(size))
print((end-start)/1000)

#binary-rec
start = time.time()
for i in range(0,1000):
    binary.rec_binary(a[i], b[i])
end =time.time()
print("euclidean-rec {}-bit".format(size))
print((end-start)/1000)