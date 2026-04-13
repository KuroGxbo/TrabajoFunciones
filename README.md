# 📦 Trabajo: Funciones y Módulos en Python

> **Repositorio:** [KuroGxbo/TrabajoFunciones](https://github.com/KuroGxbo/TrabajoFunciones)

---

## 📋 Descripción

Este proyecto es un ejercicio práctico sobre el uso de **funciones** y **módulos** en Python. Se organiza el código en módulos reutilizables que demuestran conceptos clave como la importación con alias, la asignación múltiple, y el uso de argumentos posicionales y por keyword.

---

## 🗂️ Estructura del Proyecto

```
TrabajoFunciones/
│
├── main.py                    # Archivo principal — punto de entrada
│
└── Funciones/
    ├── Funcion.py             # Módulo con funciones de validación y clasificación
    └── DatosPersonales.py     # Módulo con funciones de manejo de datos personales
```

---

## 🧠 Conceptos Aplicados

| Concepto | Descripción |
|---|---|
| `import módulo as alias` | Importación de módulos con nombre corto para mejor legibilidad |
| **Asignación múltiple** | Retorno y desempaquetado de múltiples valores en una línea |
| `*args` | Argumentos posicionales de longitud variable |
| `**kwargs` | Argumentos por nombre (keyword) de longitud variable |
| **Módulos propios** | Organización del código en archivos `.py` separados y reutilizables |

---

## 📁 Módulos

### `Funciones/Funcion.py`

Contiene las funciones principales de lógica del programa:

- **`obtener_datos()`** — Solicita al usuario su nombre y edad (retorno múltiple)
- **`validar_edad(edad)`** — Verifica si la edad ingresada es válida
- **`clasificar(edad)`** — Clasifica al usuario según su edad

### `Funciones/DatosPersonales.py`

Contiene funciones para el manejo e impresión de información personal:

- **`DatosPersonales(nombre, nota, aprobado)`** — Muestra datos básicos de un estudiante
- **`NotasPersonales(*notas)`** — Recibe y procesa una cantidad variable de notas
- **`ImprimirInformacionPersonal(*args, **kwargs)`** — Imprime información completa usando `*args` y `**kwargs`
- **`PromedioConKeyword(**kwargs)`** — Calcula el promedio de notas usando argumentos por nombre

---

## ▶️ Ejecución

```bash
# Clonar el repositorio
git clone https://github.com/KuroGxbo/TrabajoFunciones.git

# Ingresar al directorio
cd TrabajoFunciones

# Ejecutar el programa
python main.py
```

---

## 💡 Ejemplo de Uso

```python
import Funciones.Funcion as Fun
import Funciones.DatosPersonales as DatosPer

# Asignación múltiple con retorno de función
nombre, edad = Fun.obtener_datos()

if Fun.validar_edad(edad):
    print(f"{nombre}: {Fun.clasificar(edad)}")

# Uso de *args y **kwargs
DatosPer.ImprimirInformacionPersonal(*NotasAsociadas, **DatosPersonales)

# Keyword arguments
print(f"Promedio = {DatosPer.PromedioConKeyword(nota1=9, nota2=8, nota3=10)}")
```

---

## 📚 Requisitos

- Python **3.x**
- No requiere librerías externas

---

## 👨‍🏫 Contexto Académico

Este trabajo fue desarrollado como parte de la materia de **Programación Orientada a Objetos**, con el objetivo de aplicar buenas prácticas en la organización modular del código y el manejo de funciones avanzadas en Python.

---

