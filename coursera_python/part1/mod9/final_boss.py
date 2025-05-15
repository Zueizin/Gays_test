import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    similaridade = 0
    for i in range(6):
        similaridade += abs(as_a[i] - as_b[i])
    return similaridade / 6

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    num_sentencas = len(sentencas)
    
    frases = []
    for sentenca in sentencas:
        frases.extend(separa_frases(sentenca))
    num_frases = len(frases)
    
    palavras = []
    for frase in frases:
        palavras.extend(separa_palavras(frase))
    num_palavras = len(palavras)
    
    # Calcula os traços linguísticos
    if num_palavras == 0:
        return [0, 0, 0, 0, 0, 0]
    
    # Tamanho médio de palavra
    soma_tamanho_palavras = sum(len(palavra) for palavra in palavras)
    wal = soma_tamanho_palavras / num_palavras
    
    # Relação Type-Token
    ttr = n_palavras_diferentes(palavras) / num_palavras
    
    # Razão Hapax Legomana
    hlr = n_palavras_unicas(palavras) / num_palavras
    
    # Tamanho médio de sentença (em caracteres)
    soma_tamanho_sentencas = sum(len(sentenca) for sentenca in sentencas)
    sal = soma_tamanho_sentencas / num_sentencas if num_sentencas > 0 else 0
    
    # Complexidade de sentença (frases por sentença)
    sac = num_frases / num_sentencas if num_sentencas > 0 else 0
    
    # Tamanho médio de frase (em caracteres)
    soma_tamanho_frases = sum(len(frase) for frase in frases)
    pal = soma_tamanho_frases / num_frases if num_frases > 0 else 0
    
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    similaridades = []
    for texto in textos:
        ass_texto = calcula_assinatura(texto)
        similaridade = compara_assinatura(ass_texto, ass_cp)
        similaridades.append(similaridade)
    
    # Encontra o índice do texto com menor similaridade (mais similar à assinatura CP)
    indice_menor = similaridades.index(min(similaridades))
    return indice_menor + 1  # Retorna o número do texto (1-based)

# Programa principal
assinatura_cp = le_assinatura()
textos = le_textos()
resultado = avalia_textos(textos, assinatura_cp)

print(f"O autor do texto {resultado} está provavelmente infectado com COH-PIAH!")