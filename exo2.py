from random import randint
import numpy as np
from math import sqrt

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

#def puissanceItere(seuil, A):
 #   i = 0
  #  while (e > seuil):



def suite(X:np.array,A):
    X = A*X/abs(A*X)

# A est la matrice
# l est notre precision
# X valeur de Xn
# x valeur de xn - 1
"""def puissanceItere(l,A):
   X = np.array([randint(-10,10),randint(-10,10)])
   aLambda = 0
   Lambda = 0
   while ((Lambda-aLambda) > l):
       aLambda = Lambda
       X = A * X # approximation du vecteur propre associé
       Lambda = X / norme(X) # approximation de lambda
   return X"""

def puissanceItere(l,A:np.array):
   #X = np.array([randint(-10,10),randint(-10,10)])
   #X = np.array([1,1,1,1]) 
   #print(A.shape[0])
   X = np.array([randint(1,10) for x in range (A.shape[0])])
   #print (int(np.sqrt(len(A)))+1,X)
   Lambda = 0
   while (True):
       aLambda = Lambda
       AX = np.dot(A,X) # approximation du vecteur propre associé
       Lambda = norme(AX) # approximation de lambda
       X = AX / Lambda
       if (abs(Lambda - aLambda) < l ):
           return X,Lambda


C2 = np.array([[2, 3], [1, 0]])
X, Lambda = puissanceItere(1e-6, C2)
print("Vecteur propre approximé :", X)
print("Valeur propre approximée :", Lambda)
print("--------------------------------------")
C3 = np.array([[4,1,0], [1,3,1], [0,1,2]])
X, Lambda = puissanceItere(1e-6, C3)
print("Vecteur propre approximé :", X)
print("Valeur propre approximée :", Lambda)
print("--------------------------------------")
C4 = np.array([[4, 1, 0, 0],[1, 3, 1, 0],[0, 1, 2, 1],[0, 0, 1, 1]])
X, Lambda = puissanceItere(1e-6, C4)
print("Vecteur propre approximé :", X)
print("Valeur propre approximée :", Lambda)

