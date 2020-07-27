from math import factorial as F

def nck(n , k):
    """N Chose K function to get the number of K combinations of N elements given by the binomial.
    ARGS: n, k where n is the number of elements and k is the number of combinations we need to get from n
    """
    return int(F(n) / (F(k) * F(n-k)))
