# MSM_RS03110 50S ribosomal protein L1 [ Methanobrevibacter smithii ATCC 35061 ]
# https://www.ncbi.nlm.nih.gov/gene/5217347
# Read fasta data from 23S RNA interface 

from Bio import SeqIO
for seq_record in SeqIO.parse("smithii/NC_009515.1[603204..603325](-).fa", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

