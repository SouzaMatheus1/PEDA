def num_par(lim):
    if lim < 0:
        return 0
    if lim % 2 == 0:
        print(lim)
    num_par(lim - 1)
    
print(num_par(20))