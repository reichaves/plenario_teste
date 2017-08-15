from bs4 import BeautifulSoup
import requests

page = requests.get("http://www25.senado.leg.br/web/atividade/materias/-/materia/votacao/2363507")

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
