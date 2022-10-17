#Llista en python
print("lista de 6 numeros")
a=(57, 7, 98,4,13,45)
print(a)

print("lista de  String")
b=["hola", " chau","buen dia","hola","pluma"]
print(b)

print("longitus de la lista")
n=len(a)
print(n)

#para acceder a sus elementos, se debe 
#utilizar el[]
#los indices comnienzan en 0

print("el elemento con indice 0 de la lista: ")
print(b[0])
print("el elemento con indice 1 de la lista: ")
print(b[1])
print("el elemento con indice 2 de la lista: ")
print(b[2])

vaciar=[]
print("lista vacia")
print(vaciar)

#crear sublistas
print("el elemento del indice 0 al 1(2-1): ")
print(a[0:2])
print("el elemneto del indice 1 al 3 (4-1): ")
print(a[1:4])

#agregar un elemento a la lista 
print("una lista con 5 string")
a=['una', 'lista','de']
print(a)

print("La misma lista luego de agregar un string más")
a.append('numeros')
a.append('mayores')
print(a)

#Tuplas son las listas, pero no se puede modificar, son listas de solo lectura

a=(1,2,3,4)
print("una tupla de 4 elementos: ")
print(a)
print("los elementos con indice 2: ")
print(a[1])
print("los elementos entre los indices 0 y 2: ")
print(a[0:2])

#sentencias  if
edad=25
print("la persona es")
if edad < 18:
    print("menor")
else:
  
  print("mayor")

print("de edad ")
 
 #Subjects
subjects=["Matematicas","fisica","quimica","historia"]
scores=[]
for subjects in subjects :
    score=input("Que nota has sacado"+ subjects + "?") 
    scores.append(score)
for i in range(len(subjects)):
    print("En"+ subjects[i]+ "has echo"+ score [1])


        
  