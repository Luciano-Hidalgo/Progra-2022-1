def primo_decomp(n, i):
    if n == 1:
        return 1
    elif n % i == 0:
        print(i)
        return primo_decomp(n//i, i)
    else:
        return primo_decomp(n, i + 1)

def primo_decomp_final(n):
    return primo_decomp(n, 2)


def primo_decomp_iter(n):
    i = 2
    while i <= n:
        if n % i == 0:
            print(i)
            n = n // i
        else:
            i = i + 1
    return 1
    
        

primo_decomp_iter(120)
