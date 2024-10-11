#Desafio Polimorfismo multiple python m4s5

#clase persona
class Persona:
    def __init__(self, nombre, apellido, anno):
        self.nombre = nombre
        self.apellido = apellido
        self.anno = anno

# clase depto
class Departamento:
    def __init__(self, nombre_depto, nombre_corto_depto):
        self.nombre_depto = nombre_depto
        self.nombre_corto_depto = nombre_corto_depto

#clase trabajador
class Trabajador(Persona, Departamento):
    def __init__(self, nombre, apellido, anno, nombre_dpto, nombre_corto_dpto, salario):
        # Inicializamos los atributos de Persona y Departamento
        Persona.__init__(self, nombre, apellido, anno)
        Departamento.__init__(self, nombre_dpto, nombre_corto_dpto)
        # Atributo exclusivo de Trabajador
        self.salario = salario

# objeto trabajador
trabajador = Trabajador("Juan", "Pérez", 2005, "Ingeniería de Software", "IS", 20000)

#instancias de persona, depto, trabajador
print(f"Es trabajador instancia de Persona: {isinstance(trabajador, Persona)}")
print(f"Es trabajador instancia de Departamento: {isinstance(trabajador, Departamento)}")
print(f"Es trabajador instancia de Trabajador: {isinstance(trabajador, Trabajador)}")
