def determine_restriction_enzyme_cutsites(DNA_sequence,rec_sequence):
    valid=['A','C','G','T']
    for i in DNA_sequence:
        if i in valid:
            continue
        return "invalid DNA sequence"
    for i in rec_sequence:
        if i in valid:
            continue
        return "invalid recognition sequence"
    
    sites = []
    len_rec=len(rec_sequence)
    for i in range(len(DNA_sequence) - len_rec + 1):
        if DNA_sequence[i:i+len_rec] == rec_sequence:
            sites.append(i)
    if sites:
        return sites
    else:
        return "No cut sites found"

DNA='ACGGTAGGGACGTAACGT'
rec_sequence="ACG"
print(determine_restriction_enzyme_cutsites(DNA,rec_sequence))