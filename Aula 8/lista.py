#-- coding: latin-1 --
class Except(Exception):
    """Tratamento de exceção."""
    pass

class FilaVL:
    """Classe Fila: implementacao utilizando lista/vetor linear estático."""
    def __init__ (self,N):      # Cria nova fila como lista de tamanho fixo N.
        self._N=N               # Tamanho máximo da fila.
        self._data=N*[None]     # Lista sem objetos de tamanho M.
        self._size=0            # Tamanho inicial da fila.
    
    def push(self,e):
        """Lança exceção se a fila estiver cheia.
        Senão, adiciona elemento no fim da fila e aumenta o tamanho da fila."""
        if self.is_full():
            raise Except("Fila cheia!")
        else:
            self._data[self._size]=e # Novo item adicionado no topo.
            self._size+=1
    
    def pop(self):
        """Lanca excecao se a fila estiver vazia.
        Senão, remove e retorna o elemento no inicio da fila; desloca todos
        os elementos uma posição para frente; decrementa o tamanho da fila."""
        if self.is_empty( ):
            raise Except('Fila vazia!')
        else:
            front=self._data[0] # Primeiro da fila.
            for k in range(self._size-1):
                self._data[k]=self._data[k+1]
                self._size-=1
            return front
    
    def is_empty(self):
        """Retorna verdadeiro/falso se a fila estiver vazia/não vazia."""
        return self._size==0
    
    def is_full(self):
        """ Retorna verdadeiro/falso se a fila estiver cheia/não cheia."""
        return self._size==self._N
    
    def get_size(self):
        """Retorna o tamanho na fila."""
        return self._size
    
    def peek(self):
        """Se a fila estiver vazia, retorna None.
        Senão, retorna elemento no início da fila sem remove-lo."""
        if self.is_empty( ):
            return None
        else:
            return self._data[0] # primeiro item da lista.
    
    def top(self):
        """Retorna None se fila vazia.
        Senão, retorna elemento no fim da fila sem remove-lo."""
        if self.is_empty( ):
            return None
        else:
            return self._data[self._size-1] # Ultimo item da lista.
    
    def __str__(self):
        """Se a fila estiver vazia, retorna 'Fila vazia!'.
        Senão, retorna a string da fila.
        (Nota. Pode-se usar str(lista[:tamanho]) para retornar apenas parte
        da lista que contém a fila.)"""
        if self.is_empty( ):
            return 'Fila vazia!'
        else:
            return str(self._data[:self._size])
    
    def get_VL(self):
        """Se o vetor estiver vazio, retorna "Vetor vazio!".
        Senão, retorna a string completa do vetor linear.
        (Nota: usar str(lista)."""
        if self.is_empty( ):
            return "Vetor vazio."
        else:
            return str(self._data)