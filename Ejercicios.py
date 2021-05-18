frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt

lista_frutas=frutas.read().split("\n")#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=numeros.read().split("\n")#Llenar las lista con los datos del archivo numeros.txt
frutas.close()
numeros.close()

#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas: lista , caracter
Salidas: lista
"""
def eliminar_un_caracter_de_toda_la_lista(lista , caracter):
    for i in list(range(0,len(lista))):
        lista[i]=str(lista[i]).replace(caracter.lower(), "").replace(caracter.upper(), "")
    return lista
#Realizar una funcion que retorne la copia de una funcion que pasa por parametro 
"""
Entradas: lista
Salidas: copia de la lista
"""
def copia_lista(lista):
    return lista.copy() 
#Realizar una funcion que retorne una lista de numeros numeros pares   
"""
Entradas: lista
Salidas: lista números pares
"""  
def numeros_pares(lista):
    lista_pares=[]
    for i in list(range(0,len(lista))):
        if (float(lista[i]) % 2) == 0 and (float(lista[i]) >= 2 or float(lista[i]) <=-2): 
            lista_pares.append(lista[i])
    return lista_pares
#Realizar una funcion que elimine un elemento de una lista
"""
Entradas: Lista frutas, Elemento a eliminar
Salidas: Lista menos un elemento
"""  
def elimina_elemento_lista(lista , elemento):
    if elemento in lista:
        lista.remove(elemento)
    else:
        print("No se eliminó elemento porque no fue encontrado en la lista.")
    return  lista

#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas: Lista, letra inicial (puedes ser mayúscula o minúscula)
Salidas: Lista de frutas que inician con la letra dada.
"""  
def letra(lista , letra):
    lista_palabras=[]
    for i in list(range(0,len(lista))):
        if len(str(lista[i])) > 0:
            if str(lista[i])[0].lower() == letra.lower() : 
                lista_palabras.append(lista[i])
    return lista_palabras
#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas: Lista
Salidas: Longitud de la lista
"""   
def tamano_lista(lista):
    return len(lista)
#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas: Lista
Salidas: lista con tamaño, lista con tipo de dato para cada campo de la lista
"""  
def informacion_lista(lista):
    lista_tipos_dato=[]
    for i in list(range(0,len(lista))):
        lista_tipos_dato.append(type(lista[i]))
    return [len(lista) , lista_tipos_dato ] 
#Retornar una lista con los numero negativos  
"""
Entradas: Lista
Salidas: Lista con los números negativos
"""  
def numeros_negativos(lista):
    lista_negativos=[]
    for i in list(range(0,len(lista))):
        if float(lista[i]) < 0: 
            lista_negativos.append(lista[i])
    return lista_negativos

#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
"""
Entradas: Lista
Salidas: lista de posiciones en donde esté el parametro dado
""" 
def posicion_elemento(lista , elemento):
    lista_posiciones = []
    for i in list(range(0,len(lista))):
        if str(lista[i]) == str(elemento): 
            lista_posiciones.append(i)
    return lista_posiciones#[0] #en caso de que sea solo el primer elemento encontrado

#realizar una funcion que agregue al final de archivo frutas una fruta
"""
Entradas: Lista , nueva fruta
Salidas: lista de frutas con la nueva fruta añadida
""" 
def frutas(lista , elemento):
    lista.append(elemento)
    return lista
  
#Realizar una funcion que cuente el numero de veces que se repite un elemento 
"""
Entradas: Lista, elemento
Salidas: número de veces que se repite el elemento
"""  
def repetir(lista , elemento):
    lista_posiciones = []
    for i in list(range(0,len(lista))):
        if str(lista[i]) == str(elemento): 
            lista_posiciones.append(i)
    return len(lista_posiciones)
  
if __name__ == "__main__":

    print("Lista frutas: ", lista_frutas)
    print("\n")
    print("Lista numeros: ", lista_numeros)

    print("\n")
    print("\n")
    print("Todas las funciones que se van a validar serán sobre las listas originales")
    print("\n")
    print("\n")
    print("Función que elimina un caracter de la lista")
    print("Ingrese caracter a eliminar de la lista de frutas:")
    caracter = input()
    frutas_sin_caracter = eliminar_un_caracter_de_toda_la_lista(lista_frutas, caracter)
    print("Lista frutas sin caracter:", frutas_sin_caracter)
    print("\n")
    print("Digite cualquier letra y de enter para continuar:")
    Aux = input()
  
    print("\n")
    print("\n")
    print("Se realiza función que copia lista de frutas")    
    copy=copia_lista(lista_frutas)
    print("Lista copiada", copy)
    print("\n")
    print("Digite cualquier letra y de enter para continuar:")
    Aux = input()
    
    print("\n")
    print("\n")
    print("Se realiza función que lista los números pares")  
    lista_numeros_pares = numeros_pares(lista_numeros)
    print("Lista numeros pares:", lista_numeros_pares)

    print("\n")
    print("\n")
    print("Se realiza función que elimina un elemento de la lista")  
    print("Ingrese el elemento a eliminar de la lista de frutas:")
    elemento = input()   
    lista_sin_elemento = elimina_elemento_lista(lista_frutas, elemento)
    print("Lista sin elemento:", lista_sin_elemento)
 
    print("\n")
    print("\n")
    print("Se realiza función que lista las frutas que inician con la letra dada") 
    print("Elije la letra inicial que deben tener la lista de frutas:")
    elemento = input()    
    lista_letra = letra(lista_frutas , elemento)
    print("Lista de frutas con esa letra inicial:", lista_letra)
    print("\n")
    print("Digite cualquier letra y de enter para continuar:")
    Aux = input()

    print("\n")
    print("\n")
    print("Función para ver el tamaño de la lista")
    tamano_list = tamano_lista(lista_frutas)
    print("El tamaño de la lista es: ", tamano_list)
    print("\n")
    print("Digite cualquier letra y de enter para continuar:")
    Aux = input()
 
    print("\n")
    print("\n")
    print("Función para ver información de la lista:")
    info_lista = informacion_lista(lista_frutas)
    print("Matriz de información de lista frutas, tamaño y tipos de dato:", info_lista)
    print("\n")
    print("Digite cualquier letra y de enter para continuar:")
    Aux = input()
    
    print("\n")
    print("\n")
    print("Función para extraer lista con numeros negativos:")    
    list_negativos = numeros_negativos(lista_numeros)
    print("lista de numeros negativos:",list_negativos)

    print("\n")
    print("\n")
    print("Se realiza función obtener las posiciones en las que se encuentra un elemento")
    print("Ingresa un elemento que quieras revisar en que posiciones está en la lista de frutas:")
    elemento = input() 
    posiciones = posicion_elemento(lista_frutas, elemento)
    print("Matriz de posiciones de elemento en la lista", posiciones)
    
    print("\n")
    print("\n")
    print("Se realiza función para ingresar un elemento a la lista")
    print("Ingresa un elemento que quieras agregar a la lista de frutas:")
    elemento = input() 
    lista_con_elemento = frutas(lista_frutas, elemento)
    print(lista_con_elemento)

    print("\n")
    print("\n")
    print("Se realiza función que cuenta el número de veces que se repite un elemento en la lista")
    print("Ingresa un elemento que quieras cuantas veces se repite en la lista de numeros:")
    elemento = input()
    numero_repeticiones = repetir(lista_numeros, elemento)
    print(numero_repeticiones)