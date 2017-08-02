from Bio import SeqIO
record = SeqIO.read("plasmids/NC_005816.gb", "genbank")

print("Plasmid description:")
print(record.description)
print("Number of features:")
print(len(record.features))
