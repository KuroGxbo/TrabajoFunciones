#Importación de nuevo módulo con el as lo llamamos con un mombre corto
import Funciones.Funcion as Fun
import Funciones.DatosPersonales as DatosPer
"""Recordar Siempre llamar al módulo con el nombre y un punto, así aparecerá disponible en el archivo Main,
nombre y edad utilizan Asignación Múltiple"""
nombre, edad = Fun.obtener_datos()
if Fun.validar_edad(edad):
    print(f"{nombre}: {Fun.clasificar(edad)}")
else:
    print("Edad no válida")

#Utilización de Otro Módulo, en este caso uno que refiere a datos personales

DatosPer.DatosPersonales(nombre="Pepe Prez",nota=25,aprobado=True)

DatosPer.NotasPersonales(10,10,8,4,7,10,9,8,10,6)

DatosPersonales=dict(nombre="Pepe Prez",notas=False,aprobado=True,carrera="Negocios Digitales",semestre="Cuarto")
NotasAsociadas=tuple([10,10,10,7,8,9])

DatosPer.ImprimirInformacionPersonal(*NotasAsociadas,**DatosPersonales)

print(f"Promedio usando Keywords={DatosPer.PromedioConKeyword(nota3=10,nota1=9,nota2=8)}")