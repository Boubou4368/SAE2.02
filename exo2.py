from random import randint
import numpy as np

#Exercice 2
# 1
def norme(X:np.array):
    sum = 0 
    for x in X:
        sum += x**2
    return np.sqrt(sum)



V = np.array([2,0,0,3])
print(norme(V))

# 2
X = []
for x in range (20):
    X.append(randint(0,1000))
X = np.array(X.sort)

def puissanceItere(seuil, A):
    i = 0
    while (e > seuil):

    

