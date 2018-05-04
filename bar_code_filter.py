import string
import regex
import re
from itertools import islice

bar1B6XCAST="ATCACG"
bar2B6="TTAGGC"

out=open("B6XCAST_reads_L2_R1_4.fastq","w")
out2=open("B6reads_L2_R1_4.fastq","w")
out3=open("Undetermined_L2_R1_4.fastq","w")

with open("Undetermined_S0_L002_R1_001.fastq") as f:
    for line in f:
        if line[0:3]=="@SN":
		a="".join(line[-7:-1])
		
		#this will allow 4mismatch, please adjust the number as you needed

		fa=r"(?:"+re.escape(a)+r"){s<=4}"

		if regex.findall(fa,bar1B6XCAST)!=[]:
			print >>out,line[:-1]
			print >>out,''.join(islice(f, 3)).rstrip("\n")
		
		elif regex.findall(fa,bar2B6)!=[]:
			print >>out2,line[:-1]
			print >>out2,''.join(islice(f, 3)).rstrip("\n")
		else :
			print >>out3,line[:-1]
			print >>out3,''.join(islice(f, 3)).rstrip("\n")
