''' Este programa recebe o arquivo "2021.02.25 - Filtragem.xlsx" e copia para o
arquivo "2021.03.29 - Mapeamento_453.xlsx" todas as linhas que não são duplo-sim
(ou seja, todas linhas que não são "Sim" para "verd_online" e "Sim" para "verd_desinf").
                                                                                '''

import xlrd
import xlsxwriter


''' Copia a linha i da planilha para a linha j da novaPlanilha.                 '''

def copiaLinha (i, planilha, j, novaPlanilha):
    k = 0
    while (k < planilha.ncols):
        conteudo = planilha.cell_value (rowx = i, colx = k)
        novaPlanilha.write (j, k, conteudo)
        k = k + 1


def main ():

    arquivo1 = xlrd.open_workbook ("2021.03.29 - Mapeamento_453.xlsx", "r")
    planilha1 = arquivo1.sheet_by_index (0)
    
    arquivo2 = xlrd.open_workbook ("2021.04.06 - Partes.xlsx", "r")
    planilha2 = arquivo2.sheet_by_index (2)      

    novoArquivo = xlsxwriter.Workbook ("2021.04.08 - Partes.xlsx")
    novaPlanilha = novoArquivo.add_worksheet ("Partes")
    
    copiaLinha (0, planilha2, 0, novaPlanilha)
    novaPlanilha.write (0, 38, "classe_judicial")

    i = 1

    while (i < planilha2.nrows):
        cnj2 = planilha2.cell_value (rowx = i, colx = 6)
        
        j = 1
        while (j < planilha1.nrows):           
            cnj1 = planilha1.cell_value (rowx = j, colx = 2)
            
            if (cnj2 == cnj1):
                classe_judicial = planilha1.cell_value (rowx = j, colx = 8)

            j = j + 1
        

       
        copiaLinha (i, planilha2, i, novaPlanilha)
        novaPlanilha.write (i, 38, classe_judicial)
        
        i = i + 1      
   
    novoArquivo.close ()
    
main ()
