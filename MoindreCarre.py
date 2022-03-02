#Methode des moindre carre par descente du gradient

import matplotlib.pyplot as plt

############################################################################
#Paramètre du programe

eps = 0.00000001; #condition d'arret recherche
h = 0.0001 #pas de la recherche

par0 = [0,0,0] #parametre initiaux

############################################################################
#création des points

x = []; y=[]; sigma = []
x0 = -2
m = 1

for i in range(10):
	x.append(x0 + i*m)
	y.append(-x[i]**2 + 2*x[i] + 1)
	sigma.append(1)


############################################################################ OK
#fonction lier au polynome d'interpolation

#crée une fonction polynomiale avec une liste de parametre coefficient
def poly(x,par): 
	S = 0
	for k in range(len(par)):
		S = S + par[k]*(x**k)
	return(S)

#cree un vecteur gradient de la fonction poly
def gradpoly(x,par):
	grd = [0]
	for k in range(len(par)-1):
		grd.append(x**(k+1))
	return(grd)

#calcul de l'erreur carre du polynome por rapport aux valeurs
def X2(x,y,sigma,par):
	S = 0
	for i in range(len(x)):
		f = poly(x[i],par) #calcul de la valeur du polynome
		S = S + ((f - y[i])/sigma[i])**2
	return(S)

#calcul du gradient de l'erreur carre
def gradX2(x,y,sigma,par):
	S = []
	for j in range(len(par)): S.append(0)

	for i in range(len(x)):
		grd = gradpoly(x[i],par)
		g = (poly(x[i],par) - y[i]) / (sigma[i]**2)

		for j in range(len(par)):
			S[j] = S[j] + 2*g*grd[j]
	return(S)

#calcul dela norme de gradX2
def normeGradx2(x,y,sigma,par):
	grd = gradX2(x,y,sigma,par)
	S = 0
	for i in range(len(grd)): 
		S = S + grd[i]**2
	return(S)

"""
cree un objet avec parametre pour appeler les methodes voulu sur x et economiser RAM
sortir x2 de la somme
"""

############################################################################
#methode descente du gradient

p = par0

while (normeGradx2(x,y,sigma,p) > eps):
	grd = gradX2(x,y,sigma,p)
	for i in range(len(grd)): p[i] = p[i] - h*grd[i]
	print(p)

"""
afficher erreur
"""	

############################################################################
# création de la courbe d'interpolation

N = 200
a = x[0]; b = x[-1]
h = (b-a)/N

X= []
Y = []

for i in range(N):
	xi = a+h*i
	yi = poly(xi,p)
	Y.append(yi)
	X.append(xi)

############################################################################
#Affichage
plt.plot(x,y,"ko")
plt.plot(X,Y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
