# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 11:01:12 2020

@author: claud
"""
from Bio.Align.Applications import ClustalwCommandline
from Bio import Phylo

class AlinhamentoMultiplo:

    def __init__(self, seq_input):
        self.seq_input = seq_input
        self.diretoria = r'C:\Program Files (x86)\ClustalW2\clustalw2.exe'

    def alinhamento_multiplo(self):
        clustalw_cline = ClustalwCommandline(self.diretoria, infile = self.seq_input)
        clustalw_cline()

    def get_diretoria(self): 
        return self.diretoria
    
    def set_diretoria(self,nova_diretoria):
        self.diretoria = nova_diretoria

        

class Filogenia:
    
    def __init__(self, input_file):
        self.__input_file = input_file
        
    def ArvoreFilo(self):
        tree = Phylo.read(self.__input_file, 'newick')
        Phylo.draw_ascii(tree)


