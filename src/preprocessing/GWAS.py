import os

#Card that must be used on renum program to generate input for the thrgibbs
renumCard = ['DATAFILE',
            'phenotype.txt',
            'TRAITS',
            '2',
            'FIELDS_PASSED TO OUTPUT',
            ' ', 
            'WEIGHT(S)',
            ' ', 
            'RESIDUAL VARIANCE',
            '3',
            'EFFECT',
            '   3 cross alpha',
            'EFFECT',
            '   1  cross alpha ',
            '   RANDOM',
            '   animal',
            '   FILE',
            '   pedBLUPF90.txt', # matrix ID 0 0
            '   SNP_FILE ',
            '   genotype_BLUPF90.txt', 
            '   PED_DEPTH',
            '   0' ,
            '   INBREEDING',
            '   pedigree',
            '   (CO)VARIANCES',
            '   1' ,
            'OPTION genotype_BLUPF90.txt' ,
            'OPTION chrinfo map.txt',
            'OPTION no_quality_control',
            'OPTION solution mean',
            'OPTION sol se',
            'OPTION Inbreeding',
            'OPTION cat 3',
            'OPTION fixed_var mean', 
            'OPTION excludeCHR 23 24 25 26']

with open('renumCard.txt', 'w') as f:
    f.write('\n'.join(renumCard))

#running the airemf90 lsto calculate the GEBVs
os.system('ulimit -s unlimited')
for runN in range(46):
    for ldValue in [80, 85, 90]:
        filePath = f"ADNI1filtered/run{runN}/LD/LD{ldValue}"
        os.system(f"filePath/renumf90 renumCard.txt")

        try:
            #itaretes 500.000 times, delete first 50.000 with step defined by 10
            os.system("filePath/thrgibbs1f90 renf90.par --rounds 500000 --burnin 50000 --thin 10")
            
        except:
            pass
