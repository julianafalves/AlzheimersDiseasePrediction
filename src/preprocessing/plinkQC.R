#Quality Control of ADNI1
#This code filter the ADNI1 SNP data
#using the plink program
setwd("/home/alvesj/documents/ADNI_1_GWAS_Plink/")
dir.create("ADNI1filtered/")

#Missingness per snps = 2%
#Missingness per sample = 5%
#Minor allele Frequêncy = 1%
#Hardy-weinberg equilibrium = 5*10^-6

dir.create("ADNI1filtered/run1/")
system("./plink --bfile ADNI_cluster_01_forward_757LONI --geno 0.02 --mind 0.05 --maf 0.01 --hwe 0.000005 --make-bed --out ADNI1filtered/run1/adni1")
#system("./plink --bfile ADNI1filtered/run1/adni1 --recodeA --out ADNI1filtered/run1/adni1raw") -> get .raw
#system("./plink --bfile ADNI1filtered/run1/adni1 --recode --out ADNI1filtered/run1/adni1raw") ->get.map


#Missingness per snps = 2%
#Missingness per sample = 10%
#Minor allele Frequêncy = 1%
#Hardy-weinberg equilibrium = 5*10^-6
dir.create("ADNI1filtered/run2/")
system("./plink --bfile ADNI_cluster_01_forward_757LONI --geno 0.02 --mind 0.1 --maf 0.01 --hwe 0.000005 --make-bed --out ADNI1filtered/run2/adni1")
#system("./plink --bfile ADNI1filtered/run1/adni1 --recodeA --out ADNI1filtered/run1/adni1raw") -> get .raw
#system("./plink --bfile ADNI1filtered/run1/adni1 --recode --out ADNI1filtered/run1/adni1raw") ->get.map