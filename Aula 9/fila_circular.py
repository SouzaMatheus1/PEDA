class Except(Exception):
    """Tratamento de exceção.
    Uso: raise Except(<mensagem>). Só!"""
    pass

class FilaVC:
    """Classe Fila: implementacao utilizando lista/vetor estático circular."""
    def __init__ (self,N): # Cria nova fila.
        """Cria nova fila como lista de tamanho fixo: vetor estático."""
        self._N=N # Tamanho máximo da fila.
        self._data=[None]*N # Cria "vetor" com objetos "null" de tamanho N.
        self._front=0 # Frente da fila (incrementa a cada pop()).
        self._top=-1 # Topo (fim) da fila (incrementa antes de inserir).
        self._ptr=0 # Posição atual do ponteiro (posição na fila).
        self._size=0 # Tamanho corrente da fila.

    def push(self,e):
        """Lança exceção (com mensagem) se a fila estiver cheia.
        Senão aumenta o tamanho da fila; avança o topo; se posição do
        topo igual a N, então posição do topo é feita zero (circula);
        define valor do novo topo (e)."""
        if self.is_full():
            raise Except("Fila cheia!")
        else:
            self._size+=1
            self._top+=1
        if self._top==self._N: # Passou o fim da fila?
            self._top=0 # Circula.
            self._data[self._top]=e # Item adicionado no topo/fim.

    def pop(self):
        """Lança exceção (com mensagem) se a fila estiver vazia.
        Senão, guarda o primeiro da fila; remove o primeiro da fila (=None);
        diminui o tamanho da fila; avança a posição da frente da fila (front);
        se a nova posição da frente for N, ela deve ser zerada (circular);
        retornar o elemento no início da fila (guardado)."""
        if self.is_empty( ):
            raise Except('Fila vazia!')
        else:
            e_front=self._data[self._front] # Primeiro da fila.
            self._data[self._front]=None # Limpa posição
            self._size-=1
            self._front+=1
        
        if self._front==self._N: # Passou o fim da fila?
            self._front=0 # Circula.
        return e_front

    def is_empty(self):
        """Retorna verdadeiro/falso se a fila estiver vazia/não vazia.
        (Nota. Tipo return <expressão lógica>)"""
        return self._size==0

    def is_full(self):
        """Retorna verdadeiro/falso se a fila estiver cheia/não cheia.
        (Nota. Tipo return <expressão lógica>)"""
        return self._size==self._N

    def get_size(self):
        """Retorna o tamanho na fila."""
        return self._size

    def peek(self):
        """Lança exceção (com mensagem) se a fila estiver vazia.
        Retorna elemento no início da fila sem removê-lo."""
        if self.is_empty( ):
            return None
        else:
            return self._data[self._front] # primeiro item da fila.

    def top(self):
        """Lança exceção (com mensagem) se a fila estiver vazia.
        Retorna elemento no início da fila sem removê-lo."""
        if self.is_empty( ):
            return None
        else:
            return self._data[self._top] # Ultimo item da fila.

    def __str__(self):
        """Se a fila estiver vazia, retorna "Fila vazia!".
        Senão, monta uma lista temporária usando rewind e next para
        navegar no vetor e adicionar cada um dos self._size elementos
        da fila nessa lista temporária (lista_temp.append());
        retorna str(lista_temp)."""
        if self.is_empty( ):
            return "Fila vazia!"
        else:
            lista_temp=[]
            strSize=0
            self.rewind()
        while strSize<self._size:
            lista_temp.append(self.next())
            strSize+=1
        return str(lista_temp)

    def getVC(self):
        """Se o vetor estiver vazio, retorna "Vetor vazio!"
        Senão retorna a string do vetor circular mostrando
        os elementos da fila circulando."""
        if self.is_empty( ):
            return "Vetor vazio.!"
    
