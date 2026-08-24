# Node for the Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None   # enlace al hijo izquierdo
        self.right = None  # enlace al hijo derecho


# Binary Tree
class BinaryTree:
    def __init__(self):
        self.root = None  # raíz del árbol

    # Insertar nodo en el árbol (modo simple: tipo Binary Search Tree)
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:  # si está vacío
            self.root = new_node
            print(f"Inserted {data} as the ROOT node.")
        else:
            self._insert_recursive(self.root, new_node)

    # Método recursivo auxiliar
    def _insert_recursive(self, current, new_node):
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
                print(f"Inserted {new_node.data} to the LEFT of {current.data}.")
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
                print(f"Inserted {new_node.data} to the RIGHT of {current.data}.")
            else:
                self._insert_recursive(current.right, new_node)

    # Imprimir toda la estructura (In-Order Traversal)
    def print_tree(self):
        if self.root is None:
            print("Error: Cannot print, the Binary Tree is empty.")
        else:
            print("Binary Tree (In-Order Traversal):")
            self._print_inorder(self.root)
            print()  # salto de línea final

    # Recorrido In-Order (izquierda → raíz → derecha)
    def _print_inorder(self, node):
        if node is not None:
            self._print_inorder(node.left)
            print(node.data, end=" ")
            self._print_inorder(node.right)
