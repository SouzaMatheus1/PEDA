def somatorio(lim):
    if lim == 1:
        return 1
    else:
        return somatorio(lim - 1) + lim