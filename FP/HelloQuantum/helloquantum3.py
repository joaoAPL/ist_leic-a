#Hello Quantum - objectos

#CELULA

class celula:
    
    #Construtor
    def __init__(self, valor):
        if isinstance(valor, int) and -1 <= valor <= 1:
            self._valor = valor
        
    #Selector
    def obter_valor(self):
        return self._valor
    
    #Reconhecedor
    def eh_celula(self):
        if isinstance(self._valor, int) and -1 <= self._valor <= 1:
            return True
        return False
    
    #Modificador
    def inverte_estado(self):
        if self._valor != -1:
            self._valor = self._valor ^ 1
        else:
            raise ValueError('inverte_estado: argumento errado')
        return self._valor
    
    #Teste
    def celula_iguais(self, other):
        if obter_valor(self) == obter_valor(other):
            return True
        return False
    
    #Transformador
    def celula_para_str(self):
        if obter_valor(self) == -1:
            return 'x'
        else:
            return str(obter_valor(self))
        
#COORDENADA

class coordenada:

    #Construtor
    def __init__(self, l, c):
        if isinstance(l, int) and isinstance(c, int) and (-1 <= l <= 1 
            and -1 <= c <= 1):
            self._l = l
            self._c = c
        
    #Selectores
    def coordenada_linha(self):
        return self._l
    
    def coordenada_coluna(self):
        return self._c
    
    #Reconhecedor
    def eh_coordenada(self):
        if isinstance(coordenada_linha(self), int) and isinstance(
            coordenada_coluna(self), int) and (-1 <= coordenada_linha(self) <= 1 
            and -1 <= coordenada_coluna(self) <= 1):
            return True
        return False
    
    #Teste
    def coordenadas_iguais(self, other):
        if coordenada_linha(self) == coordenada_linha(other) and (
            coordenada_coluna(self) == coordenada_coluna(other)):
            return True
        return False
    
    #Transformador
    def coordenada_para_str(self):
        return '(' + str(coordenada_linha(self)) + ' , ' + str(
            coordenada_coluna(self)) + ')'
    
class tabuleiro:
    
    #Construtores
    def __init__(self, tabuleiro):
        self._tabuleiro = []
        if isinstance(s, str):
            tabuleiro_t = eval(tabuleiro)
            if isinstance(tabuleiro_t, tuple) and len(tabuleiro_t) == 3 and (
                len(tabuleiro[0]) == len(tabuleiro[1]) == 3 
                and len(tabuleiro[2]) == 2):      
                for linha in range(len(tabuleiro)):
                    for coluna in range(len(tabuleiro[linha])):
                        if not (-1 <= tabuleiro[linha][coluna] <= 1):
                            return False
                for elemento in tabuleiro_t:
                    self._tabuleiro.append([list(elemento)])
            else:
                raise ValueError('tabuleiro: argumento invalido')
        
    def tabuleiro_inicial():
        return [[-1, -1, -1], [0, 0, -1], [0, -1]]

    #Selector
    def tabuleiro_dimensao(self):
        return len(self._tabuleiro)
    
    def tabuleiro_celula(self, coor):
        return celula(self._t[coordenada_linha(coor)][coordenada_coluna(coor)])
    
    #Modificadores
    def tabuleiro_substitui_celula(t, c, coor):
        tabuleiro_celula(
        
    
