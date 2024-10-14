# Web Scraping para Anales del Seminario de Historia de la Filosofía

Este proyecto surge como parte de mi colaboración con la revista científica **Anales del Seminario de Historia de la Filosofía**, de **Ediciones Complutense**. El objetivo inicial de este repositorio es desarrollar un scraper mínimo en Python básico que permita la recopilación de datos de los artículos publicados en la revista, enfocándose en los autores y su frecuencia de publicación.

Este proyecto es una herramienta en marcha que comienza con este scraper simple, pero con la intención de expandirlo en el futuro. El plan es desarrollar una batería de herramientas que permitan la gestión y recopilación de datos para revistas científicas, avanzando hacia un diseño más escalable y ajustable.

## Características del Proyecto

El scraper actual se enfoca en:
- Recuperar el título y autores de los artículos publicados en la revista.
- Contar la cantidad de veces que un autor ha publicado más de una vez en los últimos números.
- Guardar los resultados en un archivo CSV para un análisis posterior.

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tuusuario/nombre-repo.git
    cd ashf
    ```

2. Instala las dependencias necesarias usando el archivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para ejecutar el scraper en su estado actual:

```bash
python src/main.py
```

Este comando ejecutará el scraper sobre las últimas ediciones de la revista Anales del Seminario de Historia de la Filosofía y generará un archivo nuevo_conteo.csv con los autores y la cantidad de veces que han publicado.

## Cambiar la revista a analizar

Si deseas modificar el código para analizar otra revista, puedes hacerlo cambiando las URLs en la sección de "páginas de archivo" dentro de main.py. Por ejemplo, si quisieras cambiar a otra revista de Ediciones Complutense:

paginas_archivo = [
    'https://revistas.ucm.es/index.php/OTRA_REVISTA/issue/archive',
    'https://revistas.ucm.es/index.php/OTRA_REVISTA/issue/archive/2'
]

## Contribuciones

Este proyecto está en una fase inicial, pero si deseas colaborar con ideas o mejoras, las contribuciones son bienvenidas. Puedes hacer un fork de este repositorio, implementar cambios y luego hacer un pull request.

## Licencia

Este proyecto está bajo la licencia MIT - consulta el archivo LICENSE para más detalles.
