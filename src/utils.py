def contar_autores(todos_los_articulos):
    conteo_autores = {}
    for articulo in todos_los_articulos:
        autores_texto = articulo['autores']
        if autores_texto not in ["Autores no disponibles", "Meta no disponible"]:
            lista_autores = [autor.strip() for autor in autores_texto.split(',')]
            for autor in lista_autores:
                if autor:
                    if autor in conteo_autores:
                        conteo_autores[autor] += 1
                    else:
                        conteo_autores[autor] = 1
    return conteo_autores

def calcular_porcentajes(conteo_autores, todos_los_articulos):
    total_articulos = len(todos_los_articulos)
    articulos_autores_recurrentes = sum(conteo for conteo in conteo_autores.values() if conteo > 1)
    porcentaje_recurrentes = (articulos_autores_recurrentes / total_articulos) * 100 if total_articulos > 0 else 0
    return total_articulos, articulos_autores_recurrentes, porcentaje_recurrentes
