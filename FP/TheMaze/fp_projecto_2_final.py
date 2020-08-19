#93866 Joao Antonio Pinheiro Lopes

#Codigo redigido segundo o PEP257 e PEP8

#POSICAO

#Para representar o ADT POSICAO foi definido o tipo de dados embutido tuplo com
#dois argumentos sendo o primeiro referente a coordenada em x (horizontal) e o
#segundo referente a coordenada em y(vertical)

#Construtores
def cria_posicao(x, y):
    """Constroi uma posicao.
    
    Operacao basica: Construtor
    Assinatura da funcao: N x N -- posicao    
    Excepcao: Caso os argumentos nao sejam numeros naturais e gerado um erro de
    valor
    """
    if isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0:
        return (x, y)
    else:
        raise ValueError("cria_posicao: argumentos invalidos")
    
def cria_copia_posicao(p):
    """Constroi uma copia da posicao.
    
    Operacao basica: Construtor
    Assinatura da funcao: posicao -- posicao    
    """    
    return cria_posicao(p[0], p[1]) 

#Selectores
def obter_pos_x(p):
    """Devolve a componente x de posicao.
    
    Operacao basica: Selector
    Assinatura da funcao: posicao -- N    
    """    
    return p[0]

def obter_pos_y(p):
    """Devolve a componente y de posicao.
    
    Operacao basica: Selector
    Assinatura da funcao: posicao -- N    
    """    
    return p[1]

#Reconhecedor
def eh_posicao(arg):
    """Certifica se o argumento dado e de facto uma posicao.
    
    Operacao basica: Reconhecedor
    Assinatura da funcao: universal -- booleano
    """
    if isinstance(arg, tuple) and len(arg) == 2:
        if isinstance(arg[0], int) and isinstance(arg[1], int) and (
           arg[0] >= 0 and arg[1] >= 0):
            return True
        else:
            return False
    else:
        return False
            
#Teste
def posicoes_iguais(p1, p2):
    """Avalia se a posicao 1 e a posicao 2 sao posicoes iguais.
    
    Operacao basica: Teste
    Assinatura da funcao: posicao x posicao -- booleano
    """            
    if obter_pos_x(p1) == obter_pos_x(p2) and (
        obter_pos_y(p1) == obter_pos_y(p2)):
        return True
    else:
        return False
   
#Transformador 
def posicao_para_str(p):
    """Representa externamente uma posicao.
    
    Operacao basica: Transformador
    Assinatura da funcao: posicao -- str    
    """            
    return str(p)

#Funcoes de alto nivel
def obter_posicoes_adjacentes(p):
    """Retorna as posicoes adjacentes a posicao (de acordo com a ordem de
    leitura).
    
    Assinatura da funcao: posicao -- tuplo de posicoes    
    """     
    if obter_pos_x(p) == 0 and obter_pos_y(p) == 0:
        return (cria_posicao(obter_pos_x(p) + 1, obter_pos_y(p)), cria_posicao(
                obter_pos_x(p), obter_pos_y(p) + 1))
    elif obter_pos_x(p) == 0 and obter_pos_y(p) != 0:
        return (cria_posicao(obter_pos_x(p), obter_pos_y(p) - 1), cria_posicao(
                obter_pos_x(p) + 1, obter_pos_y(p)), cria_posicao(
                obter_pos_x(p), obter_pos_y(p) + 1))
    elif obter_pos_x(p) != 0 and obter_pos_y(p) == 0:
        return (cria_posicao(obter_pos_x(p) - 1, obter_pos_y(p)), cria_posicao(
               obter_pos_x(p) + 1, obter_pos_y(p)), cria_posicao(
               obter_pos_x(p), obter_pos_y(p) + 1))
    else:
        return (cria_posicao(obter_pos_x(p), obter_pos_y(p) - 1), cria_posicao(
                obter_pos_x(p) - 1, obter_pos_y(p)), cria_posicao(
                obter_pos_x(p) + 1, obter_pos_y(p)), cria_posicao(
                obter_pos_x(p), obter_pos_y(p) + 1))
        
#UNIDADE

#Para representar o ADT UNIDADE foi escolhido o tipo de dados embutido
#dicionario constituido pela chave posicao cujo valor e uma posicao do tipo
#POSICAO, pela chave vida cujo valor e um natural0, pela chave forca cujo valor
#e um natural0 e por ultimo pela chave exercito cujo valor e uma string nao
#vazia

#Construtores
def cria_unidade(p, v, f, string):
    """Constroi uma unidade.
    
    Operacao basica: Construtor
    Assinatura da funcao: posicao x N x N x str -- unidade
    Excepcao: Caso os argumentos nao sejam uma posicao, um natural, um natural e
    uma string respectivamente, e gerado um erro de valor
    """    
    if eh_posicao(p) and isinstance(v, int) and isinstance(f, int) and (v > 0
       and f > 0) and isinstance(string, str) and string != '':
        return {'posicao': p, 'vida': v, 'forca': f, 'exercito': string}
    else:
        raise ValueError("cria_unidade: argumentos invalidos")

def cria_copia_unidade(u):
    """Constroi uma copia da unidade.
    
    Operacao basica: Construtor
    Assinatura da funcao: unidade -- unidade
    """        
    return u.copy()

#Selectores
def obter_posicao(u):
    """Devolve a posicao da unidade.
    
    Operacao basica: Selector
    Assinatura da funcao: unidade -- posicao
    """        
    return u['posicao']

def obter_exercito(u):
    """Devolve o exercito da unidade.
    
    Operacao basica: Selector
    Assinatura da funcao: unidade -- str
    """            
    return u['exercito']

def obter_forca(u):
    """Devolve a forca da unidade.
    
    Operacao basica: Selector
    Assinatura da funcao: unidade -- N
    """            
    return u['forca']

def obter_vida(u):
    """Devolve a vida da unidade.
    
    Operacao basica: Selector
    Assinatura da funcao: unidade -- vida
    """            
    return u['vida']

#Modificadores
def muda_posicao(u, p):
    """Altera a posicao da unidade para uma nova posicao
    
    Operacao basica: Modificador
    Assinatura da funcao: unidade x posicao -- unidade
    """    
    u['posicao'] = p
    return u

def remove_vida(u, v):
    """Altera a vida da unidade reduzindo-a a quantidade v
    
    Operacao basica: Modificador
    Assinatura da funcao: unidade x N -- unidade
    """     
    u['vida'] = u['vida'] - v
    return u    
    
#Reconhecedor
def eh_unidade(arg):
    """Certifica se o argumento dado e de facto uma unidade.
    
    Operacao basica: Reconhecedor
    Assinatura da funcao: universal -- booleano
    """    
    chaves_unidade = ['posicao', 'vida', 'forca', 'exercito']
    if isinstance(arg, dict) and len(arg) == 4:
        for elemento in list(arg):
            if elemento not in chaves_unidade:
                return False
        if eh_posicao(arg['posicao']) and ((isinstance(arg['vida'], int) and
           isinstance(arg['forca'], int) and isinstance(arg['exercito'], str))
           and (arg['vida'] >= 0 and arg['forca'] >= 0 and
           arg['exercito'] != '')):
            return True
        else:
            return False
    else:
        return False
    
#Teste
def unidades_iguais(u1, u2):
    """Avalia se a unidade 1 e a unidade 2 sao as mesmas unidades.
    
    Operacao basica: Teste
    Assinatura da funcao: unidade x unidade -- booleano
    """                
    if obter_posicao(u1) == obter_posicao(u2) and (obter_vida(u1) ==
       obter_vida(u2)) and obter_forca(u1) == obter_forca(u2) and (
       obter_exercito(u1) == obter_exercito(u2)):
        return True
    else:
        return False
    
#Transformadores
def unidade_para_char(u):
    """Representa externamente a referencia ao exercito utilizado.
    
    Operacao basica: Transformador
    Assinatura da funcao: unidade -- str    
    """                
    return obter_exercito(u)[0].upper()

def unidade_para_str(u):
    """Representa externamente qual o exercito utilizado.
    
    Operacao basica: Transformador
    Assinatura da funcao: unidade -- str    
    """                
    return obter_exercito(u)[0].upper() + str([obter_vida(u), obter_forca(u)]) \
           + '@' + str(obter_posicao(u))

#Funcoes de alto nivel
def unidade_ataca(u1, u2):
    """Retira os pontos de forca da unidade 1 aos pontos de vida da unidade 2 e
    verifica se a unidade 2 foi destruida.
    
    Assinatura da funcao: unidade x unidade -- booleano    
    """    
    u2 = remove_vida(u2, obter_forca(u1))
    if obter_vida(u2) <= 0:
        return True
    else:

        return False
    
def ordenar_unidades(t):
    """Ordena as unidades dadas pela sua posicao no labirinto, de acordo com a 
    ordem de leitura do mesmo.
    
    Assinatura da funcao: tuplo unidades -- tuplo unidades
    """        
    l = list(t)
    #Foi utilizado o Bubble Sort do livro (pag 174)
    maior_indice = len(l) - 1
    nenhuma_troca = False
    while not nenhuma_troca:
        nenhuma_troca = True
        for indice in range(maior_indice):
            if obter_pos_y(obter_posicao(l[indice])) > obter_pos_y(
                obter_posicao(l[indice + 1])):
                l[indice], l[indice + 1] = l[indice + 1], l[indice]
                nenhuma_troca = False
            elif obter_pos_y(obter_posicao(l[indice])) == obter_pos_y(
                obter_posicao(l[indice + 1])):
                if obter_pos_x(obter_posicao(l[indice])) > obter_pos_x(
                    obter_posicao(l[indice + 1])):
                    l[indice], l[indice + 1] = l[indice + 1], l[indice]
                    nenhuma_troca = False                
        maior_indice = maior_indice - 1
    return tuple(l)

#MAPA

#Para representar o ADT MAPA foi definido o tipo de dados embutido tuplo
#constituido por quatro tuplos sendo o primeiro as dimensoes (Nx, Ny) do
#labirinto, o segundo contendo as posicoes das paredes interiores ao labirinto,
#o terceiro com as unidades de um exercito designado 1 e o quarto com as
#unidades de um exercito designado 2

#Funcoes Auxiliares
def eh_dimensao(arg):
    """Verifica se o argumento dado reune as condicoes para ser uma dimensao.
    
    Assinatura da funcao: universal -- booleano
    """       
    if isinstance(arg, tuple) and len(arg) == 2:
        if isinstance(arg[0], int) and isinstance(arg[1], int) and (arg[0] >= 3 
           and arg[1] >= 3):
            return True
        else:
            return False
    else:
        return False

def eh_conj_paredes_interiores(d, arg):
    """Verifica se dado um conjunto de posicoes relativas a paredes, este trata
    deum conjunto de paredes interiores ao labirinto.
    
    Assinatura da funcao: dimensao x universal -- booleano
    """    
    if isinstance(arg, tuple):
        for parede in arg:
            if not (eh_posicao(parede) and (0 < obter_pos_x(parede) < d[0] and
                    0 < obter_pos_y(parede) < d[1])):
                return False
        return True
    else:
        return False
    
def eh_conj_exercito(arg):
    """Verifica se o argumento corresponde a um conjunto de unidades de um
    exercito.
    
    Assinatura da funcao: universal -- booleano
    """    
    if isinstance(arg, tuple) and len(arg) >= 1:
        for unidade in arg:
            if not eh_unidade(unidade):
                return False
        return True
    else:
        return False

#Construtores
def cria_mapa(d, w, e1, e2):
    """Constroi um mapa.
    
    Operacao basica: Construtor
    Assinatura da funcao: tuplo x tuplo x tuplo x tuplo -- mapa
    Excepcao: Caso os argumentos nao sejam uma dimensao, um conjunto de paredes
    interiores, um conjunto de unidades de um exercito 1, e um conjunto de
    unidades de um exercito 2 respectivamente, e gerado um erro de valor
    
    Pode-se assumir que cada conjunto de unidades de um exercito e diferente
    sendo que cada conjunto de unidades contem apenas unidades desse exercito.
    As unidades presentes nos conjuntos de unidades ocupam posicoes distintas e
    livres no labirinto.
    """        
    if eh_dimensao(d) and eh_conj_paredes_interiores(d, w) and (
        eh_conj_exercito(e1) and eh_conj_exercito(e2)):
        return (d, w, e1, e2)
    else:
        raise ValueError("cria_mapa: argumentos invalidos")    

def cria_copia_mapa(m):
    """Constroi uma copia do mapa passado como argumento.
    
    Operacao basica: Construtor
    Assinatura da funcao: mapa -- mapa
    """        
    return cria_mapa(m[0], m[1], m[2], m[3])

#Selectores
def obter_tamanho(m):
    """Devolve o tamanho do labirinto.
    
    Operacao basica: Selector
    Assinatura da funcao: mapa -- tuplo
    """     
    return m[0]

def obter_nome_exercitos(m):
    """Devolve os nomes ordenados dos exercitos em combate.
    
    Operacao basica: Selector
    Assinatura da funcao: mapa -- tuplo
    """     
    exercito_e1 = obter_exercito(m[2][0])
    exercito_e2 = obter_exercito(m[3][0])
    if unidade_para_char(m[2][0]) < unidade_para_char(m[3][0]):
        return (exercito_e1, exercito_e2)
    else:
        return (exercito_e2, exercito_e1)

def obter_unidades_exercito(m, e):
    """Devolve as unidades de um dado exercito.
    
    Operacao basica: Selector
    Assinatura da funcao: mapa x str -- tuplo unidades
    """     
    for unidade in m[2]:
        if obter_exercito(unidade) == e:
            return ordenar_unidades(m[2])
        else:
            return ordenar_unidades(m[3])
    
def obter_todas_unidades(m):
    """Devolve todas as unidades presentes no labirinto.
    
    Operacao basica: Selector
    Assinatura da funcao: mapa -- tuplo
    """     
    total_unidades = obter_unidades_exercito(m,  obter_nome_exercitos(m)[0]) + \
                     obter_unidades_exercito(m, obter_nome_exercitos(m)[1])
    return ordenar_unidades(total_unidades)

def obter_unidade(m, p):
    """Devolve a unidade do mapa que se encontra na posicao p.
    
    Operacao basica: Selector
    Assinatura da funcao: mapa x posicao -- unidade
    """         
    total_unidades = obter_todas_unidades(m)
    for unidade in total_unidades:
        if obter_posicao(unidade) == p:
            return unidade
        
#Modificadores
def eliminar_unidade(m, u):
    """Remove a unidade do mapa deixando a sua posicao no labirinto livre.
    
    Operacao basica: Modificador
    Assinatura da funcao: mapa x unidade -- mapa
    """        
    if obter_exercito(u) == obter_exercito(m[2][0]):
        for indice in range(len(m[2])):
            if m[2][indice] == u:
                e1 = m[2][:indice] + m[2][indice+1:]
        m_f = cria_mapa(m[0], m[1], e1, m[3])
        m = cria_copia_mapa(m_f)
        return m
    else:
        for indice in range(len(m[3])):
            if m[3][indice] == u:
                e2 = m[3][:indice] + m[3][indice+1:]
        m_f = cria_mapa(m[0], m[1], m[2], e2)
        m = cria_copia_mapa(m_f)
        return m
    
def mover_unidade(m, u, p):
    """Altera a posicao da unidade dada no labirinto para a nova posicao,
    actualizando o mapa que continha a unidade anterior com a nova unidade.
    
    Operacao basica: Modificador
    Assinatura da funcao: mapa x unidade x posicao -- mapa
    """            
    for indice in range(len(m)):
        if indice == 2 or indice == 3:
            for unidade in m[indice]:
                if unidade == u:
                    muda_posicao(unidade, p)
                    muda_posicao(u, p)
    return m
    
#Reconhecedores
def eh_posicao_unidade(m, p):
    """Certifica se a posicao dada corresponde a uma posicao ocupada por uma
    unidade no labirinto.
    
    Operacao basica: Reconhecedor
    Assinatura da funcao: mapa x posicao -- booleano
    """        
    for unidade in obter_todas_unidades(m):
        if posicoes_iguais(obter_posicao(unidade), p):
            return True
    return False
    
def eh_posicao_corredor(m, p):
    """Certifica se a posicao dada corresponde a corredor no labirinto. Um
    corredor e uma posicao interior ao labirinto que nao e uma parede.
    
    Operacao basica: Reconhecedor
    Assinatura da funcao: mapa x posicao -- booleano
    """            
    if p not in m[1] and (0 < obter_pos_x(p) < obter_pos_x(obter_tamanho(m)) and
       (0 < obter_pos_y(p) < obter_pos_y(obter_tamanho(m)))):
        return True
    else:
        return False
    
def eh_posicao_parede(m, p):
    """Certifica se a posicao dada corresponde a uma parede do labirinto. 
    
    Operacao basica: Reconhecedor
    Assinatura da funcao: mapa x posicao -- booleano
    """            
    if p in m[1] or not (0 < obter_pos_x(p) < d[0] and 0 < obter_pos_y(p) < 
                         d[1]):
        return True
    else:
        return False

#Teste
def mapas_iguais(m1, m2):
    """Avalia se o mapa 1 e o mapa 2 sao iguais
    
    Operacao basica: Teste
    Assinatura da funcao: mapa x mapa -- booleano
    """       
    if obter_tamanho(m1) == obter_tamanho(m2) and m1[1] == m2[1] and (
       obter_todas_unidades(m1) == obter_todas_unidades(m2)):
        return True
    else:
        return False
    
#Transformador
def mapa_para_str(m):
    """Representa externamente o labirinto.
    
    Operacao basica: Transformador
    Assinatura da funcao: mapa -- str    
    """     
    w = m[1]    
    e1 = obter_unidades_exercito(m, obter_nome_exercitos(m)[0])
    e2 = obter_unidades_exercito(m, obter_nome_exercitos(m)[1])
    posicoes_e1 = ()
    posicoes_e2 = ()
    for unidade in e1:
        posicoes_e1 = posicoes_e1 + (obter_posicao(unidade), )
    for unidade in e2:
        posicoes_e2 = posicoes_e2 + (obter_posicao(unidade), )    
    linha = ()
    coluna = ()
    for y in range(obter_pos_y(obter_tamanho(m))):
        for x in range(obter_pos_x(obter_tamanho(m))):
            if (x == 0 or x == obter_pos_x(obter_tamanho(m)) - 1) or (y == 0 or 
               y == obter_pos_y(obter_tamanho(m)) - 1) or ((x, y) in w):
                valor = '#'
            elif (x, y) in posicoes_e1:
                valor = unidade_para_char(e1[0])
            elif (x, y) in posicoes_e2:
                valor = unidade_para_char(e2[0])
            else:
                valor = '.'
            linha = linha + tuple(valor)
        coluna = coluna + (tuple(linha), )
        linha = ()
    labirinto = coluna
    labirinto_externo = ''
    for y in range(len(labirinto)):
        for x in range(len(labirinto[y])):
            labirinto_externo = labirinto_externo + labirinto[y][x]
        if y != (len(labirinto) - 1):
            labirinto_externo = labirinto_externo + '\n'
    return labirinto_externo

#Funcoes de alto nivel
def obter_inimigos_adjacentes(m, u):
    """Obtem as posicoes inimigas adjacentes a posicao fornecida pela ordem
    de leitura do labirinto.
    
    Assinatura da funcao: mapa x unidade -- tuplo unidades
    """            
    todas_unidades = obter_todas_unidades(m)
    unidades_adjacentes = []
    for unidade in todas_unidades:
        if obter_exercito(unidade) != obter_exercito(u) and (obter_posicao(
           unidade) in obter_posicoes_adjacentes(obter_posicao(u))):
            unidades_adjacentes = unidades_adjacentes + [unidade]
    return tuple(unidades_adjacentes)

def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    Assinatura da funcao: mapa x unidade -- posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)

#FUNCOES ADICIONAIS

def calcula_pontos(m, string):
    """Calcula os pontos de vida de todos os exercitos em combate calculando a
    soma dos pontos de vida de cada unidade de um dado exercito..
    
    Assinatura da funcao: mapa x str -- int
    """        
    todas_unidades = obter_todas_unidades(m)
    total_vida_e = 0
    for unidade in todas_unidades:
        if obter_exercito(unidade) == string:
            total_vida_e = total_vida_e + obter_vida(unidade)
    return total_vida_e

#def simula_turno(m):
    #todas_unidades = obter_todas_unidades(m)
    ##Realizar movimento
    #for unidade in todas_unidades:
        #posicoes_adjacentes = obter_posicoes_adjacentes(unidade)
        #for posic
        #if obter_inimigos_adjacentes(obter_posicao(unidade)) != ():
            ##Realizar o ataque
            #unidade_ataca(unidade, obter_unidade(m,  
            
        #else:
            #Realizar o ataque
            
    
    #Realizar ataque