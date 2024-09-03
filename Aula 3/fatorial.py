def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n-1)
    
print("n   n!     ")
for i in range(11):
    print("%2d %-12d"%(i, fatorial(i)))
print()