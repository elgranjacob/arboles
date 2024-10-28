class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __del__(self):
        print(f"Podando el nodo con valor: {self.data}")

class Tree:
    def __init__(self):
        self.root = None

    def esVacio(self):
        return self.root is None

    def insertar(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.inserccion_recursiva(self.root, data)

    def inserccion_recursiva(self, nodo, data):
        if data < nodo.data:
            if nodo.left is None:
                nodo.left = Node(data)
            else:
                self.inserccion_recursiva(nodo.left, data)
        else:
            if nodo.right is None:
                nodo.right = Node(data)
            else:
                self.inserccion_recursiva(nodo.right, data)

    def buscar(self, data):
        return self.busqueda_recursiva(self.root, data)

    def busqueda_recursiva(self, nodo, data):
        if nodo is None or nodo.data == data:
            return nodo
        if data < nodo.data:
            return self.busqueda_recursiva(nodo.left, data)
        return self.busqueda_recursiva(nodo.right, data)

    def impresion(self):
        self.impresion_recursiva(self.root)
        print("") 


    def impresion_recursiva(self, nodo):
        if nodo is not None:
            self.impresion_recursiva(nodo.left)
            print(nodo.data, end=" ")
            self.impresion_recursiva(nodo.right)

    def __del__(self):
        self.destruccion_recursiva(self.root)

    def destruccion_recursiva(self, nodo):
        if nodo:
            self.destruccion_recursiva(nodo.left)
            self.destruccion_recursiva(nodo.right)

    def mostrar_acostado(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.root
        if nodo.right is not None:
            self.mostrar_acostado(nodo.right, nivel + 1)
        print(' ' * 4 * nivel + '->', nodo.data)
        if nodo.left is not None:
            self.mostrar_acostado(nodo.left, nivel + 1)

    def preorden(self):
        self.recorrido_preorden(self.root)
        print("") 


    def recorrido_preorden(self, nodo):
        if nodo:
            print(nodo.data, end=" ")
            self.recorrido_preorden(nodo.left)
            self.recorrido_preorden(nodo.right)

    def inorden(self):
        self.recorrido_inorden(self.root)
        print("") 


    def recorrido_inorden(self, nodo):
        if nodo:
            self.recorrido_inorden(nodo.left)
            print(nodo.data, end=" ")
            self.recorrido_inorden(nodo.right)

    def postorden(self):
        self.recorrido_postorden(self.root)
        print("") 

    def recorrido_postorden(self, nodo):
        if nodo:
            self.recorrido_postorden(nodo.left)
            self.recorrido_postorden(nodo.right)
            print(nodo.data, end=" ")

    def eliminar(self, data, usar_predecesor=True):
        self.root = self._eliminar_recursivo(self.root, data, usar_predecesor)

    def _eliminar_recursivo(self, nodo, data, usar_predecesor):
        if nodo is None:
            return nodo

        if data < nodo.data:
            nodo.left = self._eliminar_recursivo(nodo.left, data, usar_predecesor)
        elif data > nodo.data:
            nodo.right = self._eliminar_recursivo(nodo.right, data, usar_predecesor)
        else:
            if nodo.left is None:
                return nodo.right
            elif nodo.right is None:
                return nodo.left
            if usar_predecesor:
                temp = self._encontrar_maximo(nodo.left)
                nodo.data = temp.data
                nodo.left = self._eliminar_recursivo(nodo.left, temp.data, usar_predecesor)
            else:
                temp = self._encontrar_minimo(nodo.right)
                nodo.data = temp.data
                nodo.right = self._eliminar_recursivo(nodo.right, temp.data, usar_predecesor)
        return nodo

    def _encontrar_maximo(self, nodo):
        while nodo.right is not None:
            nodo = nodo.right
        return nodo

    def _encontrar_minimo(self, nodo):
        while nodo.left is not None:
            nodo = nodo.left
        return nodo
    
    def recorrido_por_niveles(self):
        if not self.root:
            return
        
        queue = [self.root]  
        while queue:
            nodo = queue.pop(0)  
            print(nodo.data, end=" ")

            if nodo.left:
                queue.append(nodo.left)
            if nodo.right:
                queue.append(nodo.right)
        
        print("")

    def altura(self):
        return self.altura_recursiva(self.root)

    def altura_recursiva(self, nodo):
        if nodo is None:
            return 0
        altura_izquierda = self.altura_recursiva(nodo.left)
        altura_derecha = self.altura_recursiva(nodo.right)
        return max(altura_izquierda, altura_derecha) + 1
    
    def contar_hojas(self):
        return self.contar_hojas_recursivo(self.root)

    def contar_hojas_recursivo(self, nodo):
        if nodo is None:
            return 0
        if nodo.left is None and nodo.right is None:
            return 1
        return self.contar_hojas_recursivo(nodo.left) + self.contar_hojas_recursivo(nodo.right)

    def contar_nodos(self):
        return self.contar_nodos_recursivo(self.root)

    def contar_nodos_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contar_nodos_recursivo(nodo.left) + self.contar_nodos_recursivo(nodo.right)
    
    def es_completo(self):
        if not self.root:
            return True
        
        queue = [self.root]
        debe_ser_completo = False

        while queue:
            nodo = queue.pop(0)
            
            if nodo.left:
                if debe_ser_completo:
                    return False
                queue.append(nodo.left)
            else:
                debe_ser_completo = True

            if nodo.right:
                if debe_ser_completo:
                    return False
                queue.append(nodo.right)
            else:
                debe_ser_completo = True

        return True
    
    def es_lleno(self):
        return self.es_lleno_recursivo(self.root)

    def es_lleno_recursivo(self, nodo):
        if nodo is None:
            return True
        if (nodo.left is None and nodo.right is not None) or (nodo.left is not None and nodo.right is None):
            return False
        return self.es_lleno_recursivo(nodo.left) and self.es_lleno_recursivo(nodo.right)
    
    def eliminar_arbol(self):
        self.eliminar_arbol_recursivo(self.root)
        self.root = None
        print("El árbol ha sido eliminado.")

    def eliminar_arbol_recursivo(self, nodo):
        if nodo is not None:
            self.eliminar_arbol_recursivo(nodo.left)
            self.eliminar_arbol_recursivo(nodo.right)
            print(f"Destruyendo nodo con valor: {nodo.data}")
            del nodo

def main():
    arbol = Tree()
    while True:
        print("\nMenú:")
        print("[1] Insertar elemento")
        print("[2] Mostrar árbol completo acostado con la raíz a la izquierda")
        print("[3] Recorrido por niveles (Amplitud)")
        print("[4] Buscar un elemento en el árbol")
        print("[5] Recorrer el árbol en PreOrden")
        print("[6] Recorrer el árbol en InOrden")
        print("[7] Recorrer el árbol en PostOrden")
        print("[8] Eliminar un nodo del árbol usando Predecesor")
        print("[9] Eliminar un nodo del árbol usando Sucesor")
        print("[10] Altura del árbol")
        print("[11] Cantidad de hojas del árbol")
        print("[12] Cantidad de nodos del árbol")
        print("[13] Verificar si es un árbol binario completo")
        print("[14] Verificar si es un árbol binario lleno")
        print("[15] Eliminar el árbol")
        print("[16] Imprimir árbol")
        print("[17] Salir")

        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            data = int(input("Ingrese el valor a insertar: ").strip())
            arbol.insertar(data)
        elif opcion == '2':
            print("Árbol acostado:")
            arbol.mostrar_acostado()
        elif opcion == '3':
            print("Recorrido por niveles:")
            arbol.recorrido_por_niveles()
        elif opcion == '4':
            data = int(input("Ingrese el valor a buscar: ").strip())
            encontrado = arbol.buscar(data)
            if encontrado:
                print(f"Valor {data} encontrado en el árbol.")
            else:
                print(f"Valor {data} no encontrado en el árbol.")
        elif opcion == '5':
            print("Recorrido PreOrden:")
            arbol.preorden()
        elif opcion == '6':
            print("Recorrido InOrden:")
            arbol.inorden()
        elif opcion == '7':
            print("Recorrido PostOrden:")
            arbol.postorden()
        elif opcion == '8':
            data = int(input("Ingrese el valor a eliminar usando Predecesor: ").strip())
            arbol.eliminar(data, usar_predecesor=True)
        elif opcion == '9':
            data = int(input("Ingrese el valor a eliminar usando Sucesor: ").strip())
            arbol.eliminar(data, usar_predecesor=False)
        elif opcion == '10':
            print("Altura del árbol:", arbol.altura())
        elif opcion == '11':
            print("Número de hojas:", arbol.contar_hojas())
        elif opcion == '12':
            print("Número de nodos:", arbol.contar_nodos())
        elif opcion == '13':
            print("¿El árbol es completo?", arbol.es_completo())
        elif opcion == '14':
            print("¿El árbol es lleno?", arbol.es_lleno())
        elif opcion == '15':
            arbol.eliminar_arbol()
            print("¡Completo!")
        elif opcion == "16":
            print("Árbol: ")
            arbol.impresion()
        elif opcion == '17':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()
