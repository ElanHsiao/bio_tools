#!/usr/bin/python
#sys.argv[1]:fasta
import sys
import os
from Bio import SeqIO
from Bio.SeqUtils import GC
for yi in SeqIO.parse(sys.argv[1],'fasta'):
		GC_content=GC((yi.upper().seq))
		Length=len((yi.upper().seq))
        print yi.id,GC_content,Length