#!/usr/bin/env python3

#utilizando biblioteca biopython

!pip install biopython

from Bio import SeqIO

#utilizando um arquivo fasta chamado python7.fasta

records = list(SeqIO.parse("python7.fasta", "fasta"))

codon = str(records[0].seq) 

print(codon)

#definindo quais são os 3 codons de parada

codon_fim = "TAA", "TAG","TGA"

#analisando se os codons de  parada estão nos codons encontrados e verificando se o comprimento do ORF é múltiplo de 3

if len(codon)%3 == 0:
  print("Seu comprimento é múltiplo de 3")

if (codon_fim[0] in codon) == True:
  print(f"O códon de terminação {codon_fim[0]} se encontra na sequência imputada")

if (codon_fim[1] in codon) == True:
  print(f"O códon de terminação {codon_fim[1]} se encontra na sequência imputada")

if (codon_fim[2] in codon) == True:
  print(f"O códon de terminação {codon_fim[2]} se encontra na sequência imputada")

import re
codon_fim1 = re.search('ATG(.+?)TAG',codon).group(1)
codon_fim2 = re.search('ATG(.+?)TAA',codon).group(1)
codon_fim3 = re.search('ATG(.+?)TGA',codon).group(1)

if len(codon_fim1) > len(codon_fim2) and len(codon_fim1) > len(codon_fim3):
  maior = 'ATG'+codon_fim1+'TAG'
elif len(codon_fim2) > len(codon_fim3):
  maior = 'ATG'+codon_fim2+'TAA'
else:
  maior = 'ATG'+codon_fim3+'TGA'

from Bio.Seq import Seq

#maior ORF identificado e sua sequencia complementar gerada

maior_sequencia = Seq(maior)
sequencia_complementar = maior_sequencia.complement()
print(f"O maior ORF identificado foi: {maior_sequencia}")
print(f"A sequencia complementar gerada foi: {sequencia_complementar}")



