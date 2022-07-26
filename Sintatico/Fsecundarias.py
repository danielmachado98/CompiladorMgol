# -*- coding: utf-8 -*-

import csv
# Leitura da tabela ACTION-GOTO
def leitutragoto():
    file = open('Sintatico\ACTION-GOTO.csv',encoding='utf-8')
    ACTIONGOTO = csv.reader(file,delimiter=';')

    header = {}
    n = 0
    for c in next(ACTIONGOTO):
      header.update({c:n})
      n+=1

    tabela = list(ACTIONGOTO)
    return tabela,header
# Regras gramaticais
def gramatica():
    gramatica = {
        1: "P'->P", 2: "P->inicio V A", 3: "V->varincio LV", 4: "LV->D LV", 5: "LV->varfim pt_v",
        6: "D->TIPO L pt_v", 7: "L->id", 8: "TIPO->inteiro", 9: "TIPO->real", 10: "TIPO->literal",
        11: "A->ES A", 12: "ES->leia id pt_v", 13: "ES->escreva ARG pt_v", 14: "ARG->lit", 15: "ARG->num",
        16: "ARG->id", 17: "A->CMD A", 18: "CMD->id rcb LD pt_v", 19: "LD->OPRD opm OPRD", 20: "LD->OPRD",
        21: "OPRD->id", 22: "OPRD->num", 23: "A->COND A", 24: "COND->CAB CP", 25: "CAB->se ab_p EXP_R fc_p então",
        26: "EXP_R->OPRD opr OPRD", 27: "CP->ES CP", 28: "CP->CMD CP", 29: "CP->COND CP", 30: "CP->fimse",
        31: "A->R A", 32: "R->CABR CPR", 33: "CABR->repita ab_p EXP_R fc_p", 34: "CPR->ES CPR", 35: "CPR->CMD CPR",
        36: "CPR->COND CPR", 37: "CPR->fimrepita", 38: "A->fim"
    }
    return gramatica
# Follow de não terminais
def follow():
    follow = {
        "P'": 'EOF',
        "P": 'EOF',
        "V": 'leia escreva ID se repita fim',
        "LV": 'leia escreva id se repita fim',
        "D": 'inteiro real literal varfim',
        "L": 'PT_V',
        "TIPO": 'ID',
        "A": 'EOF',
        "ES": 'leia escreva ID se repita fim fimse fimrepita',
        "ARG": 'PT_V',
        "CMD": 'leia escreva ID se repita fim fimse fimrepita',
        "LD": 'PT_V',
        "OPRD": 'OPM PT_V OP FC_P',
        "COND": 'leia escreva ID se repita fim fimse fimrepita',
        "CAB": 'leia escreva ID se fimse',
        "EXP_R": 'FC_P',
        "CP": 'leia escreva ID se repita fim fimse fimrepita',
        "R": 'leia escreva ID se repita fim',
        "CABR": 'leia escreva ID se fimrepita',
        "CPR": 'leia escreva ID se repita fim'
    }
    return follow