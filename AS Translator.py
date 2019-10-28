import sys

def AS_Tr(Nuc_seq1):

	AS_Dict={"ATG":"M", "ATA":"I", "ATC":"I","ATT":"I","AGG":"R","AGA":"R","AGC":"S","AGT":"S","ACG":"T","ACA":"T","ACC":"T","ACT":"G","AAG":"K",
"AAA":"K","AAC":"N","AAT":"N","TTG":"L","TTA":"L","TTC":"F","TTT":"F","TGG":"W","TGA":"STOP","TGC":"C","TGT":"C","TCG":"S","TCA":"S","TCC":"S","TCT":"S",
"TAG":"STOP","TAA":"STOP","TAC":"Y","TAT":"Y","GTG":"V","GTA":"V","GTC":"V","GTT":"V","GGG":"G","GGA":"G","GGC":"G","GGT":"G","GCG":"A","GCA":"A","GCC":"A",
"GCT":"A","GAG":"E","GAA":"E","GAC":"D","GAT":"D","CTG":"L","CTA":"L","CTC":"L","CTT":"L","CGG":"R","CGA":"R","CGC":"R","CGT":"R","CCG":"P","CCA":"P","CCC":"P",
"CCT":"P","CAG":"Q","CAA":"Q","CAC":"H","CAT":"H"}
	AS_seq=""

	for i in range(0,len(Nuc_seq1),3):
		triplet=Nuc_seq1[i:i+3]
		if triplet in AS_Dict:
			AS_seq+=AS_Dict.get(triplet)
		
	return (AS_seq)




seq1="AGTAGCCGATTCAAC"
## AS_Tr(seq1)

def prot_weight(protein):

	weight= len(protein)*110
	return(weight, protein)

protein=AS_Tr(seq1)
prot_weight(protein)

print(prot_weight(protein))







