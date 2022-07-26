# -*- coding: utf-8 -*-

from Lexico.lexicoSimbolos import *

# Inicializa a lista do corpo do Programa.c e das variaveis temporarias 
# e flago de erro
ObjCorpo = []
ObjTemporarias = []
index = 0
error = False

# Função tradutor aplica as regras semanticas e construi 
# as estruturas usadas para criar o Progrma.c
def tradutor(regra,pilhaSemantica,tabelaSimbolos,l,c):

    # Variaveis globais usadadas no tradutor
    global ObjCorpo
    global ObjTemporarias
    global index
    global error
        
    # Verifica se L e TIPO são do mesmo tipo, caso não é erro
    # Imprimi ';'
    if regra == "D -> TIPO L pt_v":
        if pilhaSemantica[-2]['Tipo'] == pilhaSemantica[-3]['Tipo']:
            ObjCorpo.append(';\n')
        else:
            print('ERROR Semantico - Operandos com tipos incompatíveis - Linha {linha}, Coluna {coluna}'.format( linha=l,coluna=c))
            error = True

    # L se torna o id, atualizando seu tipo na tabela de simbolos
    # Imprimi L
    # L é colocado na pilha semantica
    elif regra == "L -> id":
        L = pilhaSemantica.pop()
        tabelaSimbolos = Atualizacao(L,pilhaSemantica[-1]['Tipo'],tabelaSimbolos)
        L['Tipo'] = pilhaSemantica[-1]['Tipo']
        ObjCorpo.append('{0}'.format(L['Lexema']))
        pilhaSemantica.append(L)
 
    # TIPO se torna inteiro
    # Imprimi TIPO
    # TIPO é colocado na pilha semantica
    elif regra == "TIPO -> inteiro":
        TIPO = pilhaSemantica.pop()
        ObjCorpo.append('{0} '.format('int'))
        pilhaSemantica.append(TIPO)

    # TIPO se torna real
    # Imprimi TIPO
    # TIPO é colocado na pilha semantica
    elif regra == "TIPO -> real":
        TIPO = pilhaSemantica.pop()
        ObjCorpo.append('{0} '.format('float'))
        pilhaSemantica.append(TIPO)

    # TIPO se torna literal
    # Imprimi TIPO
    # TIPO é colocado na pilha semantica
    elif regra == "TIPO -> literal":
        TIPO = pilhaSemantica.pop()
        ObjCorpo.append('{0} '.format(TIPO['Lexema']))
        pilhaSemantica.append(TIPO)
    
    # Verifica se o tipo de id é nulo, caso sim é erro
    # Verifica se o tipo de id é literal, caso sim Imprimi a linha respectiva
    # Verifica se o tipo de id é inteiro, caso sim Imprimi a linha respectiva
    # Verifica se o tipo de id é real, caso sim Imprimi a linha respectiva
    elif regra == "ES -> leia id pt_v":
        if pilhaSemantica[-2]['Tipo'] != 'Nulo':
            if pilhaSemantica[-2]['Tipo'] == 'literal':
                ObjCorpo.append('scanf("%s",{0});\n'.format(pilhaSemantica[-2]['Lexema']))
            elif pilhaSemantica[-2]['Tipo'] == 'inteiro':
                ObjCorpo.append('scanf("%d",&{0});\n'.format(pilhaSemantica[-2]['Lexema']))
            elif pilhaSemantica[-2]['Tipo'] == 'real':
                ObjCorpo.append('scanf("%lf",&{0});\n'.format(pilhaSemantica[-2]['Lexema']))
        else:
            print('ERROR Semantico - Variável não declarada - Linha {linha}, Coluna {coluna}'.format( linha=l,coluna=c))
            error = True

    # Verifica se classe de ARG é ID, caso sim:
    # Verifica se o tipo de ARG é literal, caso sim Imprimi a linha respectiva
    # Verifica se o tipo de ARG é inteiro, caso sim Imprimi a linha respectiva
    # Verifica se o tipo de ARG é real, caso sim Imprimi a linha respectiva
    # caso não, Imprimi a senteça (Não há ID)
    elif regra == "ES -> escreva ARG pt_v":
        if pilhaSemantica[-2]['Classe'] == 'ID':
            if pilhaSemantica[-2]['Tipo'] == 'literal':
                ObjCorpo.append('printf("%s",{0});\n'.format(pilhaSemantica[-2]['Lexema']))
            elif pilhaSemantica[-2]['Tipo'] == 'inteiro':
                ObjCorpo.append('printf("%d",{0});\n'.format(pilhaSemantica[-2]['Lexema']))
            elif pilhaSemantica[-2]['Tipo'] == 'real':
                ObjCorpo.append('printf("%lf",{0});\n'.format(pilhaSemantica[-2]['Lexema']))
        else:
            ObjCorpo.append('printf({0});\n'.format(pilhaSemantica[-2]['Lexema']))
        
    # ARG se torna lit
    # ARG é colocado na pilha semantica
    elif regra == "ARG -> lit":
        ARG = pilhaSemantica.pop()
        pilhaSemantica.append(ARG)

    # ARG se torna num,
    # ARG é colocado na pilha semantica
    elif regra == "ARG -> num":
        ARG = pilhaSemantica.pop()
        pilhaSemantica.append(ARG)

    # Verifica se o tipo de id é nulo, caso sim é erro
    # ARG se torna id
    # ARG é colocado na pilha semantica
    elif regra == "ARG -> id":
        if pilhaSemantica[-1]['Tipo'] != 'Nulo':
            ARG = pilhaSemantica.pop()
            pilhaSemantica.append(ARG)
        else:
            print('ERROR Semantico - Variável não declarada - Linha {linha}, Coluna {coluna}'.format( linha=l,coluna=c))
            error = True
    
    # Verifica se o tipo de id é nulo, caso sim é erro
    # Verifica se id e LD são do mesmo tipo, caso não é erro
    # Imprimi a linha respectiva
    elif regra == "CMD -> id rcb LD pt_v":
        if pilhaSemantica[-4]['Tipo'] != 'Nulo':
            if pilhaSemantica[-4]['Tipo'] == pilhaSemantica[-2]['Tipo']:
                ObjCorpo.append('{0} {1} {2};\n'.format(pilhaSemantica[-4]['Lexema'],'=',pilhaSemantica[-2]['Lexema']))
            else:
                print('ERROR Semantico - Tipos diferentes para atribuição - Linha {linha}, Coluna {coluna}'.format( linha=l,coluna=c))
                error = True
        else:
            print('ERROR Semantico - Variável não declarada - Linha {linha}, Coluna {coluna}'.format( linha=l,coluna=c))
            error = True

    # Verifica se OPRD e OPRD são do mesmo tipo e se o tipo OPRD não é literal, caso não é erro
    # LD se torna uma variavel temporaria
    # Verifica se o tipo de LD é inteiro, caso sim Imprimi variavel temporaria
    # Verifica se o tipo de LD é real, caso sim Imprimi variavel temporaria
    # Imprimi a linha respectiva
    # Incrementa o index das variaveis temporarias
    # Retira OPRD, opm, e OPRD da pilha
    # LD é colocado na pilha semantica
    elif regra == "LD -> OPRD opm OPRD":
        if pilhaSemantica[-1]['Tipo'] == pilhaSemantica[-3]['Tipo'] and pilhaSemantica[-1]['Tipo'] != 'literal':
            LD = {'Classe': 'LD', 'Lexema': 'T{0}'.format(index), 'Tipo': pilhaSemantica[-1]['Tipo']}
            if LD['Tipo'] == 'inteiro':
                ObjTemporarias.append('{0} T{1};\n'.format('int',index))
            elif LD['Tipo'] == 'real':
                ObjTemporarias.append('{0} T{1};\n'.format('float',index))
            ObjCorpo.append('{0} = {1} {2} {3};\n'.format(LD['Lexema'],pilhaSemantica[-1]['Lexema'],pilhaSemantica[-2]['Lexema'],pilhaSemantica[-3]['Lexema']))
            index+=1
            pilhaSemantica.pop()
            pilhaSemantica.pop()
            pilhaSemantica.pop()
            pilhaSemantica.append(LD)
        else:
            print('ERROR Semantico - Operandos com tipos incompatíveis - Linha {linha}, Coluna {coluna}'.format( linha=l,coluna=c))
            error = True

    # LD se torna OPRD
    # LD é colocado na pilha semantica
    elif regra == "LD -> OPRD":
        LD = pilhaSemantica.pop()
        pilhaSemantica.append(LD)
    
    # Verifica se o tipo de id é nulo, caso sim é erro
    # OPRD se torna id
    # OPRD é colocado na pilha semantica
    elif regra == "OPRD -> id":
        if pilhaSemantica[-1]['Tipo'] != 'Nulo':
            OPRD = pilhaSemantica.pop()
            pilhaSemantica.append(OPRD)
        else:
            print('ERROR Semantico - Variável não declarada - Linha {linha}, Coluna {coluna}'.format( linha=l,coluna=c))        
            error = True

    # OPRD se torna num,
    # OPRD é colocado na pilha semantica 
    elif regra == "OPRD -> num":
        OPRD = pilhaSemantica.pop()
        pilhaSemantica.append(OPRD)

    # Imprimi '}'
    elif regra == "COND -> CAB CP":
        ObjCorpo.append('}\n')

    # Imprimi a linha respectiva usando EXP_R
    elif regra == "CAB -> se ab_p EXP_R fc_p então":
        ObjCorpo.append('if({0}) {{\n'.format(pilhaSemantica[-3]['Lexema']))

    # Verifica se OPRD e OPRD são do mesmo tipo, caso não é erro
    # EXP_R se torna uma variavel temporaria
    # Verifica se o tipo de EXP_R é inteiro, caso sim Imprimi variavel temporaria
    # Verifica se o tipo de EXP_R é real, caso sim Imprimi variavel temporaria
    # Imprimi a linha respectiva
    # Incrementa o index das variaveis temporarias
    # Retira OPRD, opr, e OPRD da pilha
    # EXP_R é colocado na pilha semantica
    elif regra == "EXP_R -> OPRD opr OPRD":
        if pilhaSemantica[-1]['Tipo'] == pilhaSemantica[-3]['Tipo']:
            EXP_R = {'Classe': 'EXP_R', 'Lexema': 'T{0}'.format(index), 'Tipo': pilhaSemantica[-1]['Tipo']}
            if EXP_R['Tipo'] == 'inteiro':
                ObjTemporarias.append('{0} T{1};\n'.format('int',index))
            elif EXP_R['Tipo'] == 'real':
                ObjTemporarias.append('{0} T{1};\n'.format('float',index))
            ObjCorpo.append('{0} = {1} {2} {3};\n'.format(EXP_R['Lexema'],pilhaSemantica[-1]['Lexema'],pilhaSemantica[-2]['Lexema'],pilhaSemantica[-3]['Lexema']))
            index+=1
            pilhaSemantica.pop()
            pilhaSemantica.pop()
            pilhaSemantica.pop()
            pilhaSemantica.append(EXP_R)
        else:
            print('ERROR Semantico: Operandos com tipos incompatíveis - Linha {linha}, Coluna {coluna}'.format( linha=l,coluna=c))
            error = True

    # Imprimi a linha respectiva usando EXP_R
    elif regra == "CABR -> repita ab_p EXP_R fc_p":
        ObjCorpo.append('while({0}) {{\n'.format(pilhaSemantica[-2]['Lexema']))

    # Imprimi '}'
    elif regra == "CPR -> fimrepita":
        ObjCorpo.append('}\n')

    """
    Regras sem necessidade de regras semanticas:

    elif regra == "R -> CABR CPR":
    elif regra == "CPR -> ES CPR":
    elif regra == "CPR -> CMD CPR":
    elif regra == "CPR -> COND CPR":
    """
    # Retorna as estruturas usadas para criar o Progrma.c,
    # a pilha semantica, tabela de simbolos, e a flag de erro
    return ObjCorpo, ObjTemporarias, pilhaSemantica, tabelaSimbolos, error
    

# Função gerador constroi o Programa.c resultante do compilador
def gerador(ObjCorpo, ObjTemporarias):
    output_file = open('programa.c', 'w')

    # cabeçalho do programa c
    output_file.write("#include<stdio.h>\n")
    output_file.write("typedef char literal[256];\n")
    output_file.write("void main(void) {\n")

    # checa se existem variaveis temporaris, e imprimi elas no local especificado
    if ObjTemporarias:
        output_file.write("/*----Variaveis temporarias----*/\n")
        for lines in ObjTemporarias:
            output_file.write(lines)
        output_file.write("/*--------------------------------*/\n")

    # imprimi o restante do Programa.c
    for lines in ObjCorpo:
        output_file.write(lines)

    # fecha a função main e o arquivo
    output_file.write("}")
    output_file.close()