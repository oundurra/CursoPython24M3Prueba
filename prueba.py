import requests # esta libreria me sirve para hacer el llamado a la api
import json # esta libreria me sirve para convertir el archivo json que me entrega la ap
from string import Template # esta libreria me sirve para usar el Template

def request_get(url): # defino el método que invoca la API
    return json.loads(requests.get(url).text) # invoco la API y convierto la salida en lista

def get_page_html():
    html = '''<!DOCTYPE html>
            <html>
            <head>
                <title>Título de la Página</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">            </head>
            <body>
                <nav class="navbar bg-body-tertiary">
                    <div class="container-fluid">
                        <span class="navbar-brand mb-0 h1">Aves de Chile</span>
                    </div>
                </nav>
                <div class="row row-cols-1 row-cols-md-5 g-4">
                $body
                </div>                    
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
            </body>
            </html>
            '''
    return html

def get_card_html():
    html = '''<div class="col">
                    <div class="card">
                    <img src="$url" class="card-img-top">
                    <div class="card-body">
                        <h5 class="card-title">$nombre_espanol</h5>
                        <h5 class="card-title">$nombre_ingles</h5>
                    </div>
                    </div>
                </div>'''
    return html

url = "https://aves.ninjas.cl/api/birds" # este es el endpoint (url) donde esta la api
results = request_get(url)[0:20] # llamo la api con el metodo request y guardo el resultado en response

data = [[i['name']['spanish'],i['name']['english'],i['images']['main']] for i in results] # recorro el resultado de la API para extraer la data

card_template = Template(get_card_html()) # defino el template del código HTML de las tarjetas
html_template = Template(get_page_html()) # defino el template de la pagina HTML

cards = ''
for i in data: # genero el HTML de las imágenes recorriendo la lista urls y usando el template card_template
    cards += card_template.substitute(nombre_espanol = i[0], nombre_ingles = i[1], url = i[2])+'\n'

html_template = html_template.substitute(body = cards) # genero el HTML de la página web
html_file = open("index.html","w") # abro el archivo index.html en modo escritura
html_file.write(html_template) # escribo el código HTML en el archivo index.html
html_file.close() # cierro el archivo index.html