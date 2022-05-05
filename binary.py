

def rec_binary(a,b):
    if a==b:
        return a
    if  ((a&1)==0)and((b&1)==0):
        return (rec_binary(a>>1, b>>1)<<1)
    elif ((a&1)==0):
        return rec_binary(a>>1, b)
    elif ((b&1)==0):
        return rec_binary(a, b>>1)
    elif (a>=b):
        return rec_binary(a-b, b)
    elif (a<b):
        return rec_binary(a, b-a)

def itr_binary(a,b):
    t1,t2,t3 = a,b,1
    while (((t1&1)==0)and((t2&1)==0)):
        t1,t2,t3 = t1>>1 , t2>>1, t3<<1
    while t1 != t2:
        while ((t1&1) == 0):
            t1 = t1 >> 1
        while ((t2&1) == 0):
            t2 = t2 >> 1
        if t2>t1:
            t2 = t2-t1
        elif t2 < t1:
            t1 = t1-t2
    return t1*t3

def rec_binary_bitop(a,b):
    if a==b:
        return a
    if  (not(a&1))&(not(b&1)):
        return (rec_binary(a>>1, b>>1)<<1)
    elif (not(a&1)):
        return rec_binary(a>>1, b)
    elif (not(b&1)):
        return rec_binary(a, b>>1)
    elif (a>=b):
        return rec_binary(a-b, b)
    elif (a<b):
        return rec_binary(a, b-a)

def itr_binary_bitop(a,b):
    t1,t2,t3 = a,b,1
    while ((not(t1&1))&(not(t2&1))):
        t1,t2,t3 = t1>>1 , t2>>1, t3<<1
    while t1 != t2:
        while (not(t1&1)):
            t1 = t1 >> 1
        while (not(t2&1)):
            t2 = t2 >> 1
        if t2>t1:
            t2 = t2-t1
        elif t2 < t1:
            t1 = t1-t2
    return t1*t3

