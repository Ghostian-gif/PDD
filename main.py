
'''Considérese que vamos a armar un computador con cuatro componentes
(núcleo, tarjeta madre, tarjeta gráfica, y refrigeración). la confiabilidad
del sistema se puede mejorar si se instalan varias unidades paralelas
en uno o más de los componentes. La siguiente tabla muestra la probabilidad
de que los respectivos componentes funcionen si constan de una, dos o tres
unidades paralelas:
UNIDADES  |         Probabilidades de funcionamiento
PARALELAS |  Targeta  grafica | Núcleo | Refrigeración | Targeta Madre
__________|___________________|________|_______________|_______________
          |                   |        |               |
     1    |        0.5        |   0.6  |      0.7      |     0.5
__________|___________________|________|_______________|_______________
          |                   |        |               | 
     2    |        0.6        |   0.7  |      0.8      |     0.7
__________|___________________|________|_______________|_______________
          |                   |        |               |  
     3    |        0.8        |   0.8  |      0.9      |     0.9
__________|___________________|________|_______________|_______________

La probabilidad de que el sistema funcione es el producto de las probabilidades
de que los componentes respectivos funcionen.
- En la siguiente tabla se presenta el costo (en miles de dólares) de instalar
una, dos o tres unidades paralelas en los componentes respectivos:
UNIDADES  |                          Costos
PARALELAS |  Targeta  grafica | Nucleo | Refrigeracion | Targeta Madre
__________|___________________|________|_______________|_______________
          |                   |        |               |
     1    |        1          |    2   |       1       |      2
__________|___________________|________|_______________|_______________
          |                   |        |               | 
     2    |        2          |    4   |       3       |      3 
__________|___________________|________|_______________|_______________
          |                   |        |               |  
     3    |        3          |    5   |       4       |      4
__________|___________________|________|_______________|_______________

- Dadas las limitaciones de presupuesto se puede gastar un máximo de $10000.
Use programación dinámica para determinar cuántas unidades paralelas debe 
instalar en cada uno de los cuatro componentes para maximizar la probabilidad
de que el sistema funcione.
Ejercicio tomado de: https://www.youtube.com/watch?v=RfvHxUb5Zuo
'''
#Solucion del ejercicio

'''Se crea una matriz que guarde los datos de la tabla Probabilidad de funcionamiento.'''
MatrizProba = [[0.5,0.6,0.7,0.5],[0.6,0.7,0.8,0.7],[0.8,0.8,0.9,0.9]]
'''Se crea una matriz que guarde los datos de la tabla Costos.'''
MatrizCosto = [[1,2,1,2],[2,4,3,3],[3,5,4,4]]
'''Se define el presupuesto que tenemos'''
Presupuesto=10000
'''Para empezar a hacer el ejercicio se van a crear ciclos donde van a ser
las etapas del ejercicio según la programación dinámica probabilística, 
que van a ser la ruta que va a seguir para maximizar la probabilidad, va a
ser un ciclo por cada componente'''
CicloA=[]
CicloB=[]
CicloC=[]
CicloD=[]
'''Toca tener en cuenta que como son tres probabilidades el cilclo se va a
abrir en ese numero de opciones, entonces el tamaño del ciclo 1 es 3, el ciclo 2 es 9, 
el ciclo 3 es 27, y el ciclo 4 es 81, se inicializan esos valores'''

n1=3
n2=pow(n1,2)
n3=pow(n1,3)
n4=pow(n1,4)
'''Lo siguiente es que por cada posición va a haber 3 valores en todos los
ciclos, el primer valor es el presupuesto que va quedando, el segundo valor es
la probabilidad del componente, y el tercer valor es la ruta'''
m=3
'''Se van a crear las matrices segun sus respectivos tamaños'''
'''CicloA'''
for f in range(n1):
  CicloA.append([])
  for c in range(m):
    CicloA[f].append(None)
    CicloA[f][c]=0
'''CicloB'''
n2=pow(n1,2)
for f in range(n2):
  CicloB.append([])
  for c in range(m):
    CicloB[f].append(None)
    CicloB[f][c]=0
'''CicloC'''
for f in range(n3):
  CicloC.append([])
  for c in range(m):
    CicloC[f].append(None)
    CicloC[f][c]=0
'''CicloD'''
for f in range(n4):
  CicloD.append([])
  for c in range(m):
    CicloD[f].append(None)
    CicloD[f][c]=0
'''Lo Siguiente es llenar los respectivos datos'''
'''Ciclo A: se puede ver que va a ser el presupuesto menos el precio del componente 1,
además de su probabilidad y la ruta'''
cont=0;
for f in range(n1):
  CicloA[f][0]=Presupuesto-(MatrizCosto[f][0]*1000)
  CicloA[f][1]=MatrizProba[f][0]
  cont=cont+1
  CicloA[f][2]=cont
'''Ciclo B: se puede ver que va a ser el presupuesto que queda de A menos el precio del
componente 2, además de su probabilidad y la ruta
'''
j=0
i=0
cont=0;
for f in range(n2):
  if j==3:
    j=0
    i=i+1
  CicloB[f][0]=CicloA[i][0]-(MatrizCosto[j][1]*1000)
  CicloB[f][1]=MatrizProba[j][1]
  cont=cont+1
  CicloB[f][2]=cont
  j=j+1
'''Ciclo C: se puede ver que va a ser el presupuesto que queda de B menos el precio del 
componente 3, además de su probabilidad y la ruta
'''
i=0
j=0
cont=0;
for f in range(n3):
  if j==3:
    j=0
    i=i+1
  CicloC[f][0]=CicloB[i][0]-(MatrizCosto[j][2]*1000)
  CicloC[f][1]=MatrizProba[j][2]
  cont=cont+1
  CicloC[f][2]=cont
  j=j+1
'''Ciclo D: se puede ver que va a ser el presupuesto que queda de C menos el precio
del componente 4, además de su probabilidad y la ruta'''
i=0
j=0
cont3=0;
for f in range(n4):
  if j==3:
    j=0
    i=i+1
  CicloD[f][0]=CicloC[i][0]-(MatrizCosto[j][3]*1000)
  CicloD[f][1]=MatrizProba[j][3]
  cont3=cont3+1
  CicloD[f][2]=cont3
  j=j+1
'''Lo siguiente va a ser devolvernos hasta el valor que nos va a dar la probabilidad
del sistema'''
'''Entonces vamos a llamar el devolvernos como sus respectivos ciclos mas el valor
de '1' '''
'''Se va a llamar CicloAr, CicloBr, CicloCr'''
CicloCr=[]
CicloBr=[]
CicloAr=[]
'''Lo siguiente es que por cada posición va a haber 3 valores en todos los
ciclos, el primer valor es el contador del ciclo, el segundo valor es
la probabilidad del componente agrupado que va a ser igual a la probabilidad mayor
dentro del rango de probabilidades por la probabilidad actual de dicha semejanza
(por ejemplo, Ciclo C*Ciclo Cr en sus probabilidades), y el tercer valor es la ruta'''
'''Se van a crear las matrices segun sus respectivos tamaños'''
'''CicloCr'''
for f in range(n3):
  CicloCr.append([])
  for c in range(m):
    CicloCr[f].append(None)
    CicloCr[f][c]=0
'''CicloBr'''
for f in range(n2):
  CicloBr.append([])
  for c in range(m):
    CicloBr[f].append(None)
    CicloBr[f][c]=0
'''CicloAr'''
for f in range(n1):
  CicloAr.append([])
  for c in range(m):
    CicloAr[f].append(None)
    CicloAr[f][c]=0
'''Lo siguiente va a ser buscar la probabilidad más alta del cuarto componente
entre su respectivo rango de probabilidades en la matriz D, teniendo en cuenta que 
si el presupuesto final es negativo, se coloca la probabilidad -1 para que no se 
tome en cuenta en la ruta
'''
'''CicloCr'''
i=0
j=0
o=3
aux=0
cont2=0
cont=1
for f in range(n3):
  mayor=0
  cont2=0
  while j<o:
    if CicloD[j][1]>mayor and CicloD[j][0]>=0:
      mayor=CicloD[j][1]
      aux=j
    else:
      cont2=cont2+1
    j=j+1
  if cont2!=3:
    o=o+3
    CicloCr[f][0]=cont
    CicloCr[f][1]=CicloD[aux][1]
    CicloCr[f][2]=CicloD[aux][2]
    
  else:
    o=o+3
    CicloCr[f][0]=cont
    CicloCr[f][1]=-1
  cont=cont+1
'''Lo siguiente va a ser buscar la probabilidad mas alta de la matrizCr 
multiplicada por la Matriz C, que nos va a representar el tecer componente
mas el cuarto entre su respectivo rango de probabilidades en la matrizC*Cr'''
'''CicloBr'''
i=0
j=0
o=3
cont2=0
cont =1
for f in range(n2):
  mayor=0
  cont2=0
  while j<o:
    if CicloCr[j][1]*CicloC[j][1]>mayor and CicloC[j][0]>=0:
      mayor=CicloCr[j][1]*CicloC[j][1]
      aux=j
    else:
      cont2=cont2+1
    j=j+1
  if cont2!= 3:
    o=o+3
    CicloBr[f][0]=cont
    aux2=CicloC[aux][1]*CicloCr[aux][1]
    aux2=round(aux2*1000)/1000
    CicloBr[f][1]=aux2
    CicloBr[f][2]=CicloC[aux][2]
  else:
    o=o+3
    CicloBr[f][0]=cont
    CicloBr[f][1]=-1
  cont=cont+1
'''Lo siguiente va a ser buscar la probabilidad mas alta de la matrizBr 
multiplicada por la Matriz B, que nos va a representar el tecer componente
mas el cuarto entre su respectivo rango de probabilidades en la matrizB*Br'''
'''CicloAr'''
i=0
j=0
o=3
cont=1
for f in range(n1):
  mayor=0
  while j<o:

    if CicloBr[j][1]*CicloB[j][1]>mayor and CicloB[j][0]>=0:
      mayor=CicloBr[j][1]*CicloB[j][1]
      aux=j
    j=j+1
  o=o+3
  CicloAr[f][0]=cont
  aux2=CicloB[aux][1]*CicloBr[aux][1]
  aux2=round(aux2*1000)/1000
  CicloAr[f][1]=aux2
  CicloAr[f][2]=CicloB[aux][2]
  cont=cont+1
'''Se define la maxima probabilidad segun el cicloAr, multiplicando las probabilidades
entre Ar y A, y mirando la probabilidad mas alta'''
mayor=0;
f=0
for f in range(n1):
  if CicloAr[f][1]*CicloA[f][1]>mayor:
    mayor=CicloAr[f][1]*CicloA[f][1]
    aux=f
mayor=round(mayor*10000)
mayor=mayor/100
print(mayor, "% de probabilidad máxima de que el sistema funcione")
'''Calcular la ruta'''
'''Se crea la matriz ruta'''
Ruta=[]
for f in range(4):
  Ruta.append([])
  Ruta[f]=0
'''Se obtiene la ruta devolviendose en los procesos segun la probabilidad maxima'''
Ruta[0]=CicloA[aux][2]
Ruta[1]=CicloAr[Ruta[0]-1][2]
Ruta[2]=CicloBr[Ruta[1]-1][2]
Ruta[3]=CicloCr[Ruta[2]-1][2]
print("La ruta para comprar los componentes según calidad con el presupuesto dado es: ")
print(Ruta)
'''Lo siguiente va a ser especificar el componente (nucleo, targeta madre, targeta grafica
, y refrigeración) a comprar segun la ruta'''
Ruta2=[]
for f in range(4):
  Ruta2.append([])
  Ruta2[f]=0
Ruta2[0]=CicloA[Ruta[0]-1][1]
Ruta2[1]=CicloB[Ruta[1]-1][1]
Ruta2[2]=CicloC[Ruta[2]-1][1]
Ruta2[3]=CicloD[Ruta[3]-1][1]
'''Para el nucleo'''
if Ruta2[0]==0.8:
  print("El nucleo va a necesitar ",3," unidades paralelas para maximizar su funcionalidad con un presupuesto de ",Presupuesto," Dolares")
elif Ruta2[0]==0.6:
  print("El nucleo va a necesitar ",2," unidades paralelas para maximizar su funcionalidad con un presupuesto de ",Presupuesto," Dolares")
elif Ruta2[0]==0.5:
  print("El nucleo va a necesitar ",1," unidades paralelas para maximizar su funcionalidad con un presupuesto de ",Presupuesto," Dolares")
'''Para la targeta madre'''
if Ruta2[1]==0.8:
  print("La targeta madre va a necesitar ",3," unidades paralelas para maximizar su funcionalidad con un presupuesto de ",Presupuesto," Dolares")
elif Ruta2[1]==0.7:
  print("La targeta madre va a necesitar ",2," unidades paralelas para maximizar su funcionalidad con un presupuesto de ",Presupuesto," Dolares")
elif Ruta2[1]==0.6:
  print("La targeta madre va a necesitar ",1," unidades paralelas para maximizar su funcionalidad con un presupuesto de ",Presupuesto," Dolares")
'''Para la targeta grafica'''
if Ruta2[2]==0.9:
  print("La targeta grafica va a necesitar ",3," unidades paralelas para maximizar su funcionalidad con un presupuesto de ",Presupuesto," Dolares")
elif Ruta2[2]==0.8:
  print("La targeta grafica va a necesitar ",2," unidades paralelas para maximizar su funcionalidad con un presupuesto de ",Presupuesto," Dolares")
elif Ruta2[2]==0.7:
  print("La targeta grafica va a necesitar ",1," unidades paralelas para maximizar su funcionalidad con un presupuesto de ",Presupuesto," Dolares")
'''Para la refrigeracion'''
if Ruta2[3]==0.9:
  print("La refrigeración va a necesitar ",3," unidades paralelas para maximizar su funcionalidad con un presupuesto de ",Presupuesto," Dolares")
elif Ruta2[3]==0.7:
  print("La refrigeración va a necesitar ",2," unidades paralelas para maximizar su funcionalidad con un presupuesto de ",Presupuesto," Dolares")
elif Ruta2[3]==0.5:
  print("La refrigeración va a necesitar ",1," unidades paralelas para maximizar su funcionalidad con un presupuesto de ",Presupuesto," Dolares")