# -*- coding: utf-8 -*-

from Sintatico.AnalisadorSintatico import *
from Semantico.AnalisadorSemantico import *

def main():
    tabelaSimbolos = criarTabelaSimbolos()
    base = open("ProgBase/base3.alg", 'r')
    ObjCorpo, ObjTemporarias, error = parser(base,tabelaSimbolos)
    if not error:
        gerador(ObjCorpo, ObjTemporarias)

main()