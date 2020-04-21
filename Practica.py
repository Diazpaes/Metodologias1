from abc import ABCMeta, abstractmethod
from random import randint, uniform,random
import random

# Ejercicio 1 implementa la interface comparable

class Comparable (metaclass= ABCMeta):
    @abstractmethod
    def sosIgual(self, comparo):
        return self == comparo

    @abstractmethod
    def sosMayor(self, comparo):
        return self < comparo
    
    @abstractmethod
    def sosMenor(self, comparo):
        return self > comparo

# Ejercicio 2 implementa la clase numero
    
class Numero(Comparable):
     
    def __init__ (self, valor):
           self.valor = valor
     
    def get_valor(self):
          return self.valor
    
    def sosIgual(self, comparo):
        return self.valor == comparo.valor


    def sosMayor(self, comparo):
        return self.valor < comparo.valor
    
    def sosMenor(self, comparo):
        return self.valor > comparo.valor

# Ejercicio 3 implementa la interface coleccionable

class Coleccionable(metaclass= ABCMeta):
    @abstractmethod
    def cuantos(self):
        pass
    @abstractmethod
    def minimo(self):
        pass
    @abstractmethod
    def maximo(self):
        pass
    @abstractmethod
    def agregar(self, Comparable):
        pass
    @abstractmethod
    def contiene(self, Comparable):
        pass


# Ejercicio 4 impelemnta la pila la cola y sus metodos heredados
class Pila:
    def __init__(self):
         self.items = []

    def estaVacia(self):
         return self.items == []

    def push(self, item):
         self.items.append(item)

    def pop(self):
         return self.items.pop()

    def inspeccionar(self):
         return self.items[len(self.items)-1]

    def tamano(self):
         return len(self.items)
    
    def cuantos(self):
        return len(self.items)
    
    def minimo(self):
        min_value = self.items[0]
        for i in range(self.cuantos()):
            valor = self.items[i]
            if min_value.sosMenor(valor):
                min_value = valor
        return min_value
    
    def maximo(self):
        max_value = self.items[0]
        for i in range(self.cuantos()):
            valor = self.items[i]
            if max_value.sosMayor(valor):
                max_value = valor
        return max_value

    def agregar(self, Comparable):
        self.items.insert(0, Comparable)
    
    def contiene(self, Comparable):
        encontrado = False
        for i in range(self.cuantos()):
            valor = self.items[i].dni
            if Comparable == valor:
                encontrado = True
                break
        return encontrado


class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)
    
    def pop(self):
         return self.items.pop()

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)
    
    def cuantos(self):
        return len(self.items)
    
    def minimo(self):
        min_value = self.items[0]
        for i in range(self.cuantos()):
            valor = self.items[i]
            if min_value.sosMayor(valor):
                min_value = valor
        return min_value
    
    def maximo(self):
        max_value = self.items[0]
        for i in range(self.cuantos()):
            valor = self.items[i]
            if max_value.sosMenor(valor):
                max_value = valor
        return max_value

    def agregar(self, Comparable):
        self.items.insert(0, Comparable)
    
    def contiene(self, Comparable):
        encontrado = False
        for i in range(self.cuantos()):
            valor = self.items[i].dni
            if Comparable == valor:
                encontrado = True
                break
        return encontrado

# Ejercicio 8 Implementar ColeccionMultiple
class ColeccionMultiple(Coleccionable):
    def __init__(self, p, c):
        self.pilainterna = p
        self.colainterna = c
    
    def cuantos(self):
        return self.pilainterna.cuantos(), self.colainterna.cuantos()
    
    def minimo(self):
        if self.pilainterna.minimo().valor > self.colainterna.minimo().valor :
            min_value = self.pilainterna.minimo().dni
            return min_value
        min_value = self.colainterna.minimo().dni
        return min_value
    
    def maximo(self):
        if self.pilainterna.maximo().valor < self.colainterna.maximo().valor :
            max_value = self.pilainterna.maximo().dni
            return max_value
        max_value = self.colainterna.maximo().dni
        return max_value
    
    def agregar(self, Comparable):
        pass
    
    def contiene(self, Comparable):
        return self.colainterna.contiene(Comparable) or self.pilainterna.contiene(Comparable)

#Ejercicio 11 implementar clase persona
class Persona(Comparable):
    def __init__ (self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
    
     
    def get_nombre(self):
        return self.nombre
    
    def get_dni(self):
        return self.dni
    
    def sosIgual(self, comparo):
        return self.dni == comparo.dni


    def sosMayor(self, comparo):
        return self.dni > comparo.dni
    
    def sosMenor(self, comparo):
        return self.dni < comparo.dni

class  ColeccionMultiplepersona(Coleccionable):
    def __str__(self):
        return f"la coleccion tiene {self.cuantos()}, el dni minimo es {self.minimo()} y el maximo es {self.maximo()}"
    def __init__(self, p, c):
        self.pilainterna = p
        self.colainterna = c
    
    def cuantos(self):
        return self.pilainterna.cuantos(), self.colainterna.cuantos()
    
    def minimo(self):
        if self.pilainterna.minimo().dni < self.colainterna.minimo().dni :
            min_value = self.pilainterna.minimo().dni
            return min_value
        min_value = self.colainterna.minimo().dni
        return min_value
    
    def maximo(self):
        if self.pilainterna.maximo().dni > self.colainterna.maximo().dni :
            max_value = self.pilainterna.maximo().dni
            return max_value
        max_value = self.colainterna.maximo().dni
        return max_value
    
    def agregar(self, Comparable):
        self.items.insert(0, Comparable)

    def contiene(self, Comparable):
        return self.colainterna.contiene(Comparable) or self.pilainterna.contiene(Comparable)

def main():
    # Ejercicio 5 impelmentar llenar
    def llenar (Coleccionable):
        for i in range(20):
            comparable = Numero(randint(0, 9999))
            Coleccionable.agregar(comparable)

    #Ejercicio 12 implementar llenar personas
    def llenarpersonas(Coleccionable):
        listapersonas = ["juan", "pedro", "nicolas", "German", "Damian", "Rocio", "Rosario", "Victoria", "Lucas","Yanina", "Noelia","Camila","Facundo","Patricio","Ignacio", "Florencia","Andrea"]
        for i in range(20):
            comparable = Persona(random.choice(listapersonas),randint(1000000,99999999))
            Coleccionable.agregar(comparable)

    
    # Ejercicio 6 implementa funcion informar

    def informar(coleccionable):
        print(f"el coleccionable tiene:{coleccionable.cuantos()}")
        print(f"el minimo valor es: {coleccionable.minimo().valor}")
        print(f"el maximo valor es: {coleccionable.maximo().valor}")
        
        comparable = int(input("ingrese un numero: "))
        if coleccionable.contiene(comparable):
            print ("el elemento leido esta en la coleccion")
        else:
            print("el elemento leido no esta en la coleccion")
    
    # Ejercicio 13 Implementar funcion Informar personas
    def informarpersona(coleccionable):
        print(f"el coleccionable tiene: {coleccionable.cuantos()}")
        print(f"el minimo numero de dni es: {coleccionable.minimo()}")
        print(f"el maximo numero de dni es: {coleccionable.maximo()}")
        print(coleccionable)
        comparable = int(input("Ingrese un DNI: "))
        if coleccionable.contiene(comparable):
            print ("el DNI leido esta en la coleccion")
        else:
            print("el DNI leido no esta en la coleccion")


    # Ejercicio 7 llena la pila y la cola e invoca la funcion informar
    # Ejercicio 9 crear coleccion multiple e informar 
    # Ejercicio 13 coleccion multiple de personas informada
    cola_1 = Cola()
    Pila_1 = Pila()
    cola_2 = Cola()
    pila_2 = Pila()
    multiple = ColeccionMultiple(Pila_1,cola_1)
    multiple_2 = ColeccionMultiplepersona(pila_2, cola_2)
    llenar(cola_1)
    llenar(Pila_1)
    llenarpersonas(pila_2)
    llenarpersonas(cola_2)
    informar(cola_1)
    informar(Pila_1)
    informar(multiple)
    informarpersona(multiple_2)
    


if __name__ == "__main__":
    main()

