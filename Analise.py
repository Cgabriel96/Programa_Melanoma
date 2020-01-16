#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:26:22 2020

@author: anabarbosa
"""
import requests
from Bio import Entrez, ExPASy, Seq, SeqIO, SeqRecord, SwissProt
from urllib.request import urlopen
from io import TextIOWrapper

Entrez.email = 'example@gmail.com'

class AnaliseLiteratura:
    
    def __init__(self,query):
        self.__query = query

    def analise_literatura(self):
        nome = str('_SEARCH_ ' + self.__query + '.txt')
        ficheiro = open(nome,'w')
        print('A sua pesquisa encontra-se em decurso. Por favor, aguarde.')
        gene_search = Entrez.esearch(db="pubmed", sort='relevance', retmax='10', term=self.__query, retmode="text")
        gene_read = Entrez.read(gene_search)
        gene_search.close()
        for read in gene_read['IdList']:
            article_search = Entrez.efetch(db="pubmed", id=read, rettype="fasta", retmode="text")
            article_read = article_search.read()
            article_search.close()
            ficheiro.write(article_read+'\n')
        print('Os identificadores dos artigos correspondentes á pesquisa são os seguintes: \n %s.' %(gene_read['IdList']))
        print('\nA informação acerca dos artigos encontra-se no ficheiro: %s.' %nome)
    

class AnaliseGene:
    
    def __init__(self,gene_id):
        self.__gene_id = gene_id
    
    def NCBI_nucleotide(self):
        gene = Entrez.efetch(db="nucleotide", id=self.__gene_id, retmode="text", rettype='gb')
        gene_read = SeqIO.read(gene,'genbank')
        gene.close()
        nome = str('analise_' + gene_read.name)
        ficheiro = open(nome,'w')
        dic_tipos = {}
        
        for feat in gene_read.features:
            ficheiro.write('Tipo de feature: '+ str(feat.type)+'\n')
            ficheiro.write('Localização: '+ str(feat.location)+'\n')
            ficheiro.write('Qualifiers: '+ str(feat.qualifiers) + '\n')
            ficheiro.write('\n')
            if feat.type not in dic_tipos:
                dic_tipos[feat.type] = 1
            else:
                dic_tipos[feat.type] += 1
        
        for feature_type in dic_tipos.keys():
            ficheiro.write('O gene em análise tem: ' + str(dic_tipos[feature_type]) + ' features do tipo ' + str(feature_type) + '\n')
        
        for annotation in gene_read.annotations:
            ficheiro.write('\n'+ str(annotation) + ':' + str(gene_read.annotations[annotation])+'\n')
        
        ficheiro.close()
        print('A análise do gene foi gravada com sucesso no ficheiro: %s.' %nome)
        
class AnaliseProt:
    
    def __init__(self,uniprot_id):
        self.__uniprot_id = uniprot_id
    
    
    def Uniprot_records(self):
        handle = ExPASy.get_sprot_raw(self.__uniprot_id)#ID do NCBI, para tirar ficheiro xml da Uniprot
        url = handle.url # 
        url = url.replace('txt','xml') #
        response = requests.get(url) #
        with open('Uniprot' + self.__uniprot_id + '.xml','wb') as file: #b para escrever em modo binário
            file.write(response.content)
        
        
    def prot_info(self):
        lista_ref = [] #Informação das bases de dados para o id dos genes correspondentes
        lista_PDB = [] # (PDB, id_correspondente)
        lista_id_PDB = [] #(id_correspondente)
        handle_uniprot = SeqIO.read('Uniprot' + self.__uniprot_id + '.xml','uniprot-xml') #Objeto SeqRecord com informações do xml da Uniprot
        
        file = open('Uniprot_info_'+ self.__uniprot_id + '.txt','w')# 'w para dar permissões de escrita  
    
        file.write(str(handle_uniprot.seq))
        file.write(str(handle_uniprot.features))
        
        
        try:
            file.write(str(handle_uniprot.annotations['taxonomy']))
        except:
            print('Sem informação correspondente a taxonomia ')
            
        try:
            file.write(str(handle_uniprot.annotations['comment_subcellularlocation_location']))
        except:
            print('Sem informação correspondente a localização subcelular')
        
        try:
            file.write(str(handle_uniprot.annotations['comment_PTM'])) #pos trascription modifications
        except:
            print('Sem informação correspondente a PTM')
        
        try:
            file.write(str(handle_uniprot.annotations['comment_function']))
        except: 
            print('Erro')
        
        try: 
            file.write(str(handle_uniprot.annotations['alternativeName_fullName'])) 
        except:
            print('Sem informação correspondente a nomes alternativos')
        
    
        file.write(str(handle_uniprot.dbxrefs))
        file.close()
        
        for referencia in handle_uniprot.dbxrefs:
            a = tuple(referencia.split(':'))
            lista_ref.append (a)
            
        for referencia in lista_ref:
            if referencia[0] == 'PDB':
                lista_PDB.append(referencia)
            
        for tuplo in lista_PDB: #Para obter apenas os id dos tuplos
            lista_id_PDB.append(tuplo[1])
        
        print(lista_id_PDB)






