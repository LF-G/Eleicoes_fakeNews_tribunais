''' Este programa recebe uma tabela (em formato xlsx) com as partes
dos processos da base e cria um arquivo com os nomes das partes pa-
dronizados".                                                    '''


# -*- encoding: utf-8 -*-

import xlrd
import xlsxwriter
from unidecode import unidecode


def escreveCabecalho (planilha, novaPlanilha):
    k = 0
    while (k < planilha.ncols):
        variavel = planilha.cell_value (rowx = 0, colx = k)
        novaPlanilha.write (0, k, variavel)
        k = k + 1


''' Copia todo o conteúdo da linha não cabeçalho i, exceto o conteúdo
da coluna "parte".                                           '''

def copiaLinha (i, planilha, novaPlanilha):
    k = 1
    while (k < planilha.ncols):
        variavel = planilha.cell_value (rowx = i, colx = k)
        novaPlanilha.write (i, k, variavel)
        k = k + 1    


def main ():
    arquivo = xlrd.open_workbook ("2021.04.08 - Partes.xlsx", "r")
    planilha = arquivo.sheet_by_index (0)

    novoArquivo = xlsxwriter.Workbook ("2021.04.08 - Partes padro(2).xlsx")
    novaPlanilha = novoArquivo.add_worksheet ("Partes")

    escreveCabecalho (planilha, novaPlanilha)

    i = 1    
    while (i < planilha.nrows):
        nome = planilha.cell_value (rowx = i, colx = 0)
        novo_nome = unidecode (nome)
        novo_nome = novo_nome.upper ()
        copiaLinha (i, planilha, novaPlanilha)
        novaPlanilha.write (i, 0, novo_nome)
        i = i + 1

    novoArquivo.close ()        

main ()
