#93866 Joao António Pinheiro Lopes

def eh_tabuleiro(arg):
    if isinstance(arg, tuple) and len(arg) == 3:
        if (isinstance(arg[0], tuple) and isinstance(arg[1], tuple) and 
           isinstance(arg[2], tuple) and len(arg[0]) == 3 and len(arg[1]) == 3
           and len(arg[2]) == 2):
            for indice in range(len(arg)):
                for elemento in arg[indice]:
                    if not (-1 <= elemento <= 1):
                        return False
            return True
    return False

def tabuleiro_str(t):
    if eh_tabuleiro(t):
        novo_interno = ()
        novo_t = ()
        for indice in range(len(t)):
            for elemento in t[indice]:
                if elemento == -1:
                    novo_interno = novo_interno + ('x', )
                else:
                    novo_interno = novo_interno + (elemento, )
            novo_t = novo_t + (novo_interno, )
            novo_interno = ()
        return '+-------+\n|...' + str(novo_t[0][2]) + '...|\n|..' + str(novo_t[0][1]) +\
               '.' + str(novo_t[1][2]) + '..|\n|.' + str(novo_t[0][0]) + '.' + str(novo_t[1][1]) +\
               '.' + str(novo_t[2][1]) + '.|\n|..' + str(novo_t[1][0]) + '.' + str(novo_t[2][0]) +\
               '..|\n+-------+'
    else:
        raise ValueError('tabuleiro_str: argumento invalido')
    
def tabuleiros_iguais(t1, t2):
    if eh_tabuleiro(t1) == eh_tabuleiro(t2):
        for indice_1 in range(len(t1)):
            for indice_2 in range(len(t1[indice_1])):
                if t1[indice_1][indice_2] != t2[indice_1][indice_2]:
                    return False
        return True
    else:
        raise ValueError('tabuleiros_iguais: um dos argumentos nao e tabuleiro')
    
def porta_x(t, c):
    if eh_tabuleiro(t) and (c == 'E' or c == 'D'):
        if c == 'E':
            if t[1][0] == -1:
                raise ValueError('porta_x: um dos argumentos e invalido')
            else:
                novo_valor = t[1][0] ^ 1
            novo_tabuleiro = t[:1] + ((novo_valor, ) + t[1][1:], ) + (t[2], )
        else:
            if t[2][0] == -1:
                raise ValueError('porta_x: um dos argumentos e invalido')
            else:
                novo_valor = t[2][0] ^ 1
            novo_tabuleiro = t[:2] + ((novo_valor, t[2][1]), )
        return propaga(novo_tabuleiro, 'x', c)
    else:
        raise ValueError('porta_x: um dos argumentos e invalido')

def porta_z(t, c):
    if eh_tabuleiro(t) and (c == 'E' or c == 'D'):
        if c == 'E':
            if t[0][0] == -1:
                raise ValueError('porta_z: um dos argumentos e invalido')
            else:
                novo_valor = t[0][0] ^ 1
            novo_tabuleiro = ((novo_valor, ) + t[0][1:], ) + t[1:]
        else:
            if t[2][1] == -1:
                raise ValueError('porta_z: um dos argumentos e invalido')
            else:
                novo_valor = t[2][1] ^ 1
            novo_tabuleiro = t[:2] + ((t[2][0], novo_valor), )
        return propaga(novo_tabuleiro, 'z', c)
    else:
        raise ValueError('porta_z: um dos argumentos e invalido')

def porta_h(t, c):
    if eh_tabuleiro(t) and (c == 'E' or c == 'D'):
        if c == 'E':
            novo_tabuleiro = ((t[1][0], ) + t[0][1:], ) + ((t[0][0], ) + t[1][1:], ) + (t[2], )
        else:
            novo_tabuleiro = t[:2] + ((t[2][1], t[2][0]), )
        return propaga(novo_tabuleiro, 'h', c)
    else:
        raise ValueError('porta_h: um dos argumentos e invalido')
                    
def propaga(t, porta, c):
    
    def porta_x(t, c):
        novo_valor_1 = t[1][1]
        if t[1][1] == 0:
            novo_valor_1 = 1
        elif t[1][1] == 1:
            novo_valor_1 = 0
        if c == 'E':
            novo_valor_2 = t[1][2]
            if t[1][2] == 0:
                novo_valor_2 = 1
            elif t[1][2] == 1:
                novo_valor_2 = 0
            novo_tabuleiro = t[:1] + ((t[1][0], novo_valor_1, novo_valor_2), ) + (t[2], )
        else:
            novo_valor_2 = t[0][1]
            if t[0][1] == 1:
                novo_valor_2 = 0
            elif t[0][1] == 0:
                novo_valor_2 = 1
            novo_tabuleiro = ((t[0][0], novo_valor_2, t[0][2]), ) + ((t[1][0], novo_valor_1, t[1][2]), ) + (t[2], )
        return novo_tabuleiro
    
    def porta_z(t, c):
        novo_valor_2 = t[0][2]
        if t[0][2] == 0:
            novo_valor_2 = 1
        elif t[0][2] == 1:
            novo_valor_2 = 0
        if c == 'E':
            novo_valor_1 = t[0][1]
            if t[0][1] == 0:
                novo_valor_1 = 1
            elif t[0][1] == 1:
                novo_valor_1 = 0
            novo_tabuleiro = ((t[0][0], novo_valor_1, novo_valor_2), ) + t[1:]
        else:
            novo_valor_1 = t[1][2]
            if t[1][2] == 1:
                novo_valor_1 = 0
            elif t[1][2] == 0:
                novo_valor_1 = 1
            novo_tabuleiro = (t[0][:2] + (novo_valor_2, ), ) + (t[1][:2] + (novo_valor_2, ), ) + (t[2], )
        return novo_tabuleiro        
    
    def porta_h(t, c):
        if c == 'E':
            novo_tabuleiro = ((t[0][0], t[1][1], t[1][2]), ) + ((t[1][0], t[0][1], t[0][2]), ) + (t[2], )
        else:
            novo_tabuleiro = ((t[0][0], t[0][2], t[0][1]), ) + ((t[1][0], t[1][2], t[1][1]), ) + (t[2], )
        return novo_tabuleiro    
    
    if porta == 'x':
        return porta_x(t, c)
    elif porta == 'z':
        return porta_z(t, c)
    else:
        return porta_h(t, c)
    
