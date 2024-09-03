// CLASSE FILA COM VETOR CIRCULAR.
public class FilaVC {
    // Classe interna para tratar exceções específicas da Fila.
    public static class Except extends RuntimeException {
        // Construtor da exceção que aceita uma mensagem.
        public Except(String mensagem) {
            super(mensagem); // Chama o construtor da superclasse (RuntimeException).
        }
    }

    private int N; // Tamanho máximo da fila.
    private Object[] data; // Array para armazenar os elementos da fila.
    // Object é a superclasse geral do Java: um objeto de uma classe qualquer do
    // Java é sempre também um objeto da classe Object. Assim, quando um parâmetro é
    // definido como sendo da classe Object (como no método push()), qualquer
    // objeto pode ser passado, incluindo tipos primitivos. Neste último caso,
    // o tipo primitivo é convertido automaticamente para um objeto da classe
    // Wrapper correspondente (processo de autoboxing, como se fosse um "cast" do C).
    // Como exemplo, um int é convertido para Integer, um float para Float, um char
    // para Character, e assim por diante: as mesmas operações se aplicam.
    // Assim, qualquer tipo de elemento pode ser adicionado à fila, pois todos os
    // tipos serão tratados como Object, incluindo tipos primitivos.
    private int front; // Índice da frente da fila.
    private int top; // Índice do topo da fila (último elemento).
    private int ptr; // Posição atual do ponteiro (para navegação na fila).
    private int size; // Tamanho atual da fila.
    // Construtor da fila, inicializa a fila com o tamanho máximo N.
    
    public FilaVC(int N) {
        this.N = N; // Define o tamanho máximo da fila.
        this.data = new Object[N]; // Cria o array para armazenar os elementos.
        this.front = 0; // Inicializa o índice da frente da fila.
        this.top = -1; // Inicializa o índice do topo da fila.
        this.ptr = 0; // Inicializa o ponteiro de navegação.
        this.size = 0; // Inicializa o tamanho atual da fila.
    }

    // Método para adicionar um elemento à fila.
    public void push(Object e) {
        // Verifica se a fila está cheia.
        if (isFull()) {
            throw new Except("Fila cheia!"); // Lança exceção se a fila estiver cheia.
        } else {
            
        }
    }

    // Método para retornar e remover um elemento da fila.
    public Object pop() {
        // FilaVC e_front;

        if(this.isEmpty()){
            throw new Except("Fila vazia!");
        }else{
            // e_front = (FilaVC) this.data[this.front];
            Object e_front = data[front];
            // this.data[this.front] = null;
            data[front] = null;
            // this.size -= 1;
            size --;
            // this.front += 1;
            front ++;
            // if(this.front == this.N){
            //     this.front = 0;
            // }
    
            if(front == N){
                front = 0;
            }
    
            return e_front;
        }
    }

    // Método para verificar se a fila está vazia.
    public boolean isEmpty() {
        return this.size == 0;
    }

    // Método para verificar se a fila está cheia.
    public boolean isFull() {
        return this.size == this.N;
    }

    // Método para obter o tamanho atual da fila.
    public int getSize() {
        return this.size;
    }

    // Método para retornar o elemento da frente da fila sem removê-lo.
    public Object peek() {
        // Verifica se a fila está vazia.
        if (isEmpty()) {
            return null; // Retorna null se a fila estiver vazia.
        } else {
            return data[front]; // Retorna o elemento da frente da fila.
        }
    }

    // Método para obter o último elemento da fila sem removê-lo.
    public Object top() {
        if(isEmpty()){
            return null;
        }else{
            return this.data[this.top];
        }
    }

    // Método para converter a fila em uma string (para exibição).
    @Override
    public String toString() {
        // Verifica se a fila está vazia.
        if (isEmpty()) {
            return "Fila vazia!"; // Retorna uma mensagem se a fila estiver vazia.
        } else {
            String listaTemp = ""; // Inicializa uma string para acumular os elementos.
            int strSize = 0; // Tamanho atual da string.
            rewind(); // Reinicia o ponteiro de navegação.
            // Percorre todos os elementos da fila.
            while (strSize < size) {
                listaTemp += next() + " "; // Adiciona cada elemento à string.
                strSize++; // Incrementa o tamanho da string.
            }
            return listaTemp.trim(); // Retorna a string representando a fila.
        } // O método trim() retira espaços antes e depois da string.
    }

    // Método para retornar o conteúdo completo do vetor circular.
    public String getVC() {
        if(isEmpty()){
            throw new Except("vetor vazia!");
        }else{
            // return toString(this.data);
            return java.util.Arrays.toString(data);
        }
    }

    // Método para reiniciar o ponteiro de navegação na fila.
    public void rewind() {
        this.ptr = this.front;
    }

    // Método para avançar para o próximo elemento na fila.
    public Object next() {
        if(isEmpty()){
            return null;
        }else{
            Object e = this.data[this.ptr];
            this.ptr += 1;
            
            if(this.ptr == this.N){
                this.ptr = 0;
            }
    
            return e;
        }

    }
}
// CLASSE CLIENTE.
public class cliFilaVC {
// Método principal para testar a fila circular.
public static void main(String[] args) {
FilaVC f = new FilaVC(6);
System.out.println("-------------------------------");
System.out.print("push: ");
for (int k = 0; k < 6; k++) {
System.out.print((k + 1) + " ");
f.push(k + 1);
}
System.out.println("\nfila: " + f);
System.out.println("size: " + f.getSize());
System.out.println("VC: " + f.getVC());
System.out.println("-------------------------------");
System.out.print("4 x pop: ");
for (int k = 0; k < 4; k++) {
System.out.print(f.pop() + " ");
}
System.out.println("\npush: ");
for (int k = 0; k < 2; k++) {
System.out.print((k + 7) + " ");
f.push(k + 7);
}
System.out.println("\nfila: " + f);
System.out.println("size: " + f.getSize());
System.out.println("VC: " + f.getVC());
System.out.println("-------------------------------");
System.out.print("push: ");
for (int k = 0; k < 2; k++) {
System.out.print((k + 10) + " ");
f.push(k + 10);
}
System.out.println("\nfila: " + f);
System.out.println("size: " + f.getSize());
System.out.println("VC: " + f.getVC());
System.out.println("-------------------------------");
System.out.print("3 x pop: ");
for (int k = 0; k < 3; k++) {
System.out.print(f.pop() + " ");
}
System.out.println("\nfila: " + f);
System.out.println("size: " + f.getSize());
System.out.println("VC: " + f.getVC());
System.out.println("-------------------------------");
System.out.print("push: ");
for (int k = 0; k < 3; k++) {
System.out.print((k + 13) + " ");
f.push(k + 13);
}
System.out.println("\nfila: " + f);
System.out.println("size: " + f.getSize());
System.out.println("VC: " + f.getVC());
System.out.println("-------------------------------");
System.out.print("pop: ");
while (!f.isEmpty()) {
System.out.print(f.pop() + " ");
}
System.out.println("\nfila: " + f);
System.out.println("size: " + f.getSize());
System.out.println("VC: " + f.getVC());
System.out.println("-------------------------------");
String[] nome = {"Joao", "Maria", "Zeca", "Patricia"};
System.out.print(nome.length + "x push: ");
for (int k = 0; k < nome.length; k++) {
System.out.print(nome[k] + " ");
f.push(nome[k]);
}
System.out.println("\npeek: " + f.peek());
System.out.println("top : " + f.top());
System.out.println("fila: " + f);
System.out.println("size: " + f.getSize());
System.out.println("VC: " + f.getVC());
System.out.println("-------------------------------");
}
}