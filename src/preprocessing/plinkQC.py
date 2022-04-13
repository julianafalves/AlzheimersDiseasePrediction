import os


QL_parameters = {'Missingness per snps':[0.02,0.05,0.1,0.2],
                 'Missingness per sample':[0.05,0.1],
                 'Minor allele Frequêncy':[0.01,0.05,0.1],
                 'Hardy-weinberg equilibrium':[0.000005,0.00000001]}

run = 1

for genoId in range(len(QL_parameters['Missingness per snps'])):
    geno = QL_parameters['Missingness per snps'][genoId]
    
    for mafId in range(len(QL_parameters['Minor allele Frequêncy'])):
        maf = QL_parameters['Minor allele Frequêncy'][mafId]
        
        for mindId in range(len(QL_parameters['Missingness per sample'])):
            mind = QL_parameters['Missingness per sample'][mindId]
            
            for hweId in range(len(QL_parameters['Missingness per sample'])):
              hwe = QL_parameters['Hardy-weinberg equilibrium'][hweId]
        
              os.mkdir(f"ADNI1filtered/run{run}")
              os.system(f"./plink --bfile ADNI_cluster_01_forward_757LONI --geno {geno} --mind {mind} --maf {maf} --hwe {hwe} --make-bed --out ADNI1filtered/run{run}/adni1")
              
              os.mkdir(f"ADNI1filtered/run{run}/txtFiles")
              os.system(f"./plink --bfile ADNI1filtered/run{run}/adni1 --recodeA --out ADNI1filtered/run{run}/txtFiles/adniRaw")
              
              os.system(f"awk '{{print}}' ADNI1filtered/run{run}/txtFiles/adniRAW.raw > ADNI1filtered/run{run}/txtFiles/genotipos")
              #LD Pruning - remove SNPs with hifh LD 
              os.mkdir(f"ADNI1filtered/run{run}/LD")
              
              for i in ['80','85','90']: 
                os.mkdir(f"ADNI1filtered/run{run}/LD/LD{i}")
                os.system(f"./plink --bfile ADNI1filtered/run{run}/adni1 --make-founders --indep-pairwise 50 5 {int(i)/100} --out ADNI1filtered/run{run}/LD/ouputLD{i}")
                os.system(f"./plink --bfile ADNI1filtered/run{run}/adni1 --exclude ADNI1filtered/run{run}/LD/ouputLD{i}.prune.out --make-bed --out ADNI1filtered/run{run}/LD/LD{i}/pruned")
                
              run = run + 1




            
        
  




            
        
