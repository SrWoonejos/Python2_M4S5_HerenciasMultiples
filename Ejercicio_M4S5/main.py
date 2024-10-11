#ejercicio herencias multiples a,b,c

# Definición de las clases A y B
class A:
    def __init__(self):
        print("Pertenezco a la clase A")

    def metodo_a(self):
        print("Método heredado de A")

class B:
    def __init__(self):
        print("Clase B")

    def metodo_b(self):
        print("Método heredado de B")

# Nueva clase C con herencia múltiple de B y A
class C(B, A):  # Hereda de B y A
    def __init__(self):
        # Llamada al constructor de B (el primero en la herencia múltiple)
        super().__init__()
    
    def metodo_c(self):
        print("Método de clase C")

# Crear un objeto de la clase C
objeto_c = C()

# Acceder a los métodos de la clase A, B y C
objeto_c.metodo_a()  # Heredado de la clase A
objeto_c.metodo_b()  # Heredado de la clase B
objeto_c.metodo_c()  # Propio de la clase C
