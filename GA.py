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
    x1= -1+ ((2+1)/(2**-1 + 2**-2+2**-3))*((krom[0]*2**-1)+(krom[1]*2**-2)+(krom[2]*2**-3))
    x2 =-1+ ((1+1)/(2**-1 + 2**-2+2**-3))*((krom[3]*2**-1)+(krom[4]*2**-2)+(krom[5]*2**-3))
    
    return [x1, x2]

def fitness(krom):
    k= encodingKromosom(krom)
    fitnessfunc= -((np.cos(k[0]))*(np.sin(k[1]))- (k[0]/(k[1]**2)+1))
    return fitnessfunc

def arrAllFitness(pop,pop_size):
    arrfit=[]
    for i in range (pop_size):
        arrfit.append(fitness(pop[i]))
    return arrfit

def tournamentSelection(pop, uk_tour, popsize):
    best_krom = []
    for i in range(1, uk_tour):
        krom = pop[random.randint(0,popsize-1)]
        if (best_krom == [] or fitness(krom) > fitness(best_krom)):
            best_krom = krom
    return best_krom


def crossover(parent1,parent2,pcross):
    r =random.random()
    if (r<pcross):
        point = random.randint(0,5)
        for i in range(point):
            parent1[i],parent2[i]=parent2[i],parent1[i]

    return parent1,parent2

def mutation(parent1,parent2,pmutate):
    r=random.random()
    if (r< pmutate):
        parent1[random.randint(0,5)] = random.randint(0,1)
        parent2[random.randint(0,5)] = random.randint(0,1)
    return parent1,parent2

def getElitisme(arrfit):
    return arrfit.index(max(arrfit))

popsize = 1
generation = 50
pcross= 0.70
pmutate= 0.02
uk_tour = 5
krom_size = 6

arr_fitness =[]
def encodingKromosom(krom): 
    x1= -1+ ((2+1)/(2**-1 + 2**-2+2**-3))*((krom[0]*2**-1)+(krom[1]*2**-2)+(krom[2]*2**-3))
    x2 =-1+ ((1+1)/(2**-1 + 2**-2+2**-3))*((krom[3]*2**-1)+(krom[4]*2**-2)+(krom[5]*2**-3))
    
    return [x1, x2]
def generatePopulation():
    new_pop=[]
    for i in range (popsize):
        new_pop.append(generateKromosom(krom_size))
    return new_pop

populationbaru= generatePopulation()
populationbaru.append(generateKromosom(krom_size))
print(populationbaru)
def nampungencoding(populatt):
    arrayencode=[]
    for i in range (popsize+1):
        arrayencode.append(encodingKromosom(populatt[i]))
    return arrayencode

def fitnesss(populatt):
    k=nampungencoding(populatt)
    for i in range (popsize+1):
        fitnessfunc= -((np.cos(k[i][0]))*(np.sin(k[i][1]))- (k[i][0]/(k[i][1]**2)+1))
        k[i]=fitnessfunc
    return k

print(nampungencoding(populationbaru))

for i in range (popsize+1):
    print(fitness(populationbaru[i]))

#print(nampungencoding(populationbaru))


# encodingKromosom(new_pop)
# pupulasi = generatePopulation()
# print(pupulasi)

# for i in range(popsize):
#     print(encodingKromosom(pupulasi))


#arr_fitness = encodingKromosom(new_pop)
#print(arr_fitness)

# population = generatePopulasi(popsize)
# for i in range(generation):
#     fungsfitness= arrAllFitness(population,popsize)
#     new_pop = []

#     bestfitness=getElitisme(fungsfitness)
#     new_pop.append(population[bestfitness])
#     new_pop.append(population[bestfitness])
#     i=0
#     while (i<popsize-1):
#         parent1 = tournamentSelection(population,uk_tour,popsize)
#         parent2 = tournamentSelection(population,uk_tour,popsize)
#         while (parent1==parent2):
#             parent2 = tournamentSelection(population,uk_tour,popsize)
#         cpar1= copy.deepcopy(parent1)
#         cpar2= copy.deepcopy(parent2)
#         child= crossover(cpar1,cpar2,pcross)
#         child= mutation(child[0],child[1],pmutate)
#         new_pop += child
#         i+=2
#     population= new_pop
# fungsfitness= arrAllFitness(population,popsize)
# result =getElitisme(fungsfitness)


# print('           HASIL MINIMASI FUNGSI')
# print()
# print('Kromosom terbaik:', population[result])
# print('Fitness terbaik :', fitness(population[result]))
# print('Hasil decode    :', encodingKromosom(population[result]))
