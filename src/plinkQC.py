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

                pathName = f"ADNI1filtered/run{run}/LD/LD{i}"
                os.system(f"./plink --file {pathName}/pruned --recodeA")#get.raw
                os.system(f"awk '{$1=$2=$3=$4=$5=$6=""; print $0}' {pathName}/pruned.raw > {pathName}/genotipos") ### remove as 6 primeiras colunas
                
                os.system(f"awk 'NR > 1 { print }' {pathName}/genotipos > {pathName}/genotipos") # remove a primeira linha
                os.system(f"sed 's/NA/5/g' {pathName}/genotipos > {pathName}/genotipos") # substituir NA por 5
                os.system(f"sed 's/ //g' {pathName}/genotipos > {pathName}/genotipos")  # remove espaço
                os.system(f"awk 'NR > 1 { print }' {pathName}/pruned.raw > {pathName}/pessoas")
                os.system(f"awk '{print $2}' {pathName}/pessoas > {pathName}/pessoas")
                os.system(f"paste pessoas {pathName}/genotipos > {pathName}/genotipos_BLUP")
                
                ####modificar o arquivo mapa
                os.system(f"./plink --file {pathName}/pruned --recode") #get .map
                
                os.system(f"awk '{print $2, $1, $4} {pathName}/pruned.map > {pathName}/mapa")
              run = run + 1



            
        
  




            
        
