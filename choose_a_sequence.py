#!/usr/bin/python
#sys.argv[1]:original fasta sys.argv[2]:prefix sys.argv[3]:start sys.argv[4]:end
import sys
from Bio import SeqIO
seq=SeqIO.read(sys.argv[1],'fasta')
ot=open('%s.fasta' % (sys.argv[2]),'w')
start=int(sys.argv[3])-1
end=int(sys.argv[4])

seq_choose=seq[start:end]
seq_choose.id=sys.argv[2]
seq_choose.description = ''
SeqIO.write(seq_choose,ot,'fasta')
ot.close()
