#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 17:34:05 2020

@author: anabarbosa
"""
from Bio.Blast import NCBIWWW
from Bio import SeqIO

class Blastn:
    
    def __init__(self,input_file,output_file,database="nr"):
        self.__input_file = input_file
        self.__output_file = output_file
        self.__database = database
        
        
    def blastn(self):
        record=SeqIO.read(self.__input_file,"fasta")
        print("O gene %s foi submetida ao blastn. Por favor aguarde."%(record.id))
        ficheiro=open(self.__output_file,"w")
        blast_result = NCBIWWW.qblast("blastn", self.__database, record.format("fasta"))
        ficheiro.write(blast_result.read()+"\n")
        print("O resultado do Blastn para o gene %s encontra-se no ficheiro %s."%(record.id, self.__output_file))
        ficheiro.close()
        blast_result.close()
        
class Blastp:
    
    def __init__(self,input_file,output_file,database="nr"):
        self.__input_file = input_file
        self.__output_file = output_file
        self.__database = database
        
    def blastp(self):
        record=SeqIO.read(self.__input_file,"fasta")
        print("A proteína %s foi submetida ao blastp. Por favor aguarde."%(record.id))
        ficheiro=open(self.__output_file,"w")
        blast_result = NCBIWWW.qblast("blastp", self.__database, record.format("fasta"))
        ficheiro.write(blast_result.read()+"\n")
        print("O resultado do Blastp para a proteína %s encontra-se no ficheiro %s."%(record.id, self.__output_file))
        ficheiro.close()
        blast_result.close()
        


