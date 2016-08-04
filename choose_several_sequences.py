#!/usr/bin/python
#sys.argv[1]:original fasta,sys.argv[2]:file with IDs,sys.argv[3]:prefix of file
import sys
from Bio import SeqIO
seq=SeqIO.to_dict(SeqIO.parse(sys.argv[1],'fasta'))
ot=open("%s.fasta" % (sys.argv[3]),'w')
for line in open(sys.argv[2]):
	line = line.strip()
	seq_choose = seq[line][0:]
	seq_choose.id = line
	seq_choose.description = ''
	SeqIO.write(seq_choose,ot,'fasta')
ot.close()

