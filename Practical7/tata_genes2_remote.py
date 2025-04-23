import datetime
import re
start_time = datetime.datetime.now()
input=open("/public/workspace/robert_young/ibi1_2025/hg38.mrna.fa",'r')
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

output=open('/public/workspace/IBI1_17/dongting/tata_genes2.fa', 'w')
for i in tata_genes:
    output.write(i[0]+'\n'+i[1]+'\n')
end_time = datetime.datetime.now()
runtime = end_time - start_time
print("runtime", runtime)
