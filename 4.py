# diccionarios son esrtucturas de datos 

# prueba_deportiva = {'Jorge':500,'Diana':600,'Rodrigo':700,'axel':900,'brandon':100,}

# #simplificar
# nota =prueba_deportiva

# print(nota['Rodrigo'])

# print(nota['axel'])

# print(nota['Jorge'])

# print(nota['Diana'])

# import random
# clientes = ["Alex","Bob","Carol","Dave","Flow", "Katie","Nate"]
# diccionario_descuentos  = {cliente:random.randint(1,100) for cliente in clientes}

# print(diccionario_descuentos)

# {'Alex':16,'Bob':26,'Carol':83,'Dave':21,'Flow':45, 'Katie':5,'Nate':9}


dl={
    "Nombre":"sara",
    "Edad":27,
    "documento":1008882
}
print(dl)

# d2=dict([
#     ('nombre','sara'),
#     ('Edad', 27),
#     ('documento',1008882)
# ])
# print(d2)

# d3=dict(nombre='sara',
#     Edad= 27,
#     documento=1003882)

# print(d3)

#metodo get
# print(dl['Nombre']) 
# print(dl.get('Nombre'))

dl['Nombre'] = "Laura"
print (dl)


dl['Direccion'] = "Calle 123"
print (dl)

# for x in dl:
#     print(x)

# for x in dl:
#     print(dl[x])

#imprimir ambos datos por medio del item
for x, y in dl.items():
    print(x,y)