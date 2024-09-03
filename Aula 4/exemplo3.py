def somatorio_cubo(lim):
    if lim == 0:
        return 0
    else:
        return somatorio_cubo(lim - 1) + (lim ** 3)
    
print(somatorio_cubo(3))