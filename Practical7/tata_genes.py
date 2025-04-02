import re
input=open("c:/Users/Iriss/Desktop/IBI/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')
gene_name=[]
last_seq=[]
include_tata=[]
sequence=''
tata=r'TATA(A|T)A(A|T)'
for line in input:
    line=line.rstrip()
    if line[0]=='>':
        if len(gene_name)!=0:
            sequence=''.join(last_seq)
            if re.search(tata, sequence):
                include_tata.append([gene_name, sequence])
        gene_name = re.findall(r'gene:.+?\s',line)[0][5:]
        last_seq = []
    else:
        last_seq.append(line)
        
if len(gene_name)!=0 :
            sequence=''.join(last_seq)
            if re.search(tata, sequence):
                include_tata.append([gene_name, sequence])
output=open('c:/Users/Iriss/Desktop/IBI/tata_genes.fa', 'w')
for i in include_tata:
    output.write('>'+i[0]+'\n')
    output.write(i[1]+'\n')