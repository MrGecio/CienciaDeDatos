
#Repaso Pyhton Diccionarios Ciencia de Datos 
#Briseño Gutierrez German 21140765


import time

#Ejercicio 1

#Codgo que recorra cada persona e imprima cuantos libros han leido 
# si alguieen no a leido imprimir ___no ha leido ningun libro en lugar del numero de libros leidos 


def librosLeidos( people, books_read ):
    index = 0
    for i in books_read :
        if i > 0:
            print(people[index] + " ha leido "+ str(i) + " libros")
                        
        else:
            print(people[index] + " no ha leido ningun libro!")
        index = index +1
        
#Ejercicio 1 y 2
#
# Solucion por uso de ciclos con tuplas 
# 
# for b , pin zip( people, books_read
#   if b == 0
#       print no ha leido libros
#    else ha leido tantos    
# 
#Se uso el metodo   zip() 
#
# #


def podio(people, books_read ):  
    podium = []  
    index = 0
    podium = books_read
    podium.sort(reverse = True)
    
    while len(podium)> 3:
        podium.pop()
    
    print("\nPodio:\n")
    for i in books_read:
        for o in podium:
            if i == o:
                index = books_read.index(i)
                print(people[index] + " ha leido "+ str(i) + " libros")
#
# Ejercicio 3 
# Solucion
# 
# book_tuples = [(b,p )for b, p in zip ( nooks_read, people)]
# 
# 
# #                



#
# otra solucion
#usando splits
#
#for b,p in sorted(book_tuples, reverse=True)[:3]: 
#   print(f'{p} has read{b} books')
# 
# 
# 
# #
                        
def multiploDe3Bono(people, books_read):
    index = 0
    for i in books_read:
        faltan = 3 - (i%3)
        if i >= 3:
            if i % 3 == 0:
                print(people[index] + " tiene "+ str(int(i/3)) + " bonos y le faltan 3 libros para conseguir su siguiente bono")
            else:
                print(people[index] + " tiene "+ str(int(i/3)) + " bonos y le faltan "+str(faltan)+ " libros para conseguir su siguiente bono")
        elif 0<i<3:
            print(people[index] + " no tiene ningun bono y le faltan "+ str(faltan)+" para conseguir su primer bono")
        else:
            print(people[index] + " no tiene ningun bono y le faltan 3 para conseguir su primer bono")
         
        index = index +1

def diccionarioLibros(Reads):
    
    ordenados = sorted(Reads.items(), key=lambda x: x[1], reverse=True)
    for i in range(3):
        nombre, cantidad = ordenados[i]
        print(f"{nombre} ha leido {cantidad} libros")


def duplicados(Reads):
    nombres_unicos = set(Reads)
    if len(Reads) != len(nombres_unicos):
        print("Se encontraron nombres duplicados en la lista original")
    else:
        print("No hay duplicados")
    return(nombres_unicos)


people = ['Krishnang', 'Steve', 'Jimmy', 'Mary', 'Divya', 'Robert', 'Yulia', 'German']
books_read = [12, 6, 0, 7, 4, 10, 15, 4]

#Ejercicio 2

# Convierte el bucle que acabas de crear en una función que tome las dos listas
#(libros leídos y personas) como argumentos. Asegúrate de probar la función para
#comprobar su correcto funcionamiento.
    
librosLeidos(people, books_read)

#Ejercicio 3

#Ordena los valores de books_read de mayor a menor e imprime las tres personas
#que más libros han leído, indicando cuantos.


podio(people, books_read)

#Ejercicio 4

#La librería Gandhi recibe un descuento por cada múltiplo de 3 que sus empleados
#compran y leen. Averigua cuántos múltiplos de 3 han leído y cuántos libros más les
#faltan para llegar al siguiente múltiplo de 3. 

multiploDe3Bono(people, books_read)

#Ejercicio 5

#Crea un diccionario para los datos donde las claves sean los nombres de las
#personas y los valores sean la cantidad de libros.

Reads = {'Krishnang':12, 'Steve':6, 'Jimmy':0, 'Mary':7, 'Divya':4, 
         'Robert':10, 'Yulia':15, 'German':4, 'Jimmy' : 0}

#Ejercicio 6

#Desafío: usa el diccionario para imprimir los nombres de las 3 personas con más
#libros leídos

diccionarioLibros(Reads)

#Ejercicio 7

#Usando conjuntos, asegúrese de que no haya nombres duplicados en nuestros
#datos. (Sí, esto es trivial, ya que nuestros datos son pequeños y podemos
#inspeccionarlos manualmente, pero si tuviéramos miles de nombres, podríamos usar
#el mismo método que aquí).

print(duplicados(Reads))

#Ejercicio 8

#Crea una clase para almacenar los libros leídos y los nombres de las personas. La
#clase también debe incluir una función para imprimir los tres libros más leídos.
#Prueba la clase para comprobar su funcionamiento.

class gestorDeLectura:
    
    def __init__(self, nombres, libros):
        self.datos = dict(zip(nombres, libros))
    
    def salidaBonita(self):
        for nombre, valor in self.datos.items():
            print(nombre +"---------"+ str(valor)+" books")
    
    def podioClase(self):
        ordenados = sorted(self.datos.items(), key=lambda item: item[1], reverse=True)
        podium = ordenados[:3]

        print("\nPodio Clase:\n")
        for i, (nombre, cantidad) in enumerate(podium, start=1):
            print(nombre+" " + str(cantidad) + " libros")


inicio = time.time()
mi_gestion = gestorDeLectura(people, books_read)
mi_gestion.salidaBonita()
mi_gestion.podioClase()
print("\n\n")
#Ejercicio 9

#Utiliza el módulo time para ver cuánto tiempo lleva crear una nueva clase e
#imprimir los tres mejores lectores.
fin = time.time()
tiempoTotal = fin - inicio
print("tiempo de ejecucion" +str(tiempoTotal)+" : segundos")


#Ejercicio 10

#El siguiente fragmento de código presenta algunos errores. Depura y corrije el error
#para que el código se ejecute.


for b,p in list(zip(books_read,people))[:3]:
    if b > 0 and b < 10:
        print(str(p) + "has only read "+str(b)+' books')
        
        
#Ejercicio 11

#Modifica el código de manera que la salida se vea así:

