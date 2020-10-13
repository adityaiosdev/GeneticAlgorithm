import random
import numpy as np
import copy


def generateKromosom(krom_size):
    krom = []  
    for i in range(krom_size):
        krom.append(random.randint(0,1))      
    
    return krom

def generatePopulasi(pop_size):
    pop = []
    for i in range(pop_size):
        pop.append(generateKromosom(6))
    return pop
def encodingKromosom(krom): 
    x1= -1+ (((2+1)/(2**-1 + 2**-2+2**-3))*((krom[0]*2**-1)+(krom[1]*2**-2)+(krom[3]*2**-3)))
    x2 = -1 + (((1+1)/(2**-1 + 2**-2+2**-3))*((krom[4]*2**-1)+(krom[5]*2**-2)+(krom[6]*2**-3)))
    
    return [x1, x2]

popsize = 50
populasi = generatePopulasi(popsize)
print(populasi)
