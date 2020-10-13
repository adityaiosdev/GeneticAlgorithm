import random
import copy
import numpy as np


def generateKromosom(uk_krom):
    krom = []  
    for i in range(uk_krom):
        krom.append(random.randint(0,1))      
    
    return krom

