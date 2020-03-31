import urllib3
import certifi
from bs4 import BeautifulSoup
#from openpyxl import Workbook
url = 'https://www.leroymerlin.com.br/'


#GET Pega o conteudo do site 

def acessar(site):
    http = urllib3.PoolManager() #Cria um objeto que gerencia a conexão
    resp = http.request('GET', url)
    if resp.status >= 200 or resp.status < 300:
        print("Requerimento Ok...")
        return resp.data.decode('utf-8')


#Head Verificar Site

def verificar(site):
    http = urllib3.PoolManager()
    resp = http.request('HEAD', url)
    print(resp.headers['Server'])
    print(resp.headers['Date'])
    print(resp.headers['Content-Type'])
    #print(resp.headers['Last-Modified'])


html_doc = acessar(url)
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
"""for link in soup.find_all('a'):
    print(link.get('href'))"""