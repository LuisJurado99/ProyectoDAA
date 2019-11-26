from ArbolesBinarios import *

def main():
    arbol = ArbolBinarioBusqueda()
    arbol.insert(NodoArbol( "Rango Sueldo", NodoArbol( "No" ), NodoArbol( "Edad", NodoArbol("No"), NodoArbol("No"), NodoArbol("INFONAVIT", NodoArbol("No"), NodoArbol("Si"))), NodoArbol("Buró de Crédito", NodoArbol("No"), NodoArbol("INFONAVIT", NodoArbol("Ahorros", NodoArbol("Si"), NodoArbol("No"), NodoArbol("Edad", NodoArbol("No"), NodoArbol("No"), NodoArbol("Si"))), NodoArbol("Si")))))
    arbol.transversal()
    print("\n")
    arbol.preguntas()
    
main()
