#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 15:45:06 2020

@author: anabarbosa
"""
from cmd import *
from GetID import GetID
from Blast import Blastp, Blastn
from SaveSequence import SaveSequence
from Analise import AnaliseLiteratura, AnaliseGene, AnaliseProt
from ProcuraHomologia import ProcuraHomologia
from AlinhamentoMultiplo import AlinhamentoMultiplo, Filogenia

class LabShell(Cmd):
    
    intro = ''' \n Comandos do LabShell:
 ---------------------------------------------------------------------------------------------------------------------            
|    literatura -> literatura para os genes em estudo                                                                 |
|    guardar_gene_fasta -> guardar os genes em formato fasta                                                          |
|    guardar_gene_GenBank -> guardar os genes em formato GenBank                                                      |
|    guardar_proteina -> guardar a proteína codoficada pelo gene em formato fasta                                     |
|    analise_gene -> permite aceder e guardar as informações do gene                                                  |
|    analise_proteina -> permite aceder e guardar as informações da proteína codificada por um gene                   |
|    blastn <file_input file_output database> -> efetua o blast para determinado gene                                 |
|    blastp <file_input file_output database> -> efetua o blast para determinada proteína                             |
|    homologia <file_input> -> verifica a existência de sequências homologas por análise dos resultados do Blast      |
|    alinhamento_multiplo <file_input> -> efetua o alinhamento múltiplo de sequências homologas                       |
|    arvore_filogenetica <file_input> -> efetua a construção da árvore filogenética                                   |                                                                                               
|    sair -> fecha o programa                                                                                         |
|                                                                                                                     |
|                Prima < ? comando > para mais informações acerca do comando                                          |
 ---------------------------------------------------------------------------------------------------------------------
 '''
    prompt = 'Lab > '
    
    def do_literatura(self, arg):
        '''Permite consultar os 10 artigos mais relevantes da base de dados PubMed para a pesquisa pretendida. '''
        try:
            option = int(input('Selecione o número correspondente ao gene a analisar: \n1 -> SOX10 \
                               \n2 -> ZEB2 \n3 -> TFAP2 \n Opção: '))
            
            if option==1:
                gene = AnaliseLiteratura('SOX10 AND Melanoma AND humans')
            elif option==2:
                gene = AnaliseLiteratura('ZEB2 AND Melanoma AND humans')
            elif option==3:
                gene = AnaliseLiteratura('TFAP2 AND Melanoma AND humans')
            else:
                print('Opção inválida.')
        
            gene.analise_literatura()
            
        except:
            print('Ocorreu um erro. Não foi possível efetuar a análise da literatura.')
    
    def do_guardar_gene_fasta(self, arg):
        ''' Permite guardar o gene selecionado em formato FASTA. '''
        try:              
            option = int(input('Selecione o número correspondente ao gene a guardar: \n1 -> SOX10 \
                               \n2 -> ZEB2 \n3 -> TFAP2 \n Opção: '))
            
            if option==1:
                geneID = GetID('SOX10')
                SOX10_ID = geneID.SOX10_ID()
                geneSeq = SaveSequence(SOX10_ID)
                geneSeq.SOX10_fasta()
                
            elif option==2:
                geneID = GetID('ZEB2')
                ZEB2_ID = geneID.ZEB2_ID()
                geneSeq = SaveSequence(ZEB2_ID)
                geneSeq.ZEB2_fasta()
                
            elif option==3:
                geneID = GetID('TFAP2')
                TFAP2_ID = geneID.TFAP2_ID()
                geneSeq = SaveSequence(TFAP2_ID)
                geneSeq.TFAP2_fasta()
                
            else:
                print('Opção inválida.')
                            
        except:
            print('Ocorreu um erro. Não foi possível guardar o gene.')
    
    def do_guardar_gene_GenBank(self, arg):
        ''' Permite guardar o gene selecionado em formato GenBank. '''
        try:              
            option = int(input('Selecione o número correspondente ao gene a guardar: \n1 -> SOX10 \
                               \n2 -> ZEB2 \n3 -> TFAP2 \n Opção: '))
            
            if option==1:
                geneID = GetID('SOX10')
                SOX10_ID = geneID.SOX10_ID()
                geneSeq = SaveSequence(SOX10_ID)
                geneSeq.SOX10_GenBank()
                
            elif option==2:
                geneID = GetID('ZEB2')
                ZEB2_ID = geneID.ZEB2_ID()
                geneSeq = SaveSequence(ZEB2_ID)
                geneSeq.ZEB2_GenBank()
                
            elif option==3:
                geneID = GetID('TFAP2')
                TFAP2_ID = geneID.TFAP2_ID()
                geneSeq = SaveSequence(TFAP2_ID)
                geneSeq.TFAP2_GenBank()
                
            else:
                print('Opção inválida.')
                            
        except:
            print('Ocorreu um erro. Não foi possível guardar o gene.')
        
    def do_guardar_proteina(self, arg):
        ''' Permite guardar a proteína codificada pelo gene selecionado em formato fasta. '''
        try:
            option = int(input('Selecione o número correspondente ao gene a guardar: \n1 -> SOX10 \
                               \n2 -> ZEB2 \n3 -> TFAP2 \n Opção: '))
            
            if option==1:
                geneID = GetID('SOX10')
                SOX10_ID = geneID.SOX10_NCBIprotein()
                geneSeq = SaveSequence(SOX10_ID)
                geneSeq.SOX10_protein()
                
            elif option==2:
                geneID = GetID('ZEB2')
                ZEB2_ID = geneID.ZEB2_NCBIprotein()
                geneSeq = SaveSequence(ZEB2_ID)
                geneSeq.ZEB2_protein()
                
            elif option==3:
                geneID = GetID('TFAP2')
                TFAP2_ID = geneID.TFAP2_NCBIprotein()
                geneSeq = SaveSequence(TFAP2_ID)
                geneSeq.TFAP2_protein()
                
            else:
                print('Opção inválida.')
                            
        except:
            print('Ocorreu um erro. Não foi possível guardar a proteína.')
        
    def do_analise_gene(self, arg):
        ''' Permite aceder ás informações disponibilizadas pelo NCBI em formato GenBank de um gene. '''
        try:
            option = int(input('Selecione o número correspondente ao gene a analisar: \n1 -> SOX10 \
                               \n2 -> ZEB2 \n3 -> TFAP2 \n Opção: '))
            
            if option==1:
                geneID = GetID('SOX10')
                SOX10_ID = geneID.SOX10_ID()
                SeqAnalise = AnaliseGene(SOX10_ID)
                SeqAnalise.NCBI_nucleotide()

            elif option==2:
                geneID = GetID('ZEB2')
                ZEB2_ID = geneID.ZEB2_ID()
                SeqAnalise = AnaliseGene(ZEB2_ID)
                SeqAnalise.NCBI_nucleotide()
                
            elif option==3:
                geneID = GetID('TFAP2')
                TFAP2_ID = geneID.TFAP2_ID()
                SeqAnalise = AnaliseGene(TFAP2_ID)
                SeqAnalise.NCBI_nucleotide()
                
            else:
                print('Opção inválida.')
        
        except:
            print('Ocorreu um erro. Não foi possível efetuar a análise do gene.')
    
    def do_blastn(self, arg):
        ''' Efetua o blastn de determinado gene exportando a informação para um ficheiro em formato xml. 
 Para o correto funcionamento, introduza, pela seguinte ordem:
     - O ficheiro com a sequência em formato fasta para efetuar blast;
     - O nome do ficheiro em formato .xml de output;
     - A base de dados (por default é 'nr').
 '''
        try:
            args = arg.split(' ')
            if len(args)==3:
                input_file = args[0]
                output_file = args[1]
                database = args[2]
                blast_protein = Blastn(input_file,output_file,database)
                blast_protein.blastn()
            elif len(args)==2:
                input_file = args[0]
                output_file = args[1]
                blast_protein = Blastn(input_file,output_file)
                blast_protein.blastn()
            else:
                print('Número de argumentos inválido.')
        except:
            print('Ocorreu um erro. Não foi possível executar o Blastn.')
    
    def do_blastp(self, arg):
        ''' Efetua o blastp de determinada proteína exportando a informação para um ficheiro em formato xml. 
 Para o correto funcionamento, introduza, pela seguinte ordem:
     - O ficheiro com a sequência em formato fasta para efetuar blast;
     - O nome do ficheiro em formato .xml de output;
     - A base de dados (por default é 'nr').
 '''
        try:
            args = arg.split(' ')
            if len(args)==3:
                input_file = args[0]
                output_file = args[1]
                database = args[2]
                blast_protein = Blastp(input_file,output_file,database)
                blast_protein.blastp()
            elif len(args)==2:
                input_file = args[0]
                output_file = args[1]
                blast_protein = Blastp(input_file,output_file)
                blast_protein.blastp()
            else:
                print('Número de argumentos inválido.')
        except:
            print('Ocorreu um erro. Não foi possível executar o Blastp.')
        
    def do_homologia(self, arg):
        ''' Verifica a existência de sequencias homologas e caso se verifique a sua existência, gera um ficheiro com essas sequencias. 
 Para o correto funcionamento, introduza o ficheiro xml com o resultado do Blast.
 Atenção: Considera-se como critério para definir homologia sequências com e-value inferior a 0.001.
 '''
        try:
            args = arg.split(' ')
            if len(args)==1:
                input_file = args[0]
                ficheiro_xml = ProcuraHomologia(input_file)
                ficheiro_xml.procura()
            else:
                print('Número de argumentos inválido.')
        except:
            print('Ocorreu um erro. Não foi possível executar a procura de Homologia.')
        
    def do_analise_proteina(self, arg):
        ''' Tendo por base o nome do gene, identifica e analisa uma determinada proteína codificada por esse.'''
        try:
            option = int(input('Selecione o número correspondente ao gene a analisar: \n1 -> SOX10 \
                               \n2 -> ZEB2 \n3 -> TFAP2 \n Opção: '))
            
            if option==1:
                geneID = GetID('SOX10')
                SOX10_ID = geneID.SOX10_Uniprot()
                prot = AnaliseProt(SOX10_ID)
                prot.Uniprot_records()
                prot.prot_info()

            elif option==2:
                geneID = GetID('ZEB2')
                ZEB2_ID = geneID.ZEB2_Uniprot()
                prot = AnaliseProt(ZEB2_ID)
                prot.Uniprot_records()
                prot.prot_info()
                
            elif option==3:
                geneID = GetID('TFAP2')
                TFAP2_ID = geneID.TFAP2_Uniprot()
                prot = AnaliseProt(TFAP2_ID)
                prot.Uniprot_records()
                prot.prot_info()
                
            else:
                print('Opção inválida.')
        except:
            print('Ocorreu um erro. Não foi possível analisar a proteína.')
        
    def do_alinhamento_multiplo(self, arg):
        ''' Tendo por base um ficheiro de sequências homologas, efetua o alinhamento múltiplo das sequências. 
 Para o correto funcionamento, introduza um ficheiro com sequências homologas resultantes do Blast.
 '''
        try:
            seqs = AlinhamentoMultiplo(arg)
            seqs.alinhamento_multiplo()
        except:
            print('Ocorreu um erro. Não foi possível efetuar o alinhamento múltiplo.')
        
    def do_arvore_filogenetica(self,arg):
        ''' Tendo por base um ficheiro de alinhamento multiplo, em formato .dnd constrói uma árvore filogenética. 
 Para o correto funcionamento, introduza um ficheiro resultante do alinhamento múltiplo.
 '''
        try:
            align = Filogenia(arg)
            align.ArvoreFilo()
        except:
            print('Ocorreu um erro. Não foi possível efetuar a construção da árvore filogenética.')
            
    def do_menu(self, arg):
        print(self.intro)
    
    def do_sair(self, arg):
        print('Obrigado por utilizar o LabShell!')
        return True
        
if __name__=='__main__':
    LabShell().cmdloop()
    
    
    
    
    
