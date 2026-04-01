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

class Asignatura:
    def __init__(self, codigo, nombre, horas_semanales):
        self.codigo = codigo
        self.nombre = nombre
        self.horas_semanales = horas_semanales

    def mostrar_asignatura(self):
        print("Código:", self.codigo)
        print("Nombre:", self.nombre)
        print("Horas semanales:", self.horas_semanales)


class Curso:
    def __init__(self, codigo_curso, seccion, sala):
        self.codigo_curso = codigo_curso
        self.seccion = seccion
        self.sala = sala

    def mostrar_curso(self):
        print("Código del curso:", self.codigo_curso)
        print("Sección:", self.seccion)
        print("Sala:", self.sala)

class Matricula:
    def __init__(self, fecha, estado):
        self.fecha = fecha
        self.estado = estado

    def registrar_matricula(self):
        print("Matrícula registrada en fecha:", self.fecha)

    def cancelar_matricula(self):
        print("La matrícula ha sido cancelada.")





