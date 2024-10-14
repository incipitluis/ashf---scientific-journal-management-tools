import requests
from bs4 import BeautifulSoup
import time

# Función para obtener artículos de una URL
def obtener_articulos(url):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                break
        except requests.exceptions.SSLError as e:
            print(f"Intento {attempt + 1}: Error SSL al acceder a {url}. Reintentando en 5 segundos...")
            time.sleep(5)
    else:
        print(f"No se pudo acceder a {url} después de {max_retries} intentos.")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    articulos = []
    sections = soup.find_all('div', class_='section')

    for section in sections:
        # Obtener el título de la sección
        section_title = section.find('h2')
        if section_title:
            section_title_text = section_title.text.strip()
        else:
            section_title_text = ''

        # Omitir la sección "Reseñas"
        if section_title_text == 'Reseñas':
            continue  # Saltar esta sección

        ul_articles = section.find('ul', class_='cmp_article_list articles')
        if ul_articles:
            for li in ul_articles.find_all('li'):
                summary_div = li.find('div', class_='obj_article_summary')

                if summary_div:
                    titulo_div = summary_div.find('div', class_='title')
                    if titulo_div:
                        titulo = titulo_div.text.strip()
                    else:
                        titulo = "Título no disponible"

                    meta_div = summary_div.find('div', class_='meta')
                    if meta_div:
                        autores_div = meta_div.find('div', class_='authors')
                        if autores_div:
                            autores_texto = autores_div.text.strip()
                        else:
                            autores_texto = "Autores no disponibles"
                    else:
                        autores_texto = "Meta no disponible"

                    articulos.append({
                        'titulo': titulo,
                        'autores': autores_texto,
                    })

    return articulos

# Función para obtener URLs de los números de la revista
def obtener_urls_numeros(url_index):
    response = requests.get(url_index)
    if response.status_code != 200:
        print(f"Error al acceder a la URL: {url_index}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    urls_numeros = []

    
    ul_issues_archive = soup.find('ul', class_='issues_archive')
    if ul_issues_archive:
      
        for li in ul_issues_archive.find_all('li'):
         
            a_title = li.find('a', class_='title')
            if a_title and 'href' in a_title.attrs:
                href = a_title['href']
                if href.startswith('http'):
                    full_url = href
                else:
                    full_url = 'https://revistas.ucm.es' + href
                urls_numeros.append(full_url)

    return urls_numeros
