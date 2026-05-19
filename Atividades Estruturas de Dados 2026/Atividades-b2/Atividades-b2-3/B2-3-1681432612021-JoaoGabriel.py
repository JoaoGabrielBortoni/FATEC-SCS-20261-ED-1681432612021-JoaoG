'''
*----------------------------------------------------------------------------------*
*                           FATEC São Caetano do Sul                               *
*                                Atividade B2 - 3                                  *
*  Autor: 1681432612021 - João Gabriel Bortoni                                     *
*  Objetivo: Arvore Binaria                                                        *
*  Data: 12/05/2026                                                                *
*----------------------------------------------------------------------------------*
'''


class No:
        def __init__(self, valor):
                self.valor = valor 
                self.esq = None  
                self.dir = None  

class ArvoreBST: 
        def __init__(self, raiz=None): 
                self.raiz = raiz  
        
        def analisar_arvore(self):
                if not self.raiz:
                        print("A árvore é uma BST válida.") 
                        return
                pilha = [] 
                atual = self.raiz 
                anterior = None  
                while pilha or atual:
                        while atual: 
                                pilha.append(atual)
                                atual = atual.esq
                        atual = pilha.pop()
                        if anterior and atual.valor <= anterior.valor:
                                print("A árvore não é uma BST válida.") 
                                return
                        anterior = atual
                        atual = atual.dir 
                print("A árvore é uma BST válida.")
                
        def imprimir_nos_internos(self):
                if not self.raiz:
                        print() 
                        return 
                pilha = []  
                atual = self.raiz  
                while pilha or atual:
                        while atual: 
                                pilha.append(atual) 
                                atual = atual.esq 
                        atual = pilha.pop()  
                        if atual.esq or atual.dir:
                                print(atual.valor, end=' ') 
                        atual = atual.dir  
                print()          
        
        def imprimir_folhas(self):  
                if not self.raiz: 
                        print() 
                        return 
                pilha = [] 
                atual = self.raiz  
                while pilha or atual:  
                        while atual:  
                                pilha.append(atual) 
                                atual = atual.esq 
                        atual = pilha.pop() 
                        if not atual.esq and not atual.dir: 
                                print(atual.valor, end=' ') 
                        atual = atual.dir  #
                print()  

        def imprimir_niveis(self):  
                if not self.raiz:  
                        return  
                fila = [self.raiz]
                while fila:
                        tamanho_nivel = len(fila) 
                        for _ in range(tamanho_nivel):
                                nodo = fila.pop(0) 
                                print(nodo.valor, end=' ')  
                                if nodo.esq:  
                                        fila.append(nodo.esq)  
                                if nodo.dir:  
                                        fila.append(nodo.dir)
                        print() 

        def calcular_altura(self, no):  
                if not no: 
                        return -1 
                return 1 + max(self.calcular_altura(no.esq), self.calcular_altura(no.dir)) 

        def calcular_profundidade(self, valor):  
                if not self.raiz:
                        return -1 
                atual = self.raiz  
                profundidade = 0  
                while atual: 
                        if valor < atual.valor: 
                                atual = atual.esq 
                                profundidade += 1  
                        elif valor > atual.valor:  
                                atual = atual.dir  
                                profundidade += 1  
                        else:  
                                return profundidade  
                return -1  

        def imprimir_ancestrais(self, valor): 
                if not self.raiz:
                        return  
                ancestrais = []  
                atual = self.raiz  
                while atual: 
                        if valor < atual.valor: 
                                ancestrais.append(atual.valor)  
                                atual = atual.esq 
                        elif valor > atual.valor: 
                                ancestrais.append(atual.valor) 
                                atual = atual.dir  
                        else:  
                                for ancestral in ancestrais:  
                                        print(ancestral, end=' ') 
                                print() 
                                return  
                return  
        
        def imprimir_descendentes(self, valor): 
                atual = self.raiz  
                while atual:  
                        if valor < atual.valor: 
                                atual = atual.esq 
                        elif valor > atual.valor: 
                                atual = atual.dir 
                        else:
                                pilha = []  
                                nodo = atual.esq  
                                while pilha or nodo:
                                        while nodo: 
                                                pilha.append(nodo)  
                                                nodo = nodo.esq
                                        nodo = pilha.pop()  
                                        print(nodo.valor, end=' ') 
                                        nodo = nodo.dir  
                                pilha = []  
                                nodo = atual.dir 
                                while pilha or nodo:  
                                        while nodo: 
                                                pilha.append(nodo) 
                                                nodo = nodo.esq 
                                        nodo = pilha.pop() 
                                        print(nodo.valor, end=' ')  
                                        nodo = nodo.dir  
                                print()
                                return 
                return  