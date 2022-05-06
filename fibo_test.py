import random
import binary
import Euclidean
import time
import sys
sys.setrecursionlimit(100000000)

times = 1000
bitsize = 2048

def fibo_itr(bit_size):
    t0 = 0
    t1 = 1
    temp =0
    while bit_size != t1.bit_length():
        temp = t0 + t1
        t0 = t1
        t1 = temp
    return t0,t1
a,b = fibo_itr(bitsize)

print(a.bit_length())
print(b.bit_length())



##시간측정 시작
#euclide-itr
start = time.time()
for i in range(times):
    Euclidean.itr_euclidean(a, b)
end =time.time()
print("euclidean-ite {}-bit fibo".format(bitsize))
print((end-start)/times)

#euclide-rec
start = time.time()
for i in range(times):
    Euclidean.rec_euclidean(a, b)
end =time.time()
print("euclidean-rec {}-bit fibo".format(bitsize))
print((end-start)/times)

print( )

#binary-itr
start = time.time()
for i in range(0,times):
    binary.itr_binary(a, b)
end =time.time()
print("binary-itr {}-bit fibo".format(bitsize))
print((end-start)/times)

#binary-rec
start = time.time()
for i in range(times):
    binary.rec_binary(a, b)
end =time.time()
print("euclidean-rec {}-bit".format(bitsize))
print((end-start)/times)

print()
#binary-itr-bit operation
start = time.time()
for i in range(times):
    binary.itr_binary_bitop(a, b)
end =time.time()
print("binary-itr bit opertion {}-bit fibo".format(bitsize))
print((end-start)/times)

#binary-rec
start = time.time()
for i in range(times):
    binary.rec_binary_bitop(a, b)
end =time.time()
print("euclidean-rec bit operation {}-bit fibo".format(bitsize))
print((end-start)/times)
