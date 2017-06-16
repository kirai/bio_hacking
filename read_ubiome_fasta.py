# Read first fast file from Hector's ubiome analysis
# DNA sample extracted: 11th of April 2017 

from Bio import SeqIO
for seq_record in SeqIO.parse("ubiome_data/April2017/ssr_108823/ssr_108823__R1__L001.fastq", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

