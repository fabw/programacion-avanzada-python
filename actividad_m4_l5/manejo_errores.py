class EdadInvalidaError(Exception):
    pass


def dividir():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 / num2
    except ValueError:
        print("Error: debe ingresar solo números.")
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero.")
    else:
        print("El resultado es:", resultado)


def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser menor que 0.")
    print("Edad válida:", edad)


def simulacion_archivo():
    try:
        print("Abriendo archivo...")
        numero = int(input("Ingrese un número entero: "))
        print("Número ingresado:", numero)
    except ValueError:
        print("Error: debe ingresar un número entero.")
    finally:
        print("Cerrando archivo...")


if __name__ == "__main__":
    dividir()

    try:
        edad = int(input("Ingrese una edad: "))
        validar_edad(edad)
    except ValueError:
        print("Error: debe ingresar un número entero para la edad.")
    except EdadInvalidaError as e:
        print("Error:", e)

    simulacion_archivo()
