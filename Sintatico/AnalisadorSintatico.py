# -*- coding: utf-8 -*-

from Lexico.LexAnalisador import *
from Semantico.AnalisadorSemantico import *
from Sintatico.Fsecundarias import *

# Leitura da tabela ACTION-GOTO
tabela, header = leitutragoto()

# Regras gramaticais
gramatica = gramatica()

# Follow de não terminais
follow = follow()

# Inicializa a pilha sintatica, semantica e flago de erro
pilhaSintatica = ['0']
pilhaSemantica = []
error = False

# Algoritmo de analise - PARSER
def parser(base, tabelaSimbolos):

    #variaveis globais
    global pilhaSintatica
    global pilhaSemantica
    global error    

    # Inicializa as variaveis para o Scanner
    token = {'Classe': '', 'Lexema': '', 'Tipo': ''}
    l = 1
    c = 0
    posicao = 0
    token, posicao, l, c, error = scanner(base, tabelaSimbolos, posicao, l, c)

    # Seja a o primeiro símbolo de w$;
    a = token['Classe']

    while (True):

        # Caso ocorra erro sintatico, pega o proximo token e reinicia o loop
        if a == "ERRO":
            token, posicao, l, c, error = scanner(base, tabelaSimbolos, posicao, l, c)
            a = token['Classe']
            continue

        # seja s o estado no topo da pilha sintatica;
        S = pilhaSintatica[-1]

        # Define Action[S,a] e t
        string = tabela[int(S)][header[a]]
        action, t = string[0], string[1:]

        # if (ACTION [s,a] = shift t ) {
        if action == 'S':
            # empilha t na pilha sintatica;
            pilhaSintatica.append(t)

            # empilha valor lexico na pilha semantica
            if Busca(token['Lexema'],tabelaSimbolos):
                pilhaSemantica.append(tabelaSimbolos[token['Lexema']])
            else:
                pilhaSemantica.append(token)
                
            # seja a o próximo símbolo da entrada;
            token, posicao, l, c, error = scanner(base, tabelaSimbolos, posicao, l, c)
            a = token['Classe']

        #  }else if (ACTION [s,a] = reduce A-> β ) {
        elif action == 'R':
            # Define alfa e beta
            alfa, beta = gramatica[int(t)].split("->")

            # desempilha | β | símbolos da pilha sintatica (a quantidade de símbolos de beta);
            for i in range(len(beta.split())):
                pilhaSintatica.pop()

            # faça o estado t agora ser o topo da pilha sintatica;
            t = pilhaSintatica[-1]

            # empilhe GOTO[t,A] na pilha sintatica
            estado = tabela[int(t)][header[alfa]]
            pilhaSintatica.append(estado)

            # imprima a produção A-> β ;
            regra = "{0} -> {1}".format(alfa,beta)
            
            # gerador semantico
            ObjCorpo, ObjTemporarias,pilhaSemantica,tabelaSimbolos, error = tradutor(regra,pilhaSemantica,tabelaSimbolos,l,c)

        # } else if (ACTION [s,a] = accept ) pare; /* a análise terminou*/
        elif action == 'A':
            return ObjCorpo, ObjTemporarias, error

        # else invocar uma rotina de recuperação do erro;
        elif action == 'E':
            # MODO PANICO seguindo o livro do Dragão

            # Checa qual token possivel estava aguardando
            count = 0
            for i in tabela[int(S)]:
                if i != 'Er' and i != S:
                    esperado = list(header.keys())[count]
                    break
                count += 1

            # Imprimi mensagem de Erro
            print(
                'ERROR Sintatico - Esperava Token {esp} - Linha {linha}, Coluna {coluna}'.format(esp=esperado, linha=l,
                                                                                                 coluna=c))
            error = True                                                                                                 

            # escaneamos a pilha sintatica procurando um 's' com um GOTO em um não terminal particular 'A'
            for i in reversed(pilhaSintatica):
                # se chegar no final do arquivo sem retomar analise, finaliza analise
                if token['Classe'] == 'EOF':
                    print('ERROR - Não pode ser continuada a analise')
                    return ObjCorpo, ObjTemporarias, error
                elif tabela[int(i)][header["P"]].isnumeric():
                    S = i
                    A = "P"
                    break
                elif tabela[int(i)][header["V"]].isnumeric():
                    S = i
                    A = "V"
                    break
                elif tabela[int(i)][header["A"]].isnumeric():
                    S = i
                    A = "A"
                    break
                elif tabela[int(i)][header["ES"]].isnumeric():
                    S = i
                    A = "ES"
                    break
                elif tabela[int(i)][header["LV"]].isnumeric():
                    S = i
                    A = "LV"
                    break
                elif tabela[int(i)][header["D"]].isnumeric():
                    S = i
                    A = "D"
                    break
                elif tabela[int(i)][header["CMD"]].isnumeric():
                    S = i
                    A = "CMD"
                    break
                elif tabela[int(i)][header["COND"]].isnumeric():
                    S = i
                    A = "COND"
                    break
                elif tabela[int(i)][header["CAB"]].isnumeric():
                    S = i
                    A = "CAB"
                    break
                elif tabela[int(i)][header["EXP_R"]].isnumeric():
                    S = i
                    A = "EXP_R"
                    break
                elif tabela[int(i)][header["R"]].isnumeric():
                    S = i
                    A = "R"
                    break
                elif tabela[int(i)][header["CP"]].isnumeric():
                    S = i
                    A = "CP"
                    break
                elif tabela[int(i)][header["CABR"]].isnumeric():
                    S = i
                    A = "CABR"
                    break
                elif tabela[int(i)][header["CPR"]].isnumeric():
                    S = i
                    A = "CPR"
                    break
                else:
                    pilhaSintatica.pop()

            # Zero ou mais inputs são descartados até encontrar um simbolo 'a' que Follow A
            while True:
                for k in follow[A].split():
                    if token['Classe'] == k:
                        break
                else:
                    token, posicao, l, c, error = scanner(base, tabelaSimbolos, posicao, l, c)
                    a = token['Classe']
                    continue
                break

            # O Parser então empilha o GOTO(s,A) e continua a analise
            estado = tabela[int(S)][header[A]]
            pilhaSintatica.append(estado)
