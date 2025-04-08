import re
input=open("c:/Users/Iriss/Desktop/IBI/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')
input=input.read()
tata= r'TATA(A|T)A(A|T)'
processed_input=re.sub(r'\n(?=>)', '||', input)
processed_input=re.sub(r']\n','||',processed_input)
input_delete_n=re.sub(r'\n', '', processed_input)
processed_data=re.sub(r'\|\|', '\n', input_delete_n)
lines= processed_data.split('\n')

tata_genes=[]
for line in lines:
    if line[0]==">":
        gene_name=line[0:8]
    else:
        if re.search(tata,line):
            tata_genes.append([gene_name,line])

output=open('c:/Users/Iriss/Desktop/IBI/tata_genes2.fa', 'w')
for i in tata_genes:
    output.write(i[0]+'\n'+i[1]+'\n')
