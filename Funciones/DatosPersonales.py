"""
Función con ** kwargs, recordar que como es un diccionario se debe utilizar .items para acceder a sus elementos y el **
"""
def DatosPersonales(**kwargs):
     print(f"Se Imprime un Diccionario")
     for clave,valor in kwargs.items():
        print(f"Clave:{clave} tiene el valor de {valor}")

"""
Función con * args, recordar que como es una lista o tupla se debe utilizar un for para acceder a sus elementos y se define con *
"""
def NotasPersonales(*args):
     print(f"Se Imprime una Tupla")
     for valor in args:
        print(f"Notas: {valor}")

"""
Función con * args y **kwargs
"""
def ImprimirInformacionPersonal(*args,**kwargs):
    print(f"Se puede imprimir datos varios, no solo un tipo")
    datos=kwargs.items()
    for clave,valor in kwargs.items():
        print(f"Información {clave}:{valor}")
        if(clave=="notas" and valor==True):
            for notas in args:
                print(f"Nota:{notas}")
            print(f"Promedio Actual:{sum(args)/args.__len__()}")
        else:
            print("Sin acceso a las notas")
        
"""
Función con parámetros con nombre
"""
def PromedioConKeyword(nota1,nota2,nota3):
    return (nota1+nota2+nota3)/3