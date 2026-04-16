#Mapa mental para auxiliar na automação 
#Repita os passos manuais usando linhas de código 
#Entrar no site - https://devaprender-play.netlify.app/
#Anotar o nome do produto
#Anotar o preço do produto 
#Repetir para todos os produtos da página
#Guardar as informações em arquivo de texto (CSV)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #permite fazer o navegador “esperar” até que algo aconteça.
from selenium.webdriver.support import expected_conditions as EC #são condições prontas, tipo: “esperar até elemento aparecer”, “ficar clicável”, etc.


driver = webdriver.Chrome()
driver.get('https://devaprender-play.netlify.app/')

espera = WebDriverWait(driver, 5)#cria um objeto que vai esperar até 5 segundos #driver é o navegador aberto 

#Faz o Selenium esperar até que a condição dentro dele seja verdadeira.
produtos = espera.until(
    EC.presence_of_all_elements_located((By.XPATH, "//h3[@class='text-lg font-semibold text-gray-900 group-hover:text-indigo-600']"))
)#Espera até que todos os elementos que correspondem ao seletor existam na página.
#Importante: ele não garante que estão visíveis, só que estão no HTML.

#XPATH(identificador de elementos no site)
#//tag[@atributo='valor']
#Anotar os nomes dos produtos
#uso find_elements para encontrar vários elementos no site

produtos = driver.find_elements(By.XPATH, "//h3[@class='text-lg font-semibold text-gray-900 group-hover:text-indigo-600']")
#define como encontrar os elementos na página, neste caso usando todas as tags 'h3'

#Anotar os  preços dos produtos

precos = driver.find_elements(By.XPATH, "//p[@class='text-2xl font-bold text-indigo-600']")

#Guardar as informações em arquivo de texto (CSV)
#Uso o iterável for para percorrer todos os produtos e preços da página 
#Para depois transformá-los em arquivo de texto com o zip 

for produto, preco in zip(produtos, precos):
#produto e preço no singular para iterar cada um na lista de produtos e preços  
#with open para abrir e fechar o arquivo automaticamente
#enconding para trazer para o portugues e não quebrar com termos como "ç"  
    with open('preços.csv', 'w', encoding='utf-8') as arquivo:
        for produto, preco in zip(produtos, precos):
            arquivo.write(f'{produto.text}, {preco.text}\n')
#arquivo.write é utilizado para escrever as informações no arquivo csv
#\n para pular a linha para cada produto/preço
input('')










