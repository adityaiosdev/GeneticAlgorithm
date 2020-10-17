import random
import numpy as np
import copy

def generateKromosom(kromsize):
    krom = []  
    for i in range(kromsize):
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

# def fitness(krom):
#     k= encodingKromosom(krom)
#     fitnessfunc= -((np.cos(k[0]))*(np.sin(k[1]))- (k[0]/(k[1]**2)+1))
#     return fitnessfunc

# def arrAllFitness(pop,pop_size):
#     arrfit=[]
#     for i in range (pop_size):
#         arrfit.append(fitness(pop[i]))
#     return arrfit


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

def getElitisme(arr_fit):
    return arr_fit.index(max(arr_fit))

popsize = 100
generation = 200
pcross= 0.7
pmutate= 0.01
toursize = 5
kromsize = 10
totalgen = 0

arr_fitness =[]
def encodingKromosom(krom): 
    x1 =-1+ ((2+1)/(2**-1 + 2**-2+2**-3))*((krom[0]*2**-1)+(krom[1]*2**-2)+(krom[2]*2**-3)+(krom[3]*2**-4)+(krom[4]*2**-5))
    x2 =-1+ ((1+1)/(2**-1 + 2**-2+2**-3))*((krom[5]*2**-1)+(krom[6]*2**-2)+(krom[7]*2**-3)+(krom[8]*2**-4)+(krom[9]*2**-5))
    return [x1, x2]
def generatePopulation():
    new_pop=[]
    for i in range (popsize):
        new_pop.append(generateKromosom(kromsize))
    return new_pop



populationbaru= generatePopulation()

# print(arrAllFitness(populationbaru,popsize))
print("============================ Populasi ==========================")
print(populationbaru)
print("============================ ===================================")
# print(arrAllFitness(populationbaru,popsize))
print("")



# def nampungencoding(populatt):
#     arrayencode=[]
#     for i in range (popsize+1):
#         arrayencode.append(encodingKromosom(populatt[i]))
#     return arrayencode

# print("============================ Hasil Encoding Tiap Individu ==========================")
# print(nampungencoding(populationbaru))
# print("====================================================================================")
# print("")
# print("")

def hasilfitnesss(populatt):
    k=[]
    for i in range (popsize):
        k.append(fitnesss(populatt[i]))
    return k
    # def arrAllFitness(pop,pop_size):
#     arrfit=[]
#     for i in range (pop_size):
#         arrfit.append(fitness(pop[i]))
#     return arrfit

def fitnesss(populatt):
    k=encodingKromosom(populatt)
    fitnessfunc= 1/((((np.cos(k[0])*np.sin(k[1]))) - (k[0]/((k[1]**2)+1))) + 0.01)
    return fitnessfunc

def nampungfitness(populatt,popsize): 
    fit_all = []    
    for i in range(popsize):
        fit_all.append(fitnesss(popsize[i]))
    return fit_all

def tournamentSelection(pop, uk_tour, popsize):
    best_krom=[]
    for i in range(1, uk_tour):
        p=populationbaru[random.randint(0,popsize-1)]
        if (len(best_krom) == 0) or fitnesss(p)>fitnesss(best_krom):
            best_krom=p
    return best_krom


# print("ini fitness")

# print(fitnesss(populationbaru))

# j= random.choice(fitnesss(populationbaru))
# print(j)

# best_krom=[]
# for i in range(1, uk_tour):
#     p=populationbaru[random.randint(0,popsize)]
#     if (best_krom==[]) or fitnesss(p)>fitnesss(best_krom):
#         best_krom = p
# print("============================ Hasil Fitness Semua Infividu ==========================")
# print(hasilfitnesss(populationbaru))
# print("============================ =======================================================")
# print(tournamentSelection(populationbaru,uk_tour,popsize))
# print("============================parent1  =======================================================")
# parent1 = tournamentSelection(populationbaru,uk_tour,popsize)
# print(parent1)
# print("============================ ==============================================================")
# print("")
# print("============================parent 2 =======================================================")
# parent2 = tournamentSelection(populationbaru,uk_tour,popsize)
# print(parent2)
# print("============================ =======================================================")
# print("")
# print("ini mutasi")
# if(parent1==parent2):
#     parent2 = tournamentSelection(populationbaru,uk_tour,popsize)
# print("============================ =======================================================")
# print(mutation(parent1,parent2,pmutate))
# print("============================anaknya =======================================================")
# print(parent1)
# print(parent2)
# child= crossover(parent1,parent2,pcross)
# print(child)
# best_krom=[]
# for i in range(1, uk_tour):
#     p=populationbaru[random.randint(0,popsize-1)]
#     print("coba")
#     if (len(best_krom) == 0) or fitnesss(p)>fitnesss(best_krom):
#         best_krom=p
#         print(best_krom)



# print(best_krom)
# print(np.max(best_krom))


# krom = fitnesss(populationbaru)
# print (krom)
# parent1=tournamentSelection(populationbaru,uk_tour,popsize)
# print ("ini parent")
# print(parent1)

#print(fitnesss(populationbaru))
# print("ini maks ")
# print(np.max(fitnesss(populationbaru)))







# print(nampungencoding(populationbaru))
# for i in range (popsize+1):
#     print(fitnesss(populationbaru[i]))

# print("Ini Maks ")
# print(fitnesss(max(populationbaru)))

#print(nampungencoding(populationbaru))


# encodingKromosom(new_pop)
# pupulasi = generatePopulation()
# print(pupulasi)

# for i in range(popsize):
#     print(encodingKromosom(pupulasi))


#arr_fitness = encodingKromosom(new_pop)
#print(arr_fitness)

population = generatePopulasi(popsize)
for i in range(generation):
    fungsfitness= hasilfitnesss(populationbaru)
    new_pop = []

    bestfitness=getElitisme(fungsfitness)
    new_pop.append(populationbaru[bestfitness])
    new_pop.append(populationbaru[bestfitness])
    i=0
    while (i<popsize-1):
        parent1 = tournamentSelection(populationbaru,toursize,popsize)
        parent2 = tournamentSelection(populationbaru,toursize,popsize)
        while (parent1==parent2):
            parent2 = tournamentSelection(populationbaru,toursize,popsize)
        coppar1= copy.deepcopy(parent1)
        coppar2= copy.deepcopy(parent2)
        child= crossover(coppar1,coppar2,pcross)
        child= mutation(child[0],child[1],pmutate)
        new_pop += child
        i+=2
    populationbaru= new_pop
fungsfitness= hasilfitnesss(populationbaru)
result =getElitisme(fungsfitness)
totalgen=totalgen+generation

print("")
print("========================================================================================")
print('           HASIL MINIMASI FUNGSI  ')
print()
print('Kromosom terbaik:', populationbaru[result])
print('Nilai Fitness terbaik :', fitnesss(populationbaru[result]))
print('Hasil decode    :', encodingKromosom(populationbaru[result]))
print("copy")
print("========================================================================================")
