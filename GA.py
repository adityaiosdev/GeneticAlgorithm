import random
import numpy as np
import copy

def generateKromosom(kromsize):
    krom = []  
    for i in range(kromsize):
        krom.append(random.randint(0,1))      
    return krom

def crossover(parent1,parent2,pcross):
    r =random.random()
    if (r<pcross):
        point = random.randint(0,7)
        for i in range(point):
            parent1[i],parent2[i]=parent2[i],parent1[i]
    return parent1,parent2


def mutation(parent1,parent2,pmutate):
    r=random.random()
    r1= random.randint(0,9)
    r2= random.randint(0,9)
    p1= parent1[r1]
    p2= parent2[r2]
    if (r< pmutate):
        r=random.random()
        if (p1==0):
            p1=1
        elif (p1==1):
            p1=0
        if (p2==0):
            p2=1
        elif (p2==1):
            p2=0
    parent1[r1] = p1
    parent2[r2] = p2
    return parent1,parent2

def getElitisme(array_fitness):
    return array_fitness.index(max(array_fitness))

popsize = 100
generation = 50
pcross= 0.7
pmutate= 0.01
toursize = 10
kromsize = 10

arr_fitness =[]
def encodingKromosom(kromos): 
    x1 =-1+ ((2+1)/(2**-1 + 2**-2+2**-3+2**-4+2**-5))*((kromos[0]*2**-1)+(kromos[1]*2**-2)+(kromos[2]*2**-3)+(kromos[3]*2**-4)+(kromos[4]*2**-5))
    x2 =-1+ ((1+1)/(2**-1 + 2**-2+2**-3+2**-4+2**-5))*((kromos[5]*2**-1)+(kromos[6]*2**-2)+(kromos[7]*2**-3)+(kromos[8]*2**-4)+(kromos[9]*2**-5))
    return [x1, x2]
def generatePopulation():
    new_pop=[]
    for i in range (popsize):
        new_pop.append(generateKromosom(kromsize))
    return new_pop

def hasilfitnesss(populatt,popsize):
    k=[]
    for i in range (popsize):
        k.append(fitnesss(populatt[i]))
    return k
def fitnesss(populatt):
    k=encodingKromosom(populatt)
    # fitnessfunc= 1/((((np.cos(k[0])*np.sin(k[1]))) - (k[0]/((k[1]**2)+1))) + 0.01)
    h= ((np.cos(k[0])*np.sin(k[1])) - (k[0]/(k[1]**2+1)))
    a= 0.01
    fitnessfunc= 1/(h+a)
    return fitnessfunc

def nampungfitness(populatt,popsize): 
    fit_all = []    
    for i in range(popsize):
        fit_all.append(fitnesss(popsize[i]))
    return fit_all

def tournamentSelection(pop, toursz, popsize):
    best_krom=[]
    for i in range(1, toursz):
        p=populationbaru[random.randint(0,popsize-1)]
        if (len(best_krom) == 0) or fitnesss(p)>fitnesss(best_krom):
            best_krom=p
    return best_krom

populationbaru= generatePopulation()

# print("============================ Populasi ==========================")
# print(populationbaru)
# print("============================ ===================================")

# print("")


# print(hasilfitnesss(populationbaru,popsize)) # digunakan untuk tracing

for i in range(generation):
    fungsfitness= hasilfitnesss(populationbaru,popsize)
    # print(fungsfitness) #dapat digunakan untuk tracing nilai fitness yang didapatkan pergenerasi
    new_pop = []
    bestfitness=getElitisme(fungsfitness)
    new_pop.append(populationbaru[bestfitness])
    new_pop.append(populationbaru[bestfitness])
    j=0
    while (j<popsize-1):
        parent1 = tournamentSelection(populationbaru,toursize,popsize)
        parent2 = tournamentSelection(populationbaru,toursize,popsize)
        while (parent1==parent2):
            parent2 = tournamentSelection(populationbaru,toursize,popsize)
        coppar1= copy.deepcopy(parent1)
        coppar2= copy.deepcopy(parent2)
        child= crossover(coppar1,coppar2,pcross)
        child= mutation(child[0],child[1],pmutate)
        new_pop += child
        j+=2
    populationbaru= new_pop
fungsfitness= hasilfitnesss(populationbaru,popsize)
result =getElitisme(fungsfitness)


print("")
print("========================================================================================")
print('           Hasil Minimasi Fungsi Genetic Algorithm  ')
print("")
print('Kromosom terbaik:', populationbaru[result])
print('Hasil encode    :', encodingKromosom(populationbaru[result]))
print('Nilai Fitness terbaik :', fitnesss(populationbaru[result]) )
print("========================================================================================")
