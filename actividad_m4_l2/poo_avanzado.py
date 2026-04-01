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
