#------------------------------------------------------------------------
# RECHERCHE DU CHEMIN LE PLUS RAPIDE ENTRE 2 POINTS A ET B
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# PACKAGES
from scipy import optimize as opt # Optimize
import numpy as np                # Numpy
import matplotlib.pyplot as plt   # Pyplot
from matplotlib import cm         # Colormaps
#------------------------------------------------------------------------

#------------------------------------------------------------------------
# POSITION DES POINTS ET DONNEES PHYSIQUES
xa, xb = 0., 1.
ya, yb = 1., 0.
m = 1.  # masse en kg
g = 10. # gravite en ms**-2
#------------------------------------------------------------------------

#------------------------------------------------------------------------



#------------------------------------------------------------------------
# CALCUL DU TEMPS DE PARCOURS
def temps(Y):
  # On calcule l'energie potentielle en supposant qu'elle est nulle en A
  Ep = m * g * (Y - Y[0])
  # On calcule l'energie cinetique 
  Ec = - Ep
  # On calcule la vitesse
  V = (2. / m * Ec) **.5 
  # On calcule la vitesse moyenne sur chaque element
  Ve = (V[1:] + V[:-1]) / 2.
  # On calcule le pas en X:
  dx = X[1] - X[0]
  # On calcule la longueur de chaque element
  Le = ( ( Y[1:] - Y[:-1] )**2 + dx**2)**.5
  # On calcule le temps de parcours par element
  te = Le / Ve
  # On calcule le temps de parcours total
  t = te.sum()
  return t
  
def add_AB(Yc):
  Y = np.zeros([len(Yc) + 2])
  Y[1:-1] = Yc
  Y[0], Y[-1] = ya, yb
  return Y

def temps2(Yc):
  return temps(add_AB(Yc))  
#------------------------------------------------------------------------
 

#------------------------------------------------------------------------
# MISE EN APPLICATION

manual = False # Mode de fonctionnement: True pour manuel, False pour automatique

# MAILLAGE EN X 
Np = 1 # Nombre de noeuds souhaites
X = np.linspace(xa, xb, Np+2) # Coordonnees en x des noeuds
# COORDONNEES EN Y ?
Y = np.linspace(ya, yb, Np+2) # Altitude des noeuds

#------------------------------------------------------------------------

#------------------------------------------------------------------------
# AFFICHAGE
yp = np.linspace(-.5, .9, 100 )
t =np.zeros_like(yp)
for i in xrange(len(yp)):
  Y[1] = yp[i]
  t[i] = temps(Y)
plt.figure(0)
plt.clf()
plt.plot(yp, t)
plt.grid()
plt.xlabel("$y_0$")
plt.ylabel("$t_f$")
plt.savefig("brachi1d.pdf")


loc = np.where(t == t.min())
Y[1] = yp[loc]
Yl = np.linspace(ya, yb, Np+2) # Altitude des noeuds
tl = temps(Yl)
plt.figure(1)
plt.clf()
plt.plot(X, Y, "og-", label = "$t_f = {0:.2f}$ s".format(t[loc][0]))
plt.plot(X, Yl, "ob-", label = "$t_f = {0:.2f}$ s".format(tl))
plt.grid()
plt.xlabel("Position, $x$")
plt.ylabel("Position, $y$")
plt.legend()
plt.savefig("brachi1d_sol.pdf")  
