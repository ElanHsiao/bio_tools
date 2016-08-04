#!/usr/bin/python
from Bio import SeqIO
import sys,os
#sys.argv[1]:ID sys.argv[2]:original fastq sys.argv[3]:name
or1=open('%s.%s'%(sys.argv[3],sys.argv[2]),'w')
lst=set([x.strip() for x in open(sys.argv[1])])
for yi in SeqIO.parse(sys.argv[2],'fastq'):
	if yi.id in lst:
		SeqIO.write(yi,or1,'fastq')