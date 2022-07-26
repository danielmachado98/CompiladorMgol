# -*- coding: utf-8 -*-

Preservadas = ['inicio', 'varinicio', 'varfim', 'escreva', 'leia', 'se', 'entao', 'fimse', 'repita', 'fimrepita', 'fim',
               'inteiro', 'literal', 'real']


def criarTabelaSimbolos():
    tabelaSimbolos = {}
    for palavraReserva in Preservadas:
        tabelaSimbolos[palavraReserva] = {"Classe": palavraReserva, "Lexema": palavraReserva, "Tipo": palavraReserva}
    return tabelaSimbolos


def Insercao(token, tabelaSimbolos):
    if not (token['Lexema'] in tabelaSimbolos):
        tabelaSimbolos[token['Lexema']] = token


def Busca(tokenID, tabelaSimbolos):
    if tokenID in tabelaSimbolos:
        return True
    else:
        return False


def Atualizacao(tokenVelho, tipo, tabelaSimbolos):
    if tokenVelho['Lexema'] in tabelaSimbolos:
        tabelaSimbolos.update({tokenVelho['Lexema']: {'Classe': tokenVelho['Classe'], 'Lexema': tokenVelho['Lexema'], 'Tipo': tipo}})
    return tabelaSimbolos
        
        
