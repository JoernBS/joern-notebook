import re

## with open("rosalind_subs.txt","r")as file ##r=read

## s = open(file.fasta) ##

s = ('GATATATGCATATACTTATAT')

t =('ATAT')
matches = re.finditer(t,s)

results = [] 
for m in matches:
	pos_start=m.start()+1
	#pos_end=pos_start+len(t)
	#string=m.group()
	#position= pos_start,pos_end
	results.append(pos_start)
	

print(results, end=' ')



