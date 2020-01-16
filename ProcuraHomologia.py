#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:48:49 2020

@author: anabarbosa
"""

from Bio.Blast import NCBIXML

class ProcuraHomologia:
    
    def __init__(self,ficheiro_input):
        self.__ficheiro_input = ficheiro_input
        
    def procura(self):
        e_value = 0.001
        args = self.__ficheiro_input.split('.')
        file=args[0]
        ficheiro_xml = open(self.__ficheiro_input,'r')
        nome = str('SeqsHomologas_' + str(file) + '.fasta')
        ficheiro_output = open(nome,'w')
        blast_records = NCBIXML.read(ficheiro_xml)
        for alignment in blast_records.alignments:
            for hsp in range(len(alignment.hsps)):
                if alignment.hsps[hsp].expect < e_value:
                    if hsp != 0:
                        ficheiro_output.write('>'+alignment.hit_id+'_'+str(hsp)+'\n'+alignment.hsps[hsp].sbjct+'\n')
                    else:
                        ficheiro_output.write('>'+alignment.hit_id+'\n'+alignment.hsps[hsp].sbjct+'\n')
        ficheiro_output.close()
        print('Ficheiro %s que contém as sequencias homologas gravado com sucesso.' %nome)
                        

