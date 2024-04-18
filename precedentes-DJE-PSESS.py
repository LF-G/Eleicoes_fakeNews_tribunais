''' Este programa vasculha a pasta de processos dos TREs em busca de precedentes que citam as
expressões DJE, Diário Eletrônico de Justiça, PSESS, Publicado em Sessão, etc. Imprime o re-
sultado em um arquivo intiulado "precedentes-DJE-PSESS". Esse arquivo é uma lista em que 
cada linha contém (I) um precedente e (II) o CNJ e a jurisdição do processo em que esse pre-
cedente aparece.                                                                         '''



# -*- coding: utf-8 -*-

import os
import time
import re
import xlsxwriter
from urllib.request import urlopen
from bs4 import BeautifulSoup


''' Escreve um cabeçalho na planilha "planilha" '''

def escreveCabecalho (planilha):
    planilha.write (0, 0, "CNJ")
    planilha.write (0, 1, "Jurisdição")
    planilha.write (0, 2, "Precedente") 
  
    
''' Recebe o caminho da pasta de um processo e retorna a lista de artigos desse processo.                                                                            '''

def montaListaPrecedentesProcesso (caminhoProcesso):
    listaArquivos = os.listdir (caminhoProcesso)
    listaArquivos.sort ()    
    lista_precedentes_processo = []
    
    for k in range (len (listaArquivos)):
        caminhoArquivoAtual = caminhoProcesso + "/" + listaArquivos[k]
        print (caminhoArquivoAtual + "\n")
            
        html = urlopen ("file:///" + caminhoArquivoAtual)
        res = BeautifulSoup (html.read (), "html5lib")        
        
        for paragrafo in res.findAll ("p"):
            texto = paragrafo.text
            lista_precedentes_paragrafo = re.findall (r".{,150}[Pp][Ss][Ee][Ss][Ss].{,110}|.{,150}[Dd]J[Ee].{,110}|.{,150}[Dd]i[aá]rio d[ae] [Jj]usti[cç]a [Ee]letr[ôo]nic[ao].{,110}|.{,150}[Pp]ublicado [Ee]m [Ss]essão.{,110}|.{,150}[Dd]E[Jd].{,110}|.{150}[Dd]i[aá]rio [Ee]letrônic[ao] d[ae] [Jj]usti[cç]a.{110}|.{,150}[D][Jj].{,110}|.{,150}[Dd]i[áa]rio d[ae] [Jj]usti[çc]a.{,110}", texto)
            lista_precedentes_processo = lista_precedentes_processo + lista_precedentes_paragrafo
        
    return lista_precedentes_processo


def main ():
    inicio = time.time ()

    camDirAtual = os.getcwd ()
    camDirJurisdicoes = camDirAtual + "/2021.03.29 - decisoes_453"

    novoArquivo = xlsxwriter.Workbook ("precedentes-DJE-PSESS.xlsx")
    novaPlanilha = novoArquivo.add_worksheet ("precedentes-DJE-PSESS")
    escreveCabecalho (novaPlanilha)

    ultimaLinhaImpressa = 0
    
    ''' Jurisdições '''
    listaJurisdicoes = os.listdir (camDirJurisdicoes)
    listaJurisdicoes.sort ()
    for i in range (len (listaJurisdicoes)):
        caminhoJurisdicaoAtual = camDirJurisdicoes + "/" + listaJurisdicoes[i]    
        
        ''' Números de processos '''
        listaProcessos = os.listdir (caminhoJurisdicaoAtual)
        listaProcessos.sort ()
        for j in range (len (listaProcessos)):               
            caminhoProcessoAtual = caminhoJurisdicaoAtual + "/" + listaProcessos[j]
            lista_artigos_processo = montaListaPrecedentesProcesso (caminhoProcessoAtual)

            k = 0
            while (k < len (lista_artigos_processo)):
                novaPlanilha.write (ultimaLinhaImpressa + 1, 0, listaProcessos[j])
                novaPlanilha.write (ultimaLinhaImpressa + 1, 1, listaJurisdicoes[i])
                novaPlanilha.write (ultimaLinhaImpressa + 1, 2, lista_artigos_processo[k])
                ultimaLinhaImpressa = ultimaLinhaImpressa + 1
                k = k + 1       

 
    novoArquivo.close ()

    fim = time.time ()
    print (fim - inicio)

main ()
