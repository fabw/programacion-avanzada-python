
# ----------------------------------------
# Actividad 1: Definición de una clase con constructor
# ----------------------------------------
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

# ----------------------------------------
# Actividad 2: Métodos accesadores y mutadores
# ----------------------------------------
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

libro2 = LibroEncapsulado("El principito", "Antoine de Saint-Exupéry", 1943)
libro2.mostrar_info()
print(libro2.get_titulo())
libro2.set_titulo("El principito - Edición especial")
print(libro2.get_titulo())
print(libro2.get_anio_publicacion())
libro2.set_anio_publicacion(1944)
print(libro2.get_anio_publicacion())

# ----------------------------------------
# Actividad 3: Sobrecarga de métodos
# ----------------------------------------
class LibroSobrecarga:
    def __init__(self, titulo, autor, anio_publicacion):
        self._titulo = titulo
        self._autor = autor
        self._anio_publicacion = anio_publicacion

    def resumen(self, texto=None):
        if texto is None:
            print("Libro sin resumen disponible")
        else:
            print(texto)

libro3 = LibroSobrecarga("1984", "George Orwell", 1949)
libro3.resumen()
libro3.resumen("Novela que muestra una sociedad controlada por un poder totalitario.")
# ----------------------------------------
# Actividad 4: Colaboración entre objetos
# ----------------------------------------
class Autor:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais


class LibroColaboracion:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def mostrar_info(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor.nombre)
        print("País del autor:", self.autor.pais)
        print("Año de publicación:", self.anio_publicacion)

autor1 = Autor("Gabriel García Márquez", "Colombia")
libro4 = LibroColaboracion("Cien años de soledad", autor1, 1967)
libro4.mostrar_info()

# ----------------------------------------
# Actividad 5: Composición
# ----------------------------------------
class Editorial:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad


class LibroComposicion:
    def __init__(self, titulo, autor, anio_publicacion, nombre_editorial, ciudad_editorial):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.editorial = Editorial(nombre_editorial, ciudad_editorial)

    def mostrar_info(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Año de publicación:", self.anio_publicacion)
        print("Editorial:", self.editorial.nombre)
        print("Ciudad de la editorial:", self.editorial.ciudad)


libro5 = LibroComposicion(
    "Don Quijote de la Mancha",
    "Miguel de Cervantes",
    1605,
    "Francisco de Robles",
    "Madrid"
)

libro5.mostrar_info()

