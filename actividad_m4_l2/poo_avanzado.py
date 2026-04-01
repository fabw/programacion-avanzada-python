# Actividad 1: Definición de una clase con constructor
class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def mostrar_info(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Año de publicación:", self.anio_publicacion)


libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro1.mostrar_info()

# Actividad 2: Métodos accesadores y mutadores
class LibroEncapsulado:
    def __init__(self, titulo, autor, anio_publicacion):
        self._titulo = titulo
        self._autor = autor
        self._anio_publicacion = anio_publicacion

    def mostrar_info(self):
        print("Título:", self._titulo)
        print("Autor:", self._autor)
        print("Año de publicación:", self._anio_publicacion)

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    def get_anio_publicacion(self):
        return self._anio_publicacion

    def set_anio_publicacion(self, nuevo_anio):
        self._anio_publicacion = nuevo_anio


print("\nACTIVIDAD 2")
libro2 = LibroEncapsulado("El principito", "Antoine de Saint-Exupéry", 1943)
libro2.mostrar_info()

print("Título actual:", libro2.get_titulo())
libro2.set_titulo("El principito - Edición especial")
print("Título modificado:", libro2.get_titulo())

print("Año actual:", libro2.get_anio_publicacion())
libro2.set_anio_publicacion(1944)
print("Año modificado:", libro2.get_anio_publicacion())
