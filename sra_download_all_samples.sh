# Top: https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?study=ERP012803
# 
# https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=samples&term=sibo&go=Go
# https://www.ncbi.nlm.nih.gov/sra/ERX2092801[accn]
# https://www.ncbi.nlm.nih.gov/Traces/study/?acc=SAMEA104163721

wget 'http://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?save=efetch&rettype=runinfo&db=sra&term==PRJEB11419' -O - | tee SraRunInfo.csv
