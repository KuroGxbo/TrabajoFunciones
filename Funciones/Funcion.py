"""Función que pregunta por el nombre y la edad, utiliza input y las almacena en las variables, en combinación con return (para devolver datos)
permite que se retornen los valores introducidos por el usuario para su posterior procesamiento"""
def obtener_datos():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    return nombre, edad

"""
Función que retorna una condición como valor de retorno
"""
def validar_edad(edad):
    return edad >= 0 and edad <= 120

""" Función que utiliza condicionales para retornar un valor específico, si alguna se cumple se ignoran las otras """
def clasificar(edad):
    if edad < 18:
        return "Menor de edad"
    elif edad < 65:
        return "Adulto"
    else:
        return "Adulto mayor"
 
