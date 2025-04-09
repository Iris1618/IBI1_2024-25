import re
input_file=open("c:/Users/Iriss/Desktop/IBI/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')
input_file=input_file.read()
tata= r'TATA(A|T)A(A|T)'

processed_input=re.sub(r'\n(?=>)', '||', input_file)
processed_input=re.sub(r']\n','||',processed_input)
input_delete_n=re.sub(r'\n', '', processed_input)
processed_data=re.sub(r'\|\|', '\n', input_delete_n)
lines= processed_data.split('\n')

splice = input("please input one of the three possible splice donor/acceptor combinations(GTAG,GCAG,ATAC):")
valid_splices = ['GTAG', 'GCAG', 'ATAC']
if splice not in valid_splices:
    print("invalid splices")
splice_donor = splice[:2]
splice_acceptor = splice[2:]


spliced_tata_genes = []
gene_name = ''
sequence = ''
new_sequence=''
count_tata=0
for line in lines:
    if line[0]==">":
        if len(gene_name)!=0 :
            if splice_donor in sequence and splice_acceptor in sequence:
                y= re.findall(rf'{splice_donor}.+{splice_acceptor}',sequence)
                if len(y)!=0:
                    if re.search(tata, y[0]):
                        count_tata += len(re.findall(tata, y[0]))
                        spliced_tata_genes.append([gene_name, sequence, count_tata])
                        count_tata=0
        gene_name = line[1:8]
        sequence = ''
    else:
        sequence += line

if len(gene_name)!=0 :
            if splice_donor in sequence and splice_acceptor in sequence:
                y= re.findall(rf'{splice_donor}.+{splice_acceptor}',sequence)
                if len(y)!=0:
                    if re.search(tata, y[0]):
                        count_tata += len(re.findall(tata, y[0]))
                        spliced_tata_genes.append([gene_name, sequence, count_tata])

filename = splice+'_spliced_genes.fa'
output=open('c:/Users/Iriss/Desktop/IBI/'+filename, 'w')
for gene in spliced_tata_genes:
    output.write('>'+gene[0]+' TATA_count='+str(gene[2])+'\n'+gene[1]+'\n')