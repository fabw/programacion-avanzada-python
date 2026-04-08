archivo = open("datos.txt", "w", encoding="utf-8")
archivo.write("Primera línea de texto.\n")
archivo.write("Segunda línea de texto.\n")
archivo.write("Tercera línea de texto.\n")
archivo.close()

archivo = open("datos.txt", "r", encoding="utf-8")
contenido = archivo.read()
print("Contenido completo del archivo:")
print(contenido)
archivo.close()

archivo = open("datos.txt", "r", encoding="utf-8")
print("Primera línea:")
print(archivo.readline(), end="")

print("\nResto del archivo:")
for linea in archivo:
    print(linea, end="")
archivo.close()

archivo = open("datos.txt", "a", encoding="utf-8")
archivo.write("Cuarta línea agregada en modo append.\n")
archivo.close()

archivo = open("datos.txt", "r", encoding="utf-8")
print("\n\nContenido actualizado del archivo:")
print(archivo.read())
archivo.close()

archivo = open("datos.txt", "r", encoding="utf-8")
print("Nombre del archivo:", archivo.name)
print("¿Está cerrado?:", archivo.closed)
print("Modo de apertura:", archivo.mode)
archivo.close()
print("¿Está cerrado después de close()?:", archivo.closed)
