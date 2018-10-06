import sys
from generallib import *
import random

numberofargs = 4+1
if len(sys.argv) < numberofargs:
    print('arguments are: 1.randomseed 2.ntreeparameter 3.datasetpath 4.outputpath')
    callexit()
if (sys.argv[3]=='-'):
    datasetpath = 'dadosBenchmark_validacaoAlgoritmoAD.csv'
else:
    datasetpath = sys.argv[3]
random.seed(sys.argv[1])
ntreeparameter = sys.argv[2]
try:
    dataset = readdataset(datasetpath)
    print('this is the dataset:',dataset)
    # tree = create_tree(dataset)

except Exception as e:
	print('Error!\n',e)
	callexit()



callexit()
