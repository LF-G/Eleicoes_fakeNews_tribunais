''' Este programa verifica se as datas associadas aos processos no arquivo
"2021.03.29 - Mapeamento_453.xlsx" estão corretas. Caso haja algum erro,
imprime o cnj do processo em que o erro ocorre.                        '''


import xlrd
import xlsxwriter


def main ():

    arquivo1 = xlrd.open_workbook ("2021.03.29 - Mapeamento_453.xlsx", "r")
    planilha1 = arquivo1.sheet_by_index (0)       

    arquivo2 = xlrd.open_workbook ("2021.02.25 - Filtragem.xlsx")
    planilha2 = arquivo2.sheet_by_index (0)

    i = 1
    while (i < planilha1.nrows):
        cnj1 = planilha1.cell_value (rowx = i, colx = 2)
        data1 = planilha1.cell_value (rowx = i, colx = 3)        
        
        j = 1
        while (j < planilha2.nrows):
            k = 0
            cnj2 = planilha2.cell_value (rowx = i, colx = 4)
            if (cnj1 == cnj2):
                data2 = planilha2.cell_value (rowx = i, colx = 5)
                if (data1 != data2):
                    print ("Erro!")
                    print (cnj1)
                    print (cnj2)

            j = j + 1

        i = i + 1

    
main ()
