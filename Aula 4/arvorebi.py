def bin_search(data, target, low, high):
    if low > high:
        return False
    
    ponto_medio = (low + high) // 2
    if target == data[ponto_medio]:
        return True
    elif target < data[ponto_medio]:
        # Pesquisa pelo lado esquerdo
        return bin_search(data, target, low, ponto_medio - 1)
    else:
        # Pesquisa pelo lado direito
        return bin_search(data, target, ponto_medio + 1, high)
    
