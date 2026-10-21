# Importa tus módulos aquí
from data.biblioteca import libros, categorias
from utils.operaciones import (
    mostrar_disponibles,
    buscar_por_paginas,
    agregar_categoria,
    contar_libros,
    promedio_paginas,
)

continuar = "s"

while continuar == "s":
    print("\n=== BIBLIOTECA ===")
    print("1. Ver libros disponibles")
    print("2. Buscar libros cortos (menos de 400 páginas)")
    print("3. Ver estadísticas")
    print("4. Agregar categoría")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_disponibles(libros)
    elif opcion == "2":
        buscar_por_paginas(libros, 400)
    elif opcion == "3":
        print(contar_libros(libros))
        print(promedio_paginas(libros))
    elif opcion == "4":
        nueva = input("Nueva categoría: ")
        agregar_categoria(categorias, nueva)
        print(categorias)
    elif opcion == "5":
        continuar = "n"
    else:
        print("Opción no válida")