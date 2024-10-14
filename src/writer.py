import csv

def guardar_en_csv(conteo_autores, nombre_archivo):
    lista_conteo_autores = [{'autor': autor, 'numero': conteo} for autor, conteo in conteo_autores.items()]
    lista_conteo_autores.sort(key=lambda x: x['numero'], reverse=True)

    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=['autor', 'numero'])
        writer.writeheader()
        writer.writerows(lista_conteo_autores)
    
    print(f"Conteo de autores guardado en {nombre_archivo}")
