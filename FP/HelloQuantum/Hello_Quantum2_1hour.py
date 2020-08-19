#Projecto Hello Quantum 2

#Tentativa de fazer o projecto - 1 hora

#CELULA

#Para representar o tipo abstracto Celula foi definido um dicionario com a chave
#'estado'

#Construtor
def cria_celula(v):
    if isinstance(v, int) and -1 <= v <= 1:
        return {'estado': v}
    else:
        raise ValueError('cria_celula: argumento errado')
    
#Selector
def obter_valor(c):
    return c['estado']

#Modificador
def inverte_estado(c):
    if c['estado'] != -1:
        c['estado'] = c['estado'] ^ 1
    return c

#Reconhecedor
def eh_celula(arg):
    if isinstance(arg, dict) and 'estado' in arg:
        if -1 <= obter_valor(arg) <= 1:
            return True
    return False
    
#Teste
def celulas_iguais(c1, c2):
    if obter_valor(c1) == obter_valor(c2):
        return True
    return False

#Transformador
def celula_para_str(c):
    if obter_valor(c) != -1:
        return str(obter_valor(c))
    else:
        return 'x'

#COORDENADA

#Para representar o tipo abstracto Coordenada foi definido um tuplo com dois
#valores sendo o primeiro correspondente a linha e o segundo correspondente a
#coluna

#Construtor
def cria_coordenada(l, c):
    if isinstance(l, int) and isinstance(c, int) and 0 <= l <= 2 and 0 <= c <= 2:
        return (l, c)
    else:
        raise ValueError('cria_coordenada: argumentos invalidos')
    
#Selectores
def coordenada_linha(c):
    return c[0]

def coordenada_coluna(c):
    return c[1]

#Reconhecedor
def eh_coordenada(arg):
    if isinstance(arg, tuple) and len(arg) == 2 and isinstance(arg[0], int) and isinstance(arg[1], int) and 0 <= arg[0] <= 2 and 0 <= arg[1] <= 2:
        return True
    return False

#Teste
def coordenadas_iguais(c1, c2):
    if coordenada_linha(c1) == coordenada_linha(c2) and coordenada_coluna(c1) == coordenada_coluna(c2):
        return True
    return False
        
#Transformador
def coordenada_para_str(c):
    return str((coordenada_linha(c), coordenada_coluna(c)))
    
#TABULEIRO

#Para representar o tipo abstracto Tabuleiro foi definido uma lista com três
#listas sendo que cada lista tem três elementos exceptuando a terceira lista que
#tem dois elementos

#Construtores
def tabuleiro_inicial():
    return [[-1, -1, -1], [0, 0, -1], [0, -1]]

def str_para_tabuleiro(s):
    if isinstance(s, str):
        arg = eval(s)
        if isinstance(arg, tuple) and len(arg) == 3 and (isinstance(arg[0], tuple)
           and isinstance(arg[1], tuple) and isinstance(arg[2], tuple)
           and (len(arg[0]) == len(arg[1]) == 3) and len(arg[2]) == 2):
            for linha in range(len(arg)):
                for coluna in range(len(arg[linha])):
                    if not isinstance(arg[linha][coluna], int) and arg[linha][coluna] not in range(-1, 2):
                        raise ValueError('str_para_tabuleiro: argumentos invalidos')
            return [list(arg[0]), list(arg[1]), list(arg[2])]
    raise ValueError('str_para_tabuleiro: argumentos invalidos')
    
#Selectores
def tabuleiro_dimensao(t):
    return len(t)

def tabuleiro_celula(t, coor):
    return cria_celula(t[coordenada_linha(coor)][coordenada_coluna(coor)])
    
#Modificadores
def tabuleiro_substitui_celula(t, c, coor):
    if isinstance(t, list) and len(t) == 3 and (isinstance(t[0], list)
       and isinstance(t[1], list) and isinstance(t[2], list)
       and (len(t[0]) == len(t[1]) == 3) and len(t[2]) == 2) and (eh_celula(c) 
       and eh_coordenada(coor)):
        t[coordenada_linha(coor)][coordenada_coluna(coor)] = obter_valor(c)
        return t
    else:
        raise ValueError('tabuleiro_substitui_celula: argumentos invalidos')
    
def tabuleiro_inverte_estado(t, coor):
    if isinstance(t, list) and len(t) == 3 and (isinstance(t[0], list)
       and isinstance(t[1], list) and isinstance(t[2], list) and (len(t[0]) == len(t[1]) == 3) and len(t[2]) == 2) and eh_coordenada(coor):
        t[coordenada_linha(coor)][coordenada_coluna(coor)] = obter_valor(inverte_estado(cria_celula(t[coordenada_linha(coor)][coordenada_coluna(coor)])))
        return t
    else:
        raise ValueError('tabuleiro_inverte_estado: argumentos invalidos')
    
#Reconhecedor
def eh_tabuleiro(arg):
    if isinstance(arg, list) and len(arg) == 3 and (isinstance(arg[0], list)
       and isinstance(arg[1], list) and isinstance(arg[2], list) and (len(arg[0]) == len(arg[1]) == 3) and len(arg[2]) == 2):
        return True
    return False

#Teste
def tabuleiros_iguais(t1, t2):
    for linha in range(tabuleiro_dimensao(t1)):
        for coluna in range(tabuleiro_dimensao(t1[linha])):
            coor = cria_coordenada(linha, coluna)
            celula_t1 = tabuleiro_celula(t1, coor)
            celula_t2 = tabuleiro_celula(t2, coor)
            if not celulas_iguais(celula_t1, celula_t2):
                return False
    return True

#Transformador
def tabuleiro_para_str(t):
    novo_interno = []
    novo_t = []
    for indice in range(len(t)):
        for elemento in t[indice]:
            celula = cria_celula(elemento)
            novo_interno = novo_interno + [celula_para_str(celula), ]
        novo_t = novo_t + [novo_interno, ]
        novo_interno = []       
    return '+-------+\n|...' + novo_t[0][2] + '...|\n|..' + novo_t[0][1] +\
            '.' + novo_t[1][2] + '..|\n|.' + novo_t[0][0] + '.' + novo_t[1][1] +\
            '.' + novo_t[2][1] + '.|\n|..' + novo_t[1][0] + '.' + novo_t[2][0] +\
            '..|\n+-------+'

#Funcoes de Alto Nivel
def porta_x(t, p):
    if eh_tabuleiro(t) and (p == 'E' or p == 'D'):
        if p == 'E':
            if obter_valor(tabuleiro_celula(t, cria_coordenada(1, 0))) == -1:
                raise ValueError('porta_x: argumentos invalidos')
            else:
                tabuleiro_inverte_estado(t, cria_coordenada(1, 0))
        else:
            if obter_valor(tabuleiro_celula(t, cria_coordenada(2, 0))) == -1:
                raise ValueError('porta_x: argumentos invalidos')
            else:
                tabuleiro_inverte_estado(t, cria_coordenada(2, 0))
        return propaga(t, 'x', p)
    else:
        raise ValueError('porta_x: argumentos invalidos')
    
def porta_z(t, p):
    if eh_tabuleiro(t) and (p == 'E' or p == 'D'):
        if p == 'E':
            if obter_valor(tabuleiro_celula(t, cria_coordenada(0, 0))) == -1:
                raise ValueError('porta_z: argumentos invalidos')
            else:
                tabuleiro_inverte_estado(t, cria_coordenada(0, 0))
        else:
            if obter_valor(tabuleiro_celula(t, cria_coordenada(2, 1))) == -1:
                raise ValueError('porta_z: argumentos invalidos')
            else:
                tabuleiro_inverte_estado(t, cria_coordenada(2, 1))
        return propaga(t, 'z', p)
    else:
        raise ValueError('porta_z: argumentos invalidos')
    
def porta_h(t, p):
    if eh_tabuleiro(t) and (p == 'E' or p == 'D'):
        if p == 'E':
            celula_aux = tabuleiro_celula(t, cria_coordenada(1, 0))
            tabuleiro_substitui_celula(t, tabuleiro_celula(t, cria_coordenada(0, 0)), cria_coordenada(1, 0))
            tabuleiro_substitui_celula(t, celula_aux, cria_coordenada(0, 0))
        else:
            celula_aux = tabuleiro_celula(t, cria_coordenada(2, 0))
            tabuleiro_substitui_celula(t, tabuleiro_celula(t, cria_coordenada(2, 1)), cria_coordenada(2, 0))
            tabuleiro_substitui_celula(t, celula_aux, cria_coordenada(2, 1))            
        return propaga(t, 'h', p)
    else:
        raise ValueError('porta_h: argumentos invalidos')

def propaga(t, porta, c):
    
    def porta_x(t, c):
        if tabuleiro_celula(t, cria_coordenada(1, 1)) != -1:
            tabuleiro_inverte_estado(t, cria_coordenada(1, 1))
        if c == 'E':
            if tabuleiro_celula(t, cria_coordenada(2, 1)) != -1:
                tabuleiro_inverte_estado(t, cria_coordenada(1, 2))
        else:
            if tabuleiro_celula(t, cria_coordenada(0, 0)) != -1:
                tabuleiro_inverte_estado(t, cria_coordenada(0, 1))            
        return t
    
    def porta_z(t, c):
        if tabuleiro_celula(t, cria_coordenada(0, 2)) != -1:
            tabuleiro_inverte_estado(t, cria_coordenada(0, 2))
        if c == 'E':
            if tabuleiro_celula(t, cria_coordenada(0, 1)) != -1:
                tabuleiro_inverte_estado(t, cria_coordenada(0, 1))
        else:
            if tabuleiro_celula(t, cria_coordenada(1, 2)) != -1:
                tabuleiro_inverte_estado(t, cria_coordenada(1, 2))
        return t
    
    def porta_h(t, c):
        if c == 'E':
            celula_aux = tabuleiro_celula(t, cria_coordenada(0, 1))
            tabuleiro_substitui_celula(t, tabuleiro_celula(t, cria_coordenada(1, 1)), cria_coordenada(0, 1))
            tabuleiro_substitui_celula(t, celula_aux, cria_coordenada(1, 1))
            celula_aux = tabuleiro_celula(t, cria_coordenada(0, 2))
            tabuleiro_substitui_celula(t, tabuleiro_celula(t, cria_coordenada(1, 2)), cria_coordenada(0, 2))
            tabuleiro_substitui_celula(t, celula_aux, cria_coordenada(1, 2))            
        else:
            celula_aux = tabuleiro_celula(t, cria_coordenada(1, 2))
            tabuleiro_substitui_celula(t, tabuleiro_celula(t, cria_coordenada(1, 1)), cria_coordenada(1, 2))
            tabuleiro_substitui_celula(t, celula_aux, cria_coordenada(1, 1))
            celula_aux = tabuleiro_celula(t, cria_coordenada(0, 2))
            tabuleiro_substitui_celula(t, tabuleiro_celula(t, cria_coordenada(0, 1)), cria_coordenada(0, 2))
            tabuleiro_substitui_celula(t, celula_aux, cria_coordenada(0, 1))                        
        return t
    
    if porta == 'x':
        return porta_x(t, c)
    elif porta == 'z':
        return porta_z(t, c)
    else:
        return porta_h(t, c)
            
#Funcoes Adicionais
def hello_quantum(s):
    tabuleiro_jogo = tabuleiro_inicial()
    tabuleiro_obj = str_para_tabuleiro((s[:len(s)-2]))
    numero_max_jog = eval(s[len(s)-1:])
    print('Bem-vindo ao Hello Quantum!\nO seu objetivo e chegar ao tabuleiro:\n' \
             + tabuleiro_para_str(tabuleiro_obj) + '\n Comecando com o tabuleiro que se segue:\n' \
             + tabuleiro_para_str(tabuleiro_inicial()))
    numero_jog = 0
    while numero_jog <= numero_max_jog:
        porta_def = input('Escolha uma porta para aplicar (X, Z ou H): ')
        qubit_def = input('Escolha um qubit para analisar (E ou D): ')
        tabuleiro_jogo = joga(tabuleiro_jogo, porta_def, qubit_def)
        print(tabuleiro_para_str(tabuleiro_jogo))
        numero_jog += 1
        if tabuleiros_iguais(tabuleiro_jogo, tabuleiro_obj):
            print('Parabens, conseguiu converter o tabuleiro em ' + str(numero_jog) + ' jogadas!')
            return True
    return False
    
def joga(t, p, q):
    if p == 'X':
        return porta_x(t, q)
    elif p == 'Z':
        return porta_z(t, q)
    else:
        return porta_h(t, q)
        