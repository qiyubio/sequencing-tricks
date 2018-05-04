import string
import sys
import os

a=sys.argv[1]

#os.system("rm align_swarm")
file=open(a+"_align_swarm",'w')

print >>file, "cd $PWD; module load samtools; module load STAR; module load sratoolkit; fastq-dump --split-3 %s; STAR --runThreadN 24 --genomeDir /fdb/STAR_current/GENCODE/Gencode_mouse/release_M16/genes-100/ --sjdbOverhang 100 --readFilesIn %s_1.fastq %s_2.fastq --readFilesCommand cat --outSAMtype BAM SortedByCoordinate --outFileNamePrefix %s " %(a,a,a,a)

file.close()

#STAR need large memory

os.system("swarm -g 72 -t 24 -f %s_align_swarm --sbatch '--time=24:00:00'"%(a))


