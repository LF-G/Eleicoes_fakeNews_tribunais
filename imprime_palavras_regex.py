# -*- coding: utf-8 -*-

'''

    Este programa analisa os processos da pasta de decisões e constrói uma 
tabela intitulada Resultados_palavras.xlsx que contém todas as palavras que
estão nos processos e que casam com cada uma das seguintes expressões regulares:
    - (fake\s?.*?)\W
    - \W(sabidament.{,20}inver.dic.*?)\W
    - \bfato.{,20}inver.dic\w*|\bfato.{,20}fals\w*|\bnot.cia.{,20}inver.dic\w*|
    \bnot.cia.{,20}fals\w*|\bnot.cia.{,20}fraudulent\w*|\bnot.cia.{,20}enganos\w*|
    \bmat.ria.{,20}inver.dic\w*|\bmat.ria.{,20}fals\w*|\bmat.ria.{,20}fraudulent\w*|
    \bconte.do.{,20}inver.dic\w*|\bconte.do.{,20}fals\w*|\bconte.do.{,20}fraudulent\w*|
    \bconte.do.{,20}enganos\w*|\binforma.{,20}inver.dic\w*|\binforma.{,20}fals\w*|
    \binforma..{,20}fraudulent\w*|\binforma..{,20}enganos\w*|\bsabidament.{,20}fals\w*|
    \bsabidament.{,20}enganos\w*
    - (desinform.*?)\W
    - \bcal[uú]ni[aeiou]\w* (grupo calúnia/calunios_)
    - \binj[uú]ri[aeiou]\w* (grupo injúria/injurios_)
    - \bdifam\w* (grupo difamação/difamatóri_)    
    - \bofen[sd]\w* (grupo ofensiv_, ofensa)
    - \bpropagandas?.{,15}irregulare?s?
    - \bpropagandas?.{,15}negativas?
    - \bfidedig.{,20} inform.*?\b|\binform.{,20} fidedig.*?\b

'''



import os
import time
import re
import xlsxwriter
from urllib.request import urlopen
from bs4 import BeautifulSoup


''' Retorna 1 se "string" estiver em "novaLista" e 0 caso contrário.    '''

def estaNaNovaLista (string, novaLista):
    i = 0
    while (i < len (novaLista)):
        if (string == novaLista[i]):
            return 1
        i = i + 1
    
    return 0


''' Recebe "lista" e devolve uma "novaLista", uma lista que contém os mesmos
elementos de lista, mas sem repetições.                                  '''

def monta (lista):
    novaLista = []
    i = 0
    while (i < len (lista)):
        if (estaNaNovaLista (lista[i], novaLista) == 0):
            novaLista.append (lista[i])
        i = i + 1
    
    return novaLista


def main ():
    camDirAtual = os.getcwd ()
    camDirJurisdicoes = camDirAtual + "/2021.07.05 - decisoes_444"
    
    novoArquivo = xlsxwriter.Workbook ("Resultados_palavras.xlsx")
    novaPlanilha = novoArquivo.add_worksheet ("Resultados")
    
    fakeFinal = []
    sabInverFinal = []
    inverFinal = []
    desinfFinal = []
    calunFinal = []
    injurFinal = []
    difamFinal = []
    ofensFinal = []
    propIrregFinal = []
    propNegFinal = []
    fidedigInfoFinal = []

    cont = 0

    ''' Jurisdições '''
    listaJurisdicoes = os.listdir (camDirJurisdicoes)
    for i in range (len (listaJurisdicoes)):
        caminhoJurisdicaoAtual = camDirJurisdicoes + "/" + listaJurisdicoes[i]        
    
        ''' Números de processos '''
        listaProcessos = os.listdir (caminhoJurisdicaoAtual)
        for j in range (len (listaProcessos)):
            cont = cont + 1
            caminhoProcessoAtual = caminhoJurisdicaoAtual + "/" + listaProcessos[j]
            listaArquivos = os.listdir (caminhoProcessoAtual)        
            
            ''' arquivos de um processo '''
            for k in range (len (listaArquivos)):
                caminhoArquivoAtual = caminhoProcessoAtual + "/" + listaArquivos[k]
                print (caminhoArquivoAtual)                
            
                html = urlopen ("file:///" + caminhoArquivoAtual)
                res = BeautifulSoup (html.read (), "html5lib")
                texto = res.get_text ()
            
                fake = re.findall (r"(fake\s?.*?)\W", texto)
                sabInver = re.findall (r"\W(sabidament.{,20}inver.dic.*?)\W", texto)
                inver = re.findall (r"\bfato.{,20}inver.dic\w*|\bfato.{,20}fals\w*|\bnot.cia.{,20}inver.dic\w*|\bnot.cia.{,20}fals\w*|\bnot.cia.{,20}fraudulent\w*|\bnot.cia.{,20}enganos\w*|\bmat.ria.{,20}inver.dic\w*|\bmat.ria.{,20}fals\w*|\bmat.ria.{,20}fraudulent\w*|\bconte.do.{,20}inver.dic\w*|\bconte.do.{,20}fals\w*|\bconte.do.{,20}fraudulent\w*|\bconte.do.{,20}enganos\w*|\binforma.{,20}inver.dic\w*|\binforma.{,20}fals\w*|\binforma..{,20}fraudulent\w*|\binforma..{,20}enganos\w*|\bsabidament.{,20}fals\w*|\bsabidament.{,20}enganos\w*", texto)
                desinf = re.findall (r"(desinform.*?)\W", texto)
                calun = re.findall (r"\bcal[uú]ni[aeiou]\w*", texto)
                injur = re.findall (r"\binj[uú]ri[aeiou]\w*", texto)  
                difam = re.findall (r"\bdifam\w*", texto)
                ofens = re.findall (r"\bofen[sd]\w*", texto)
                propIrreg = re.findall (r"\bpropagandas?.{,15}irregulare?s?", texto)
                propNeg = re.findall (r"\bpropagandas?.{,15}negativas?", texto)
                fidedigInfo = re.findall (r"\bfidedig.{,20} inform.*?\b|\binform.{,20} fidedig.*?\b", texto)

                fakeFinal = fakeFinal + fake
                sabInverFinal = sabInverFinal + sabInver
                inverFinal = inverFinal + inver
                desinfFinal = desinfFinal + desinf
                calunFinal = calunFinal + calun
                injurFinal = injurFinal + injur
                difamFinal = difamFinal + difam
                ofensFinal = ofensFinal + ofens
                propIrregFinal = propIrregFinal + propIrreg
                propNegFinal = propNegFinal + propNeg
                fidedigInfoFinal = fidedigInfoFinal + fidedigInfo

    novaPlanilha.write (0, 0, "fake")
    montaFake = monta (fakeFinal)
    i = 0
    while (i < len (montaFake)):       
        print (montaFake[i])
        novaPlanilha.write (i + 1, 0, montaFake[i])
        i = i + 1
    print (" ")

    novaPlanilha.write (0, 1, "sab_inver")
    montaSabInver = monta (sabInverFinal)
    i = 0
    while (i < len (montaSabInver)):       
        print (montaSabInver[i])
        novaPlanilha.write (i + 1, 1, montaSabInver[i])
        i = i + 1
    print (" ")
    
    novaPlanilha.write (0, 2, "inver_amplo")
    montaInver = monta (inverFinal)
    i = 0
    while (i < len (montaInver)):       
        print (montaInver[i])
        novaPlanilha.write (i + 1, 2, montaInver[i])
        i = i + 1
    print (" ")

    novaPlanilha.write (0, 3, "desinformacao")    
    montaDesinf = monta (desinfFinal)
    i = 0
    while (i < len (montaDesinf)):       
        print (montaDesinf[i])
        novaPlanilha.write (i + 1, 3, montaDesinf[i])
        i = i + 1
    print (" ")                
            
    novaPlanilha.write (0, 4, "calunia")  
    montaCalun = monta (calunFinal)
    i = 0
    while (i < len (montaCalun)):       
        print (montaCalun[i])
        novaPlanilha.write (i + 1, 4, montaCalun[i])
        i = i + 1
    print (" ")

    novaPlanilha.write (0, 5, "injuria") 
    montaInjur = monta (injurFinal)
    i = 0
    while (i < len (montaInjur)):       
        print (montaInjur[i])
        novaPlanilha.write (i + 1, 5, montaInjur[i])
        i = i + 1
    print (" ")

    novaPlanilha.write (0, 6, "difamacao") 
    montaDifam = monta (difamFinal)
    i = 0
    while (i < len (montaDifam)):       
        print (montaDifam[i])
        novaPlanilha.write (i + 1, 6, montaDifam[i])
        i = i + 1
    print (" ")

    novaPlanilha.write (0, 7, "ofensa") 
    montaOfens = monta (ofensFinal)
    i = 0
    while (i < len (montaOfens)):       
        print (montaOfens[i])
        novaPlanilha.write (i + 1, 7, montaOfens[i])
        i = i + 1
    print (" ")

    novaPlanilha.write (0, 8, "prop_irreg") 
    montaPropIrreg = monta (propIrregFinal)
    i = 0
    while (i < len (montaPropIrreg)):       
        print (montaPropIrreg[i])
        novaPlanilha.write (i + 1, 8, montaPropIrreg[i])
        i = i + 1
    print (" ")

    novaPlanilha.write (0, 9, "prop_neg") 
    montaPropNeg = monta (propNegFinal)
    i = 0
    while (i < len (montaPropNeg)):       
        print (montaPropNeg[i])
        novaPlanilha.write (i + 1, 9, montaPropNeg[i])
        i = i + 1
    print (" ")

    novaPlanilha.write (0, 10, "fidedig_info")
    montaFidedigInfo = monta (fidedigInfoFinal)
    i = 0
    while (i < len (montaFidedigInfo)):       
        print (montaFidedigInfo[i])
        novaPlanilha.write (i + 1, 10, montaFidedigInfo[i])
        i = i + 1
    print (" ")
    
    novoArquivo.close ()
    print (cont)
    
main ()
