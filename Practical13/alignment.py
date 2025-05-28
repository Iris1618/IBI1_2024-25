import os
os.chdir("c:/Users/Iriss/Desktop/IBI/IBI1_2024-25/Practical13")

def get_blosum_matrix(file):
    lines=[]
    for line in file:
        if not line[0]=="#" and line.strip():
            lines.append(line.strip().split())
    header = lines[0]
    dictionary = {}
    for row in lines[1:]:
        aa1 = row[0]
        dictionary[aa1] = {}
        for aa2, score in zip(header, row[1:]):
            dictionary[aa1][aa2] = int(score)
    return dictionary

def get_fasta_sequence(file):
    lines = file.readlines()
    sequence = ''
    for line in lines:
        if not line[0]=='>':
            sequence += line.strip()
    return sequence

def compare_sequences(seq1, seq2, blosum62):
    scores = []
    identical = 0
    for a1, a2 in zip(seq1, seq2):
        if a1 in blosum62 and a2 in blosum62[a1]:
            score = blosum62[a1][a2]
        else:
            score = 0  
        scores.append(score)
        if a1 == a2:
            identical += 1
    total_score = sum(scores)
    similarity_percent = (identical / len(seq1)) * 100
    return total_score, similarity_percent, scores

def print_result(name1, seq1, name2, seq2, score, identity, score_vector):
    print(f"Comparison: {name1} vs {name2}")
    print(f"{name1} Sequence:\n{seq1}\n")
    print(f"{name2} Sequence:\n{seq2}\n")
    print("Optional Alignment (position-by-position):")
    for i in range(len(seq1)):
        print(f"{seq1[i]}  {seq2[i]}  Score: {score_vector[i]}")
    print("\nSummary:")
    print(f"Total Score: {score}")
    print(f"Similarity percent: {identity:.2f}%\n")
with open("BLOSUM62.txt", "r") as BLOSUM62:
    blosum62=get_blosum_matrix(BLOSUM62)
with open("human_sod2.fasta", "r") as human_sod2:
    human_sequence = get_fasta_sequence(human_sod2)
with open("mouse_sod2.fasta", "r") as mouse_file:
    mouse_sequence = get_fasta_sequence(mouse_file)
with open("random.fasta", "r") as random_file:
    random_sequence = get_fasta_sequence(random_file)

score, identity, vector = compare_sequences(human_sequence, mouse_sequence, blosum62)
print_result('human_SOD2',human_sequence,'mouse_sequence',mouse_sequence,score,identity,vector)
score, identity, vector = compare_sequences(human_sequence, random_sequence, blosum62)
print_result('human_SOD2',human_sequence,'random_sequence',random_sequence,score,identity,vector)
score, identity, vector = compare_sequences(mouse_sequence, random_sequence, blosum62)
print_result('mouse_SOD2',mouse_sequence,'random_sequence',random_sequence,score,identity,vector)