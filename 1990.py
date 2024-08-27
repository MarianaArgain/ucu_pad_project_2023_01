# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:25:34 2024

@author: Usuario
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:22:29 2024

@author: Usuario
"""

import re

file=open('C:\\Users\\Usuario\\OneDrive\\Documentos\\data\\baby1994.html')

# Patrones para buscar en el archivo
pattern = 'year'
pattern1 = r'\d{4,}'  # Busca cuatro o más dígitos consecutivos (posibles años)
pattern2 = r'<tr align="right"><td>'  # Busca la cadena exacta en el HTML
pattern3 = r'\d+'  # Busca uno o más dígitos consecutivos
pattern4 = r'[A-Z][a-z]*'  # Busca palabras que comienzan con una mayúscula seguida de minúsculas
pattern5 = r'</td><td>'  # Busca la cadena exacta en el HTML

# Inicializar listas
mi_lista = []
mi_lista2 = []

# Leer el archivo y procesar la información para mi_lista
with open('C:\\Users\\Usuario\\OneDrive\\Documentos\\data\\baby1994.html') as file:
    for line in file:
        # Buscar el patrón </td><td> y agregar palabras a mi_lista
        if re.findall(pattern5, line):
            match = re.search(pattern4, line)
            if match:
                mi_lista.append(match.group(0))

# Ordenar mi_lista alfabéticamente
mi_lista.sort()

# Leer el archivo nuevamente para procesar la información para mi_lista2
with open('C:\\Users\\Usuario\\OneDrive\\Documentos\\data\\baby1994.html') as file:
    for line in file:
        # Buscar el patrón 'year'
        year_result = re.findall(pattern, line)
        if year_result:
            print(year_result)
            year_match = re.search(pattern1, line)
            if year_match:
                print(year_match.group(0))
                anio = year_match.group(0)  # Guardar el año encontrado
        
        # Buscar la estructura HTML y extraer información
        html_match = re.search(pattern2, line)
        if html_match:
            rank_match = re.search(pattern3, line)
            name_match = re.search(pattern4, line)
            if rank_match and name_match:
                # Agregar los datos a mi_lista2
                mi_lista2.append((anio, rank_match.group(0), name_match.group(0)))

# Ordenar mi_lista2 por el tercer elemento de la tupla (en orden ascendente)
mi_lista2.sort(key=lambda x: x[2])

# Imprimir las listas
print("Lista de palabras ordenadas alfabéticamente:")
print(mi_lista)

print("Lista de datos ordenada por el tercer elemento:")
print(mi_lista2)