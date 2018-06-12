#Get high qality record by setting DP:Total depth over all samples, GQ: conditional genotype quality
vcffilter -f "DP >5" -g "GQ >10" a.vcf >a_DP5_GQ10.vcf

#If you are only interested with SNPs. 
vcftools --vcf a_DP5_GQ10.vcf --remove-indels --recode --recode-INFO-all --out a_DP5_GQ10_SNP_only.vcf

#Subset with sample names (seperated by comma) and minimum 1 allele is non-reference.
bcftools view -s the_samples_you_are_interested a_DP5_GQ10_SNP_only.vcf -c1 -o >a_DP5_GQ10_SNP_only_subset.vcf
