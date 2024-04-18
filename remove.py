# -*- coding: utf-8 -*-
'''
    Este programa remove da pasta "Base de 2021.02.25" os processos descritos na tabela
"Lista de processos irrelevantes.xlsx".
    Para que tudo funcione corretamente, este arquivo deve estar na mesma pasta em
que estão a tabela e o diretório "Base de 2021.02.25".                              '''

import xlrd
import os

arquivo = xlrd.open_workbook ("Lista de processos irrelevantes.xlsx", "r")
planilha = arquivo.sheet_by_index (0)

diretorioAtual = os.getcwd ()

i = 1
while (i < planilha.nrows):
    id = planilha.cell_value (rowx = i, colx = 0)
    jurisdicao = planilha.cell_value (rowx = i, colx = 1)
    cnj = planilha.cell_value (rowx = i, colx = 2)

    id = int (id)
    id = str (id)
    if (len (id) == 3):
        id = "000" + id
    if (len (id) == 4):
        id = "00" + id
    elif (len (id) == 5):
        id = "0" + id
    
    print (id)
    
    dirARemover = diretorioAtual + "/Base de 2021.02.25" + "/" + jurisdicao + "/" + id + " - " + jurisdicao + " - " + cnj
    print (dirARemover)
    
    list = os.listdir (dirARemover)
    for j in range (len (list)):
        caminhoArquivo = dirARemover + "/" + list[j]
        os.remove (caminhoArquivo)
        
    os.rmdir (dirARemover)
    
    i = i + 1

print (" ")
print (i)
print (" ")
