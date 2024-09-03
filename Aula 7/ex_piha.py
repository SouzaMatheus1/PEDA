class Empty(Exception):
    def __init__(self, err = 'Erro: Pilha vazia.'):
        self.erro = err
        super().__init__(self.erro)

class Pilha:
    def __init__ (self):
        """Cria nova pilha."""
        self._data = [ ] # Lista nao publica.

    def __str__ (self):
        """Retorna o string da pilha como o da lista."""
        return str(self._data)
    
    def __len__ (self):
        """Retorna numero de elementos na pilha (função len())."""
        return len(self._data)

    def is_empty(self):
        """Retorna verdadeiro se a pilha estiver vazia (len==0)."""
        # return str(True if self.len() == 0 else False)
        return len(self._data) == 0
    
    def push(self, e):
        """Adiciona elemento no topo da pilha.
        Usa método append() da lista: <lista>.append(e). """
        self._data.append(e)

    def pop(self):
        """Remove e retorna o elemento no topo da pilha.Lanca excecao se a pilha estiver vazia."""
        if self.is_empty():
            raise Empty()
        
        # el = self._data[-1]
        # self._data.pop(-1)
        # return el

        return self._data.pop()

    def top(self):
        """
        Retorna elemento no topo da pilha sem remove-lo (<lista>[-1]).
        Lanca excecao se a pilha estiver vazia.
        """
        if self.is_empty():
            raise Empty()
        
        return self._data[-1]


# TESTE
p=Pilha()
p.push(1)
p.push(3)
p.push(6)
p.push(7)
print(p)
p.pop(); p.pop()
print(p)

for k in range(len(p)):
    print(p.pop(),end=" ")