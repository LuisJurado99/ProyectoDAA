class NodoArbol:
    def __init__( self, value, izquierdo = None, centro = None, derecho = None ):
        self.data = value
        self.left = izquierdo
        self.center = centro
        self.right = derecho

class ArbolBinarioBusqueda:
    def __init__( self ):
        self.__root = None

    def insert( self, nodo ):
        if self.__root == None:
            self.__root = nodo

    def transversal( self, nodo = None ):
        print("\t\t\t\t", self.__root.data)
        print("\t\t\t\t\t|")
        print(" ---------------------------------------------------------------")
        print(" |\t\t\t  |\t\t\t\t\t|")
        print(self.__root.left.data, end ="")
        print("\t\t\t", self.__root.center.data, end = "")
        print("\t\t\t\t", self.__root.right.data)
        print(" \t\t\t  |\t\t\t\t\t|")
        print("\t\t ---------------------\t\t\t  -------------")
        print("\t\t |\t  |\t     |\t\t\t  |\t      | ")
        print("\t\t", self.__root.center.left.data, end = "")
        print("\t", self.__root.center.center.data, end = "")
        print("\t", self.__root.center.right.data, end = "")
        print("\t\t", self.__root.right.left.data, end = "")
        print("\t", self.__root.right.center.data)
        print("\t\t\t\t    |\t\t\t\t      | ")
        print("\t\t\t\t  ---------\t\t\t----------")
        print("\t\t\t\t |\t   |\t\t\t|\t |")
        print("\t\t\t\t", self.__root.center.right.left.data, end = "")
        print("\t", self.__root.center.right.center.data, end = "")
        print("\t\t    ", self.__root.right.center.left.data, end = "")
        print("\t", self.__root.right.center.center.data)
        print("\t\t\t\t\t\t\t\t|")
        print("\t\t\t\t\t\t\t  -----------------")
        print("\t\t\t\t\t\t\t  |\t  |\t  |")
        print("\t\t\t\t\t\t\t", self.__root.right.center.left.left.data, end = "")
        print("\t", self.__root.right.center.left.center.data, end = "")
        print("\t", self.__root.right.center.left.right.data)
        print("\t\t\t\t\t\t\t\t\t  |")
        print("\t\t\t\t\t\t\t\t", self.__root.right.center.left.right.left.data, end = "")
        print("\t", self.__root.right.center.left.right.center.data, end = "")
        print("\t", self.__root.right.center.left.right.right.data, end = "")

    def imprime( self, nodo ):
        if nodo.data == "No" or nodo.data == "Si":
            print(f"Otorgar crédito: {nodo.data}")
            return 0
        elif nodo.data == "Rango Sueldo":
            print("¿Cuál es el rango de sueldo?")
            print("1. Menor a 8")
            print("2. Entre 8 y 28")
            print("3. Mayor a 28")
            num = input("Respuesta: ")
            return num
        elif nodo.data == "Edad":
            print("¿Cuál es la edad?")
            print("1. Entre 45 y 64 años")
            print("2. Menor a 24 o mayor a 64 años")
            print("3. Entre 24 y 44 años")
            num = input("Respuesta: ")
            return num
        elif nodo.data == "Buró de Crédito":
            print("¿Cuál es el estado de buró de crédito?")
            print("1. Rojo")
            print("2. Verde")
            num = input("Respuesta: ")
            return num
        elif nodo.data == "Ahorros":
            print("¿Cuál es la cantidad de ahorros?")
            print("1. Entre 51 y 150")
            print("2. Menor a 50")
            print("3. Mayor a 150")
            num = input("Respuesta: ")
            return num
        elif nodo.data == "INFONAVIT":
            print("¿Cuenta con INFONAVIT?")
            print("1. No")
            print("2. Si")
            num = input("Respuesta: ")
            return num
        
    def preguntas( self, nodo = None ):
        if nodo == None:
            nodo = self.__root
        respuesta = int(self.imprime(nodo))
        if respuesta == 0:
            exit
        if respuesta == 1:
            self.preguntas(nodo.left)
        if respuesta == 2:
            self.preguntas(nodo.center)
        if respuesta == 3:
            self.preguntas(nodo.right)
        
            
