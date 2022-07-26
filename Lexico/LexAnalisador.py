# -*- coding: utf-8 -*-

from Lexico.lexicoSimbolos import *

# AFD é interpretado usando a estrutura Dicionario do Python
afd = {
    0: {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
        '"': 9,
        'a': 11, 'b': 11, 'c': 11, 'd': 11, 'e': 11, 'f': 11, 'g': 11, 'h': 11, 'i': 11, 'j': 11, 'k': 11, 'l': 11,
        'm': 11, 'n': 11, 'o': 11, 'p': 11, 'q': 11, 'r': 11, 's': 11, 't': 11, 'u': 11, 'v': 11, 'w': 11, 'x': 11,
        'y': 11, 'z': 11,
        'A': 11, 'B': 11, 'C': 11, 'D': 11, 'E': 11, 'F': 11, 'G': 11, 'H': 11, 'I': 11, 'J': 11, 'K': 11, 'L': 11,
        'M': 11, 'N': 11, 'O': 11, 'P': 11, 'Q': 11, 'R': 11, 'S': 11, 'T': 11, 'U': 11, 'V': 11, 'W': 11, 'X': 11,
        'Y': 11, 'Z': 11,
        '>': 12,
        '=': 13,
        '<': 14,
        '*': 16, '+': 16, '/': 16, '-': 16,
        '(': 17,
        ')': 18,
        ';': 19,
        '{': 20},
    1: {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1,
        'E': 2, 'e': 2,
        '.': 5},
    2: {'0': 4, '1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, '7': 4, '8': 4, '9': 4,
        '+': 3, '-': 3},
    3: {'0': 4, '1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, '7': 4, '8': 4, '9': 4},
    4: {'0': 4, '1': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, '7': 4, '8': 4, '9': 4},
    5: {'0': 5, '1': 5, '2': 5, '3': 5, '4': 5, '5': 5, '6': 5, '7': 5, '8': 5, '9': 5,
        'E': 6, 'e': 6, },
    6: {'0': 8, '1': 8, '2': 8, '3': 8, '4': 8, '5': 8, '6': 8, '7': 8, '8': 8, '9': 8,
        '+': 7, '-': 7},
    7: {'0': 8, '1': 8, '2': 8, '3': 8, '4': 8, '5': 8, '6': 8, '7': 8, '8': 8, '9': 8},
    8: {'0': 8, '1': 8, '2': 8, '3': 8, '4': 8, '5': 8, '6': 8, '7': 8, '8': 8, '9': 8},
    9: {'a': 9, 'b': 9, 'c': 9, 'd': 9, 'e': 9, 'f': 9, 'g': 9, 'h': 9, 'i': 9, 'j': 9, 'k': 9, 'l': 9, 'm': 9, 'n': 9,
        'o': 9, 'p': 9, 'q': 9, 'r': 9, 's': 9, 't': 9, 'u': 9, 'v': 9, 'w': 9, 'x': 9, 'y': 9, 'z': 9,
        'A': 9, 'B': 9, 'C': 9, 'D': 9, 'E': 9, 'F': 9, 'G': 9, 'H': 9, 'I': 9, 'J': 9, 'K': 9, 'L': 9, 'M': 9, 'N': 9,
        'O': 9, 'P': 9, 'Q': 9, 'R': 9, 'S': 9, 'T': 9, 'U': 9, 'V': 9, 'W': 9, 'X': 9, 'Y': 9, 'Z': 9,
        '0': 9, '1': 9, '2': 9, '3': 9, '4': 9, '5': 9, '6': 9, '7': 9, '8': 9, '9': 9,
        ',': 9, ';': 9, ':': 9, '!': 9, '?': 9, '\\': 9, '*': 9, '+': 9, '-': 9, '/': 9, '(': 9, ')': 9, '{': 9, '}': 9,
        '[': 9, ']': 9, '<': 9, '>': 9, '=': 9, ' ': 9, '.': 9,
        '"': 10},
    10: {},
    11: {'a': 11, 'b': 11, 'c': 11, 'd': 11, 'e': 11, 'f': 11, 'g': 11, 'h': 11, 'i': 11, 'j': 11, 'k': 11, 'l': 11,
         'm': 11, 'n': 11, 'o': 11, 'p': 11, 'q': 11, 'r': 11, 's': 11, 't': 11, 'u': 11, 'v': 11, 'w': 11, 'x': 11,
         'y': 11, 'z': 11,
         'A': 11, 'B': 11, 'C': 11, 'D': 11, 'E': 11, 'F': 11, 'G': 11, 'H': 11, 'I': 11, 'J': 11, 'K': 11, 'L': 11,
         'M': 11, 'N': 11, 'O': 11, 'P': 11, 'Q': 11, 'R': 11, 'S': 11, 'T': 11, 'U': 11, 'V': 11, 'W': 11, 'X': 11,
         'Y': 11, 'Z': 11,
         '0': 11, '1': 11, '2': 11, '3': 11, '4': 11, '5': 11, '6': 11, '7': 11, '8': 11, '9': 11,
         '_': 11},
    12: {'=': 13},
    13: {},
    14: {'>': 13, '=': 13, '-': 15},
    15: {},
    16: {},
    17: {},
    18: {},
    19: {},
    20: {'a': 20, 'b': 20, 'c': 20, 'd': 20, 'e': 20, 'f': 20, 'g': 20, 'h': 20, 'i': 20, 'j': 20, 'k': 20, 'l': 20,
         'm': 20, 'n': 20, 'o': 20, 'p': 20, 'q': 20, 'r': 20, 's': 20, 't': 20, 'u': 20, 'v': 20, 'w': 20, 'x': 20,
         'y': 20, 'z': 20,
         'A': 20, 'B': 20, 'C': 20, 'D': 20, 'E': 20, 'F': 20, 'G': 20, 'H': 20, 'I': 20, 'J': 20, 'K': 20, 'L': 20,
         'M': 20, 'N': 20, 'O': 20, 'P': 20, 'Q': 20, 'R': 20, 'S': 20, 'T': 20, 'U': 20, 'V': 20, 'W': 20, 'X': 20,
         'Y': 20, 'Z': 20,
         '0': 20, '1': 20, '2': 20, '3': 20, '4': 20, '5': 20, '6': 20, '7': 20, '8': 20, '9': 20,
         ',': 20, ';': 20, ':': 20, '!': 20, '?': 20, '\\': 20, '*': 20, '+': 20, '-': 20, '/': 20, '(': 20, ')': 20,
         '{': 20, '}': 20, '[': 20, ']': 20, '<': 20, '>': 20, '=': 20, ' ': 20, '"': 20, '.': 20,
         '}': 21},
    21: {}
}

# Lista de certas classes para checagem durante o programa
Classes = {1: 'NUM', 4: 'NUM', 5: 'NUM', 8: 'NUM', 9: 'LIT0', 10: 'LIT', 11: 'ID', 12: 'OPR', 13: 'OPR', 14: 'OPR',
           15: 'RCB', 16: 'OPM', 17: 'AB_P', 18: 'FC_P', 19: 'PT_V', 20: 'COM0', 21: 'COM1'}


def scanner(base, tabelaSimbolos, posicao, l, c):
    
    # ERROR flag
    error = False

    # Seta o cursos de leitura na posiçao correta e seta o restante do arquivo para a variavel file
    base.seek(posicao)
    file = base.read()
    # Seta variaveis bases para seu estado padrão
    estado = 0
    classe = ''
    lexema = ''
    tipo = "Nulo"
    token = None
    for character in file:

        # Incrementa a posiçao do cursor e do contador de coluna
        posicao += 1
        c += 1

        # Testa a AFD a partir do estado base, atualizando o estado atual com o proximo estado da AFD
        # A medida que a AFD é rodada, atualizamos o lexema com os caracteres lidos juntamente com a classe
        try:
            # print(character, posicao)

            estado = afd[estado][character]
            lexema = lexema + character
            classe = Classes[estado]

            # Atuzlizamos o tipo caso seje necessario
            if classe == 'NUM' and estado == 1 or estado == 4:
                tipo = "inteiro"
            elif classe == 'NUM' and estado == 5 or estado == 8:
                tipo = "real"
            elif classe == 'LIT':
                tipo = "literal"

        # Quando a AFD falha, verificamos se um token foi encontrado ou se algum outro erro foi encontrado
        except:

            # Primeiro verificamos se o caracter que gerou a falha foi um espaçamento
            if character.isspace():

                # Verificação de erro a partir da ausencia de uma classe
                if classe == "":
                    classe = 'ERRO'
                    lexema = character
                    if not (lexema.isspace()):
                        token = {"Classe": classe, "Lexema": lexema, "Tipo": tipo}

                # Verifica se o token é uma palavra reserva
                elif classe == 'ID' and lexema in Preservadas:
                    token = tabelaSimbolos.get(lexema)

                # Atualizamos a variavel token com o token encontrado
                else:
                    token = {"Classe": classe, "Lexema": lexema, "Tipo": tipo}

                # Variaveis bases (com exceçao do token) são resetadas novamente
                estado = 0
                classe = ''
                lexema = ''
                tipo = "Nulo"

                if character == '\n':
                    c -= 1

            # Falha na AFD não ocorreu devido a um espaçamento, mas a um caracter especifico
            else:

                # Verificação de erro a partir da ausencia de uma classe
                if classe == "":
                    classe = 'ERRO'
                    lexema = character
                    if not (lexema.isspace()):
                        token = {"Classe": classe, "Lexema": lexema, "Tipo": tipo}

                else:
                    # Verifica se o token é uma palavra reserva
                    if classe == 'ID' and lexema in Preservadas:
                        token = (tabelaSimbolos.get(lexema))

                    # Atualizamos a variavel token com o token encontrado
                    else:
                        token = {"Classe": classe, "Lexema": lexema, "Tipo": tipo}
                
                    # Movemos o cursor para tras para verificar posteriormente se o caracter que causou a falha é um
                    # outro token
                    posicao -= 1
                    c -= 1

        # Caso um erro foi encontrado, mandamos uma mensagem de erro com a linha e coluna do erro encontrado,
        # zerando a variavel classe
        if classe == 'ERRO':
            print("ERRO léxico – Caractere inválido na linguagem. Linha {linha}, coluna {coluna}.".format(linha=l,
                                                                                                          coluna=c))
            error = True                                                                                                          
            classe = ""

        # Checamos se o comentario foi fechado, imprimindo erro caso não tenha sido, e ignoramos o comentario caso esteja correto
        if token != None and token['Classe'] == 'COM0':
            print("ERRO léxico – Não fechou as Chaves. Linha {linha}, coluna {coluna}.".format(linha=l, coluna=c))
            token = {"Classe": 'ERRO', "Lexema": '}', "Tipo": tipo}
            error = True

        if (token != None and token['Classe'] == 'COM1'):
            token = None

        # Checamos se as aspas foi fechada, imprimindo erro caso não tenha sido
        if (token != None and token['Classe'] == 'LIT0'):
            print("ERRO léxico – Não fechou as Aspas. Linha {linha}, coluna {coluna}.".format(linha=l, coluna=c))
            token = {"Classe": 'ERRO', "Lexema": '"', "Tipo": tipo}
            error = True

        #atualizamos a tabela de simbolos se for necessario
        if (token != None and not Busca(token['Lexema'], tabelaSimbolos) and token['Classe'] == 'ID'):
                        Insercao(token, tabelaSimbolos)

        # Caso a variavel token não seja nula, retornamos o token encontrado
        if not (token is None):
            return token, posicao, l, c, error

        # checa pula de linha para incrementar o contador de linha e zerar o contador de coluna
        if character == '\n':
            l += 1
            c = 0

    # No final do arquivo, verificamos se houve um token ou erro perdino nos ultimos caracteres do arquivo

    if not (classe == "" and lexema == ""):
        if classe == 'ERRO':
            lexema = character
            if not (lexema.isspace()):
                token = {"Classe": classe, "Lexema": lexema, "Tipo": tipo}

        elif classe == 'COM0':
            print("ERRO léxico – Não fechou as Chaves. Linha {linha}, coluna {coluna}.".format(linha=l, coluna=c))
            token = {"Classe": 'ERRO', "Lexema": '}', "Tipo": tipo}
            error = True

        elif classe == 'LIT0':
            print("ERRO léxico – Não fechou as Aspas. Linha {linha}, coluna {coluna}.".format(linha=l, coluna=c))
            token = {"Classe": 'ERRO', "Lexema": '"', "Tipo": tipo}
            error = True

        elif classe == 'ID' and lexema in Preservadas:
            token = (tabelaSimbolos.get(lexema))

        else:
            token = {'Classe': classe, 'Lexema': lexema, 'Tipo': tipo}

        if not (Busca(token['Lexema'], tabelaSimbolos) and token['Classe'] != 'ID'):
            Insercao(token, tabelaSimbolos)

        posicao +=1

        if not token['Classe'] == 'COM1':
            return token, posicao, l, c, error

        else:
            token = {'Classe': 'EOF', 'Lexema': 'EOF', 'Tipo': 'Nulo'}

            if not (Busca(token['Lexema'], tabelaSimbolos) and token['Classe'] != 'ID'):
                Insercao(token, tabelaSimbolos)

            return token, posicao, l, c, error

    # Caso não haja, encontramos o EOF do arquivo, retornando assim seu token correspondente
    else:
        token = {'Classe': 'EOF', 'Lexema': 'EOF', 'Tipo': 'Nulo'}

        return token, posicao, l, c, error