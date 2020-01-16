#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:43:23 2020

@author: anabarbosa
"""
from Bio import Entrez, SeqIO

Entrez.email = 'example@gmail.com'

class GetID:
    
    def __init__(self, query):
        self.__query = query
       
    def ListaIDs(self):
        gene=Entrez.esearch(db="gene", term='Homo Sapiens[Orgn] AND '+ self.__query + '[Gene]', sort = 'relevance', rettype='gb')
        gene_read = Entrez.read(gene)
        gene.close()
        return gene_read['IdList'][0]
    
    def SOX10_ID(self):
        id_gene = self.ListaIDs()
        gene_xml = Entrez.efetch(db="gene", id=id_gene, retmode='xml', rettype='gb')
        gene_read_xml = Entrez.read(gene_xml,'genbank')
        gene_xml.close()
        seq_id = gene_read_xml[0]['Entrezgene_comments'][5]['Gene-commentary_comment'][0]['Gene-commentary_comment'][0]['Gene-commentary_accession']
        return seq_id
        
    def ZEB2_ID(self):
        id_gene = self.ListaIDs()
        gene_xml = Entrez.efetch(db="gene", id=id_gene, retmode='xml', rettype='gb')
        gene_read_xml = Entrez.read(gene_xml,'genbank')
        gene_xml.close()
        seq_id = gene_read_xml[0]['Entrezgene_comments'][6]['Gene-commentary_comment'][0]['Gene-commentary_comment'][0]['Gene-commentary_accession']
        return seq_id
    
    def TFAP2_ID(self):
        id_gene = self.ListaIDs()
        gene_xml = Entrez.efetch(db="gene", id=id_gene, retmode='xml', rettype='gb')
        gene_read_xml = Entrez.read(gene_xml,'genbank')
        gene_xml.close()
        seq_id = gene_read_xml[0]['Entrezgene_comments'][5]['Gene-commentary_comment'][1]['Gene-commentary_comment'][0]['Gene-commentary_accession']
        return seq_id

    def SOX10_Uniprot(self):
        id_gene = self.ListaIDs()
        gene_xml = Entrez.efetch(db="gene", id=id_gene, retmode='xml', rettype='gb')
        gene_read_xml = Entrez.read(gene_xml,'genbank')
        gene_xml.close()
        prot_id = gene_read_xml[0]['Entrezgene_comments'][5]['Gene-commentary_comment'][0]\
        ['Gene-commentary_products'][0]['Gene-commentary_products'][0]['Gene-commentary_comment'][2]\
        ['Gene-commentary_comment'][0]['Gene-commentary_source'][1]['Other-source_anchor']
        return prot_id
    
    def ZEB2_Uniprot(self):
        id_gene = self.ListaIDs()
        gene_xml = Entrez.efetch(db="gene", id=id_gene, retmode='xml', rettype='gb')
        gene_read_xml = Entrez.read(gene_xml,'genbank')
        gene_xml.close()
        prot_id = gene_read_xml[0]['Entrezgene_comments'][6]['Gene-commentary_comment'][0]\
        ['Gene-commentary_products'][0]['Gene-commentary_products'][0]['Gene-commentary_comment'][2]\
        ['Gene-commentary_comment'][0]['Gene-commentary_source'][0]['Other-source_anchor']
        return prot_id

    def TFAP2_Uniprot(self):
        id_gene = self.ListaIDs()
        gene_xml = Entrez.efetch(db="gene", id=id_gene, retmode='xml', rettype='gb')
        gene_read_xml = Entrez.read(gene_xml,'genbank')
        gene_xml.close()
        prot_id = gene_read_xml[0]['Entrezgene_comments'][5]['Gene-commentary_comment'][1]\
        ['Gene-commentary_products'][1]['Gene-commentary_products'][0]['Gene-commentary_comment'][2]\
        ['Gene-commentary_comment'][0]['Gene-commentary_source'][0]['Other-source_anchor']
        return prot_id

    def SOX10_NCBIprotein(self):
        id_gene = self.ListaIDs()
        gene_xml = Entrez.efetch(db="gene", id=id_gene, retmode='xml', rettype='gb')
        gene_read_xml = Entrez.read(gene_xml,'genbank')
        gene_xml.close()
        prot_id = gene_read_xml[0]['Entrezgene_comments'][5]['Gene-commentary_comment'][0]\
        ['Gene-commentary_products'][0]['Gene-commentary_products'][0]['Gene-commentary_accession']
        return prot_id

    def ZEB2_NCBIprotein(self):
        id_gene = self.ListaIDs()
        gene_xml = Entrez.efetch(db="gene", id=id_gene, retmode='xml', rettype='gb')
        gene_read_xml = Entrez.read(gene_xml,'genbank')
        gene_xml.close()
        prot_id = gene_read_xml[0]['Entrezgene_comments'][6]['Gene-commentary_comment'][0]\
        ['Gene-commentary_products'][0]['Gene-commentary_products'][0]['Gene-commentary_accession']
        return prot_id

    def TFAP2_NCBIprotein(self):
        id_gene = self.ListaIDs()
        gene_xml = Entrez.efetch(db="gene", id=id_gene, retmode='xml', rettype='gb')
        gene_read_xml = Entrez.read(gene_xml,'genbank')
        gene_xml.close()
        prot_id = gene_read_xml[0]['Entrezgene_comments'][5]['Gene-commentary_comment'][1]\
        ['Gene-commentary_products'][2]['Gene-commentary_products'][0]['Gene-commentary_accession']
        return prot_id
        

    