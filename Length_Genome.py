#! /usr/bin/python
#sys.argv[1]:fasta
from Bio import SeqIO
import sys
length_sum = 0
for yi in SeqIO.parse(sys.argv[1],'fasta'):
	length_sum=len(yi)+length_sum
print(length_sum)
