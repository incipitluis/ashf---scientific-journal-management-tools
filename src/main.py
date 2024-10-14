from scraper import obtener_articulos, obtener_urls_numeros
from writer import guardar_en_csv
from utils import contar_autores, calcular_porcentajes

# URLs de las páginas de archivo
paginas_archivo = [
    'https://revistas.ucm.es/index.php/ASHF/issue/archive',
    'https://revistas.ucm.es/index.php/ASHF/issue/archive/2'
]

# Obtener URLs de todos los números
urls_todos_numeros = []
for pagina in paginas_archivo:
    urls_numeros = obtener_urls_numeros(pagina)
    urls_todos_numeros.extend(urls_numeros)

# Eliminar duplicados manteniendo el orden
urls_todos_numeros = list(dict.fromkeys(urls_todos_numeros))

# Limitar a los últimos 9 números
urls_todos_numeros = urls_todos_numeros[:9]

# Procesar artículos
todos_los_articulos = []
for url_numero in urls_todos_numeros:
    print(f"Procesando número: {url_numero}")
    articulos = obtener_articulos(url_numero)
    todos_los_articulos.extend(articulos)

# Contar autores y calcular estadísticas
conteo_autores = contar_autores(todos_los_articulos)
total_articulos, articulos_autores_recurrentes, porcentaje_recurrentes = calcular_porcentajes(conteo_autores, todos_los_articulos)

# Imprimir resultados
print(f"\nTotal de artículos: {total_articulos}")
print(f"Artículos publicados por autores con más de un artículo: {articulos_autores_recurrentes}")
print(f"Porcentaje de artículos publicados por autores recurrentes: {porcentaje_recurrentes:.2f}%")

# Guardar resultados en CSV
guardar_en_csv(conteo_autores, 'nuevo_conteo.csv')
