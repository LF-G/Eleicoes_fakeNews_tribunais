'''
Autor: Luiz Fernando Antonelli Galati
'''

'''
    Para cada um dos processos judiciais da pasta "Decisoes", este script imprime, numa tabela
em formato xlsx:
   
    - o número do processo;
    - a jurisdição do processo;
    - a quantidade de arquivos existentes no processo;
    - a frequência com que ocorrem, no processo, palavras do grupo "sabidamente inverídico";
    - a média, por arquivo do processo, de ocorrência de palavras do grupo "sabidamente inverídico";
    - a frequência com que no processo ocorrem palavras do grupo "ofens-";
    - a média, por arquivo do processo, de ocorrência de palavras do grupo "ofens-".
'''


# -*- coding: utf-8 -*-

import os
import time
import re
import xlsxwriter
from urllib.request import urlopen
from bs4 import BeautifulSoup

w = xlsxwriter.Workbook ("frequencias-3.xlsx")
ws = w.add_worksheet ("frequencias")
ws.write (0, 0, "jurisdicao")
ws.write (0, 1, "numero_processo")
ws.write (0, 2, "num_arquivos_processo")
ws.write (0, 3, "freq_sabidamente")
ws.write (0, 4, "media_por_arquivo_sabidamente")
ws.write (0, 5, "freq_ofens")
ws.write (0, 6, "media_por_arquivo_ofens")

camDirAtual = os.getcwd ()
camDirJurisdicoes = camDirAtual + "/Decisoes"

cont = 0
''' Jurisdições '''
listaJurisdicoes = os.listdir (camDirJurisdicoes)

for i in range (len (listaJurisdicoes)):
    caminhoJurisdicaoAtual = camDirJurisdicoes + "/" + listaJurisdicoes[i]
    
    ''' Números de processos '''
    listaProcessos = os.listdir (caminhoJurisdicaoAtual)
    for j in range (len (listaProcessos)):
        cont += 1
        caminhoProcessoAtual = caminhoJurisdicaoAtual + "/" + listaProcessos[j]
        listaArquivos = os.listdir (caminhoProcessoAtual)
        
        sabidFinal = []
        ofensFinal = []
        contArquivos = 0
        ''' arquivos de um processo '''
        for k in range (len (listaArquivos)):
            caminhoArquivoAtual = caminhoProcessoAtual + "/" + listaArquivos[k]
#           print (caminhoArquivoAtual)
            contArquivos += 1
            
            html = urlopen ("file:///" + caminhoArquivoAtual)
            res = BeautifulSoup (html.read (), "html5lib")
            texto = res.get_text ()
            
            sabid = re.findall (r"\W(sabidament.{,20}inver.dic.*?)\W", texto)
            ofens = re.findall (r"\b[Oo][Ff][Ee][Nn][Ss]\w*", texto)
            
            sabidFinal = sabidFinal + sabid
            ofensFinal = ofensFinal + ofens
            
        mediaSabid = (len (sabidFinal))/(contArquivos)
        mediaOfens = (len (ofensFinal))/(contArquivos)
        
        ws.write (cont, 0, listaJurisdicoes[i])
        ws.write (cont, 1, listaProcessos[j])
        ws.write (cont, 2, contArquivos)
        ws.write (cont, 3, len (sabidFinal))
        ws.write (cont, 4, mediaSabid)
        ws.write (cont, 5, len (ofensFinal))
        ws.write (cont, 6, mediaOfens)
    
w.close ()
