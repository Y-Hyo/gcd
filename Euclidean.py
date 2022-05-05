
def rec_euclidean(a,b):
    if b==0:
        return a
    return rec_euclidean(b, a%b)

def itr_euclidean(a,b):
    while b!=0:
        a,b = b,a%b
    return a

