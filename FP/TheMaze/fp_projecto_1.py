#93866 Joao Antonio Pinheiro Lopes

#Codigo redigido segundo o PEP8 e PEP257


def eh_labirinto(labirinto):
    """Verifica se e labirinto.
    
    Assinatura da funcao:
    eh_labirinto: universal -- booleano
    
    Retorna True se o argumento labirinto e um labirinto.
    """
    if isinstance(labirinto, tuple):
        for indice_x in range(len(labirinto)):
            coluna_actual = labirinto[indice_x]
            coluna_anterior = labirinto[indice_x - 1]
            if (isinstance(coluna_actual, tuple) and 
               (len(coluna_anterior) == len(coluna_actual))):
                for indice_y in range(len(coluna_actual)):
                    valor = labirinto[indice_x][indice_y]
                    if (indice_x == 0) or (indice_x == (len(labirinto) - 1)):
                        if valor == 1:
                            pass
                        else:
                            return False
                    if ((indice_y == 0) or
                        (indice_y == (len(labirinto[indice_x]) - 1))):
                        if valor == 1:
                            pass                  
                        else:
                            return False
        return True
    return False

def eh_posicao(posicao):
    """Verifica se e posicao.
    
    Assinatura da funcao:
    eh_posicao: universal -- booleano
    
    Retorna True se o argumento posicao e uma posicao.
    """
    if isinstance(posicao, tuple) and (len(posicao) == 2):
        coordenada_x = posicao[0]
        coordenada_y = posicao[1]
        if isinstance(coordenada_x, int) and isinstance(coordenada_y, int):
            return (coordenada_x >= 0) and (coordenada_y >= 0)
    else:
        return False
    
def eh_conj_posicoes(conj_posicoes):
    """Verifica se e um conjunto de posicoes.
    
    Assinatura da funcao:
    eh_conj_posicoes: universal -- booleano
    
    Retorna True se o argumento conj_posicoes e um conjunto de posicoes.
    """
    if isinstance(conj_posicoes, tuple) and isinstance(conj_posicoes[0], tuple):
        guarda_posicoes = ()
        for indice_posicao in range(len(conj_posicoes)):
            posicao_atual = conj_posicoes[indice_posicao]
            if ((eh_posicao(posicao_atual) ) and
                (posicao_atual not in guarda_posicoes)):
                guarda_posicoes = guarda_posicoes + (posicao_atual,)
            else:
                return False
        return True
    return False

def tamanho_labirinto(labirinto):
    """Calcula as dimensoes do labirinto.

    Assinatura da funcao:
    tamanho_labirinto: labirinto -- tuplo

    Excepcoes:
    Caso o argumento fornecido nao seja do tipo labirinto e gerado um erro de
    valor.
    
    Retorna um tuplo que contem no seu primeiro valor a coordenada Nx
    (corresponde as colunas) e no seu segundo valor a coordenada Ny
    (corresponde as linhas).
    """
    if eh_labirinto(labirinto) == True:
        numero_colunas = len(labirinto)
        numero_linhas = len(labirinto[0])
        tamanho_labirinto = (numero_colunas, numero_linhas)
        return tamanho_labirinto
    raise ValueError("tamanho_labirinto: argumento invalido")

def eh_mapa_valido(labirinto, conj_posicoes):
    """Verifica se e um mapa valido.
    
    Assinatura da funcao:
    eh_mapa_valido: labirinto x conj_posicoes -- booleano
    
    Excepcoes:
    Caso os argumentos fornecidos nao sejam um labirinto e um conjunto de
    posicoes e gerado um erro de valor.
    
    Retorna True se o conjunto de posicoes fornecidas (correspondentes as
    unidades presentes no labirinto) sao compativeis dentro do labirinto.
    """
    if ((eh_labirinto(labirinto) == True) and
        (eh_conj_posicoes(conj_posicoes) == True)):
        for indice_posicao in range(len(conj_posicoes)):
            posicao_atual = conj_posicoes[indice_posicao]
            if eh_posicao(posicao_atual) == True:
                coluna = posicao_atual[0]
                linha = posicao_atual[1]
                if (0 < coluna < len(labirinto) - 1) and (0 < linha
                    < len(labirinto[coluna]) - 1):
                    pass
                else:
                    return False
        return True
    raise ValueError("eh_mapa_valido: algum dos argumentos e invalido")
    
def eh_posicao_livre(labirinto, conj_posicoes, posicao):
    """Verifica se e posicao livre.
    
    Assinatura da funcao:
    eh_posicao_livre: labirinto x conj_posicoes x posicao -- booleano
    
    Excepcoes:
    Caso o labirinto e o conjunto de posicoes nao seja um mapa valido e gerado
    um erro de valor. Ou, se a posicao fornecida nao corresponde efetivamente a
    uma posicao. Por mapa valido entenda-se um labirinto com um conjunto
    de posicoes compativeis.
    
    Retorna True se o conjunto de posicoes e valido dentro do labirinto e se
    posicao corresponde a uma posicao livre dentro do labirinto
    """
    if ((eh_mapa_valido(labirinto, conj_posicoes) == eh_posicao(posicao)
         == True)):
        dimensao_labirinto = tamanho_labirinto(labirinto)
        numero_colunas = dimensao_labirinto[0]
        numero_linhas = dimensao_labirinto[1]
        coluna = posicao[0]
        linha = posicao[1]
        if ((posicao not in conj_posicoes) and
            (0 < coluna < numero_colunas) and (0 < linha < numero_linhas)):
            return True
        return False
    raise ValueError("eh_posicao_livre: algum dos argumentos e invalido")

def posicoes_adjacentes(posicao):
    """Cria o conjunto de posicoes adjacentes.
    
    Assinatura da funcao:
    posicoes_adjacentes: posicao -- conj_posicoes
    
    Excepcoes:
    Caso o argumento fornecido nao corresponda a uma posicao e gerado um erro de
    valor.
    
    Retorna o conjunto de posicoes adjacentes a posicao de acordo com a ordem de
    leitura do labirinto.
    """
    if eh_posicao(posicao) == True:
        coluna = posicao[0]
        linha = posicao[1]
        if coluna != 0:
            if linha != 0:
                conj_posicoes = ((coluna, linha - 1), (coluna - 1, linha), 
                                 (coluna + 1, linha), (coluna, linha + 1))
            else:
                conj_posicoes = ((coluna - 1, linha), (coluna + 1, linha), 
                                 (coluna, linha + 1))
        else:
            if linha != 0:
                conj_posicoes = ((coluna, linha - 1), (coluna + 1, linha),
                                 (coluna, linha + 1))
            else:
                conj_posicoes = ((coluna + 1, linha), (coluna, linha + 1))
        return conj_posicoes
    raise ValueError("posicoes_adjacentes: argumento invalido")

#Funcao auxiliar que coloca as unidades no labirinto para facilitar a posterior
#representacao externa
def muda_labirinto(labirinto, conj_posicoes):
    """Altera o labirinto.
    
    Assinatura da funcao:
    muda_labirinto: labirinto x conj_posicoes -- labirinto
    
    Retorna um labirinto com as unidades do conjunto de posicoes presentes.
    """
    dimensao_labirinto = tamanho_labirinto(labirinto)
    coluna_labirinto = dimensao_labirinto[0]
    linha_labirinto = dimensao_labirinto[1]    
    posicao = ()        
    for indice_pos in range(len(conj_posicoes)):
        posicao = conj_posicoes[indice_pos]
        coluna_posicao = posicao[0]
        linha_posicao = posicao[1]
        for indice_x in range(coluna_labirinto):
            for indice_y in range(linha_labirinto):
                if ((indice_x == coluna_posicao) and
                    (indice_y == linha_posicao)):
                    labirinto = labirinto[:indice_x] \
                        + (labirinto[indice_x][:indice_y] + (2,) \
                        + labirinto[indice_x][indice_y + 1:linha_labirinto],) \
                        + labirinto[(indice_x+1):]
    return labirinto

def mapa_str(labirinto, conj_posicoes):
    """Fornece o mapa do labirinto.
    
    Assinatura da funcao:
    mapa_str: labirinto x conj_posicoes -- cadeia de caracteres (String)
    
    Excepcoes:
    Caso o labirinto e o conjunto de posicoes nao correspondam a uma mapa valido
    e gerado um erro de valor.
    
    Retorna a representacao externa do labirinto, ou seja uma estrutura de Nx
    colunas e Ny linhas com respetivas paredes e unidades.
    """
    if eh_mapa_valido(labirinto, conj_posicoes) == True:
        novo_labirinto = muda_labirinto(labirinto, conj_posicoes)
        dimensao_labirinto = tamanho_labirinto(novo_labirinto)
        coluna_labirinto = dimensao_labirinto[0]
        linha_labirinto = dimensao_labirinto[1]
        parede = '#'
        vazio = '.'
        labirinto_externo = ''
        for indice_y in range(linha_labirinto):
            for indice_x in range(coluna_labirinto):
                valor = novo_labirinto[indice_x][indice_y]
                if valor == 1:
                    labirinto_externo = labirinto_externo + parede
                elif valor == 2:
                    labirinto_externo = labirinto_externo + 'O'
                else:
                    labirinto_externo = labirinto_externo + vazio  
            labirinto_externo = labirinto_externo + '\n'
        labirinto_externo = labirinto_externo[:len(labirinto_externo - 1)]
        return labirinto_externo
    raise ValueError("mapa_str: algum dos argumentos e invalido")

def obter_objetivos(labirinto, conj_posicoes, posicao):
    """Obtem as posicoes objetivo.
    
    Assinatura da funcao:
    obter_objetivos: labirinto x conj_posicoes x posicao -- conj_posicoes
    
    Excepcoes:
    Caso o labirinto e o conjunto de posicoes nao correspondam a um mapa valido
    ou se a posicao fornecida nao pertence ao conjunto de posicoes fornecido, 
    entao nao e possivel obter o conjunto de posicoes objetivo da posicao. E 
    gerado um erro de valor.
    
    Retorna o conjunto de posicoes objetivo da posicao fornecida.
    """
    if ((eh_mapa_valido(labirinto, conj_posicoes) == True) and
        (posicao in conj_posicoes)):
        posicao_actual = ()
        posicoes_objetivo = ()
        for indice_posicao in range(len(conj_posicoes)):
            posicao_actual = conj_posicoes[indice_posicao]
            if posicao != posicao_actual:
                posicoes_objetivo = (posicoes_objetivo 
                                     + posicoes_adjacentes(posicao_actual))
        novo_objetivo = ()
        for indice_objetivo in range(len(posicoes_objetivo)):
            posicao_objetivo = posicoes_objetivo[indice_objetivo]
            coluna_objetivo = posicao_objetivo[0]
            linha_objetivo = posicao_objetivo[1]
            if posicao == posicao_objetivo:
                pass
            else:
                if ((labirinto[coluna_objetivo][linha_objetivo] != 1) and
                    (posicao_objetivo not in novo_objetivo)):
                    novo_objetivo = novo_objetivo + (posicao_objetivo,)
        return novo_objetivo
    raise ValueError("obter_objetivos: algum dos argumentos e invalido")
        
#def obter_caminho(labirinto, conj_posicoes, posicao):
    #"""Obtem o caminho entre duas posicoes.
    
    #Assinatura da funcao:
    #obter_caminho: labirinto x conj_posicoes x posicao -- conj_posicoes
    
    #Excepcoes:
    #Caso o labirinto e o conjunto de posicoes nao correspondam a um mapa valido
    #ou se a posicao fornecida nao pertence ao conjunto de posicoes fornecido, 
    #entao nao e possivel obter um caminho partindo de posicao. E gerado um erro
    #de valor.
    
    #Retorna o conjunto de posicoes que correspondem ao caminho percorrido.
    #"""    
    #if ((eh_mapa_valido(labirinto, conj_posicoes) == True) and
        #(posicao in conj_posicoes)):
        ##estrutura de dados do tipo Fila
        #posicao_atual = ()
        #caminho_atual = []
        #lista_exploracao = [(posicao, [])]
        #posicoes_visitadas = []
        #objetivos_possiveis = obter_objetivos(labirinto, conj_posicoes, posicao)
        ##posicoes_possiveis = ()
        #while lista_exploracao != []:
            #posicao_atual = lista_exploracao[0][0]
            #caminho_atual = lista_exploracao[0][1]
            #if posicao_atual not in posicoes_visitadas:
                #posicoes_visitadas = posicoes_visitadas + [posicao_atual]
                #caminho_atual = caminho_atual + [posicao_atual]
                #if posicao_atual in objetivos_possiveis:
                    #break   
                #else:
                    #posicoes_possiveis = posicoes_adjacentes(posicao_atual)
                    #for indice_possivel in range(len(posicoes_possiveis)):
                        #if (eh_posicao_livre(labirinto, conj_posicoes,
                                            #posicoes_possiveis[indice_possivel])
                                            #== True):
                            #lista_exploracao.append([posicoes_possiveis[
                                                     #indice_possivel],
                                                     #caminho_atual])
            #lista_exploracao.remove([posicao_atual, caminho_atual])
        #return caminho_atual 
    #raise ValueError("obter_caminho: algum dos argumentos e invalido")

#def mover_unidade(labirinto, conj_posicoes, posicao):
    #"""Efetua o caminho entre posicoes.
    
    #Assinatura da funcao:
    #mover_unidade: labirinto x conj_posicoes x posicao -- conj_posicoes
    
    #Excepcoes:
    #Caso o labirinto e o conjunto de posicoes nao correspondam a um mapa valido
    #ou se a posicao fornecida nao pertence ao conjunto de posicoes fornecido, 
    #entao nao e possivel mover a unidade. E gerado um erro de valor.
    
    #Retorna a representacao externa correspondente ao caminho percorrido.
    #"""    
    #if ((eh_mapa_valido(labirinto, conj_posicoes) == True) and
        #(posicao in conj_posicoes)):
        #caminho = obter_caminho(labirinto, conj_posicoes, posicao)
        #antigo_labirinto = mapa_str(labirinto, conj_posicoes)
        #novo_labirinto = ()
        #for indice_caminho in range(len(caminho)):
            #posicao_atual = caminho[indice_caminho]
        #return novo_labirinto
    #raise ValueError("mover_unidade: algum dos argumentos e invalido")