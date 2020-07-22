from math import factorial as F

def nck(n , k):
    return F(n) / (F(k) * F(n-k))
