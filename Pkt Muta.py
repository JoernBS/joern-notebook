
Seq1="ATGCGTAAGTCCTG"
Seq2="ATGTGTAAGTTCTG"
position=0
count=0

for i,j in zip(Seq1,Seq2):
	position+=1
	if i != j:
		mutation=i+str(position)+j
		count+=1
		print(mutation,"at position:",position)
	else:
		continue
print("number of mutations:",count)




