# WEB SCRAPING CON BEAUTIFULSOUP Y REQUESTS

from bs4 import BeautifulSoup
import requests

# Obtener información de una página web
resultado = requests.get('https://fede-garay.vercel.app/')
sopa = BeautifulSoup(resultado.text, 'lxml')

# Cantidad de etiquetas h2
print(len(sopa.select('h2')))

# Texto de la primera etiqueta h2
print(sopa.select('h2')[0].get_text())

# Recorrer títulos dentro del id "videos"
for titulo in sopa.select('#videos h3'):
    print(titulo.get_text())

# Recorrer enlaces dentro del id "videos"
for etiqueta in sopa.select('#videos a'):
    print(etiqueta['href'])

# Obtener la primera imagen y su URL completa
imagen = sopa.select('img')[0]
url_imagen = "https://fede-garay.vercel.app/" + imagen['src']
print(url_imagen)

# Descargar imagen y guardarla en archivo
request_imagen = requests.get(url_imagen).content
foto = open('mi_foto.png', 'wb')
foto.write(request_imagen)
foto.close()


















