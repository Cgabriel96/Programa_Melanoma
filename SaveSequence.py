 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:47:29 2020

@author: anabarbosa
"""
from Bio import Entrez, SeqIO

Entrez.email = 'example@gmail.com'


class SaveSequence:
    
    def __init__(self,id_seq):
        self.__id_seq = id_seq
        
    def SOX10_fasta(self):
        gene_fasta = Entrez.efetch(db="nucleotide", id=self.__id_seq, retmode='text', rettype='fasta')
        gene_read_fasta = SeqIO.read(gene_fasta,'fasta')
        gene_fasta.close()
        SeqIO.write(gene_read_fasta,'SOX10_fasta.txt','fasta')
        print('O ficheiro fasta do gene SOX10 foi guardado com sucesso no ficheiro: SOX10_fasta.txt')
    
    def SOX10_GenBank(self):
        gene_fasta = Entrez.efetch(db="nucleotide", id=self.__id_seq, retmode='text', rettype='gb')
        gene_read_fasta = SeqIO.read(gene_fasta,'gb')
        gene_fasta.close()
        SeqIO.write(gene_read_fasta,'SOX10_GenBank.txt','gb')
        print('O ficheiro GenBank do gene SOX10 foi guardado com sucesso no ficheiro: SOX10_GenBank.txt')
    
    def ZEB2_fasta(self):
        gene_fasta = Entrez.efetch(db="nucleotide", id=self.__id_seq, retmode='text', rettype='fasta')
        gene_read_fasta = SeqIO.read(gene_fasta,'fasta')
        gene_fasta.close()
        SeqIO.write(gene_read_fasta,'ZEB2_fasta.txt','fasta')
        print('O ficheiro fasta do gene ZEB2 foi guardado com sucesso no ficheiro: ZEB2_fasta.txt')
        
    def ZEB2_GenBank(self):
        gene_fasta = Entrez.efetch(db="nucleotide", id=self.__id_seq, retmode='text', rettype='gb')
        gene_read_fasta = SeqIO.read(gene_fasta,'gb')
        gene_fasta.close()
        SeqIO.write(gene_read_fasta,'ZEB2_GenBank.txt','gb')
        print('O ficheiro GenBank do gene ZEB2 foi guardado com sucesso no ficheiro: ZEB2_GenBank.txt')
        
    def TFAP2_fasta(self):
        gene_fasta = Entrez.efetch(db="nucleotide", id=self.__id_seq, retmode='text', rettype='fasta')
        gene_read_fasta = SeqIO.read(gene_fasta,'fasta')
        gene_fasta.close()
        SeqIO.write(gene_read_fasta,'TFAP2_fasta.txt','fasta')
        print('O ficheiro fasta do gene TFAP2 foi guardado com sucesso no ficheiro: TFAP2_fasta.txt')
        
    def TFAP2_GenBank(self):
        gene_fasta = Entrez.efetch(db="nucleotide", id=self.__id_seq, retmode='text', rettype='gb')
        gene_read_fasta = SeqIO.read(gene_fasta,'gb')
        gene_fasta.close()
        SeqIO.write(gene_read_fasta,'TFAP2_GenBank.txt','gb')
        print('O ficheiro GenBank do gene TFAP2 foi guardado com sucesso no ficheiro: TFAP2_GenBank.txt')

    def SOX10_protein(self):
        gene_fasta = Entrez.efetch(db="protein", id=self.__id_seq, retmode='text', rettype='fasta')
        gene_read_fasta = SeqIO.read(gene_fasta,'fasta')
        gene_fasta.close()
        SeqIO.write(gene_read_fasta,'SOX10_protein.txt','fasta')
        print('A proteína cujo gene SOX10 codifica foi guardada com sucesso no ficheiro: SOX10_protein.txt')

    def ZEB2_protein(self):
        gene_fasta = Entrez.efetch(db="protein", id=self.__id_seq, retmode='text', rettype='fasta')
        gene_read_fasta = SeqIO.read(gene_fasta,'fasta')
        gene_fasta.close()
        SeqIO.write(gene_read_fasta,'ZEB2_protein.txt','fasta')
        print('A proteína cujo gene ZEB2 codifica foi guardada com sucesso no ficheiro: ZEB2_protein.txt')

    def TFAP2_protein(self):
        gene_fasta = Entrez.efetch(db="protein", id=self.__id_seq, retmode='text', rettype='fasta')
        gene_read_fasta = SeqIO.read(gene_fasta,'fasta')
        gene_fasta.close()
        SeqIO.write(gene_read_fasta,'TFAP2_protein.txt','fasta')
        print('A proteína cujo gene TFAP2 codifica foi guardada com sucesso no ficheiro: TFAP2_protein.txt')
