class Persona:
    def __init__(self, nombre, apellido, rut):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("RUT:", self.rut)
        
class Alumno(Persona):
    def __init__(self, nombre, apellido, rut, matricula, carrera):
        super().__init__(nombre, apellido, rut)
        self.matricula = matricula
        self.carrera = carrera

    def inscribirse_curso(self):
        print(self.nombre, "se ha inscrito en un curso.")

    def ver_horario(self):
        print("Mostrando horario del alumno", self.nombre)

class Profesor(Persona):
    def __init__(self, nombre, apellido, rut, id_profesor, especialidad):
        super().__init__(nombre, apellido, rut)
        self.id_profesor = id_profesor
        self.especialidad = especialidad

    def asignar_nota(self):
        print("El profesor", self.nombre, "ha asignado una nota.")

    def impartir_clase(self):
        print("El profesor", self.nombre, "está impartiendo clase.")
