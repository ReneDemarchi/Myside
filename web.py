import time
from dados import adicionar_dados_brutos
from selenium import webdriver
from selenium.webdriver.common.by import By

def navegador():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(3)
    driver.maximize_window()
    return driver

def numero_anuncio(driver):
    numero = driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[2]/div/h1').text.split()[0].replace('.','')
    return int(numero)

def dados_tabela(driver):
    numero_de_anuncio_na_pagina = len(driver.find_elements(By.CSS_SELECTOR, 'li[data-cy="rp-property-cd"]'))
    for numero_do_anuncio in range(1,numero_de_anuncio_na_pagina+1,1):
        try:
            titulo = driver.find_element(By.XPATH,f'/html/body/section/div/div[3]/div[4]/div[1]/ul/li[{numero_do_anuncio}]/a/div/div[2]/div[1]/div/h2').text.split('\n')[-1]
            endereço = driver.find_element(By.XPATH,f'/html/body/section/div/div[3]/div[4]/div[1]/ul/li[{numero_do_anuncio}]/a/div/div[2]/div[1]/div/p').text
            metro = driver.find_element(By.XPATH,f'/html/body/section/div/div[3]/div[4]/div[1]/ul/li[{numero_do_anuncio}]/a/div/div[2]/div[2]/ul/li[1]/h3').text.split('\n')[-1]
            quarto = driver.find_element(By.XPATH,f'/html/body/section/div/div[3]/div[4]/div[1]/ul/li[{numero_do_anuncio}]/a/div/div[2]/div[2]/ul/li[2]/h3').text.split('\n')[-1]
            banheiro = driver.find_element(By.XPATH,f'/html/body/section/div/div[3]/div[4]/div[1]/ul/li[{numero_do_anuncio}]/a/div/div[2]/div[2]/ul/li[3]/h3').text.split('\n')[-1]
            try:
                garagem = driver.find_element(By.XPATH,f'/html/body/section/div/div[3]/div[4]/div[1]/ul/li[{numero_do_anuncio}]/a/div/div[2]/div[2]/ul/li[4]/h3').text.split('\n')[-1]
            except:
                garagem = 0
            preco = driver.find_element(By.XPATH,f'/html/body/section/div/div[3]/div[4]/div[1]/ul/li[{numero_do_anuncio}]/a/div/div[2]/div[3]/div[1]/p[1]').text.replace('A partir de ','')
            link = driver.find_element(By.XPATH,f'/html/body/section/div/div[3]/div[4]/div[1]/ul/li[{numero_do_anuncio}]/a').get_attribute("href")
        except:
            titulo = driver.find_element(By.XPATH,f'/html/body/section/div/div[3]/div[4]/div[1]/ul/li[{numero_do_anuncio}]/a/div[2]/div[2]/div[1]/div/h2').text.split('\n')[-1]
            endereço = driver.find_element(By.XPATH,f'/html/body/section/div/div[3]/div[4]/div[1]/ul/li[{numero_do_anuncio}]/a/div[2]/div[2]/div[1]/div/p').text
            metro = driver.find_element(By.XPATH,f'/html/body/section/div/div[3]/div[4]/div[1]/ul/li[{numero_do_anuncio}]/a/div[2]/div[2]/div[2]/div[1]/ul/li[1]/h3').text.split('\n')[-1]
            quarto = driver.find_element(By.XPATH,f'/html/body/section/div/div[3]/div[4]/div[1]/ul/li[{numero_do_anuncio}]/a/div[2]/div[2]/div[2]/div[1]/ul/li[2]/h3').text.split('\n')[-1]
            banheiro = driver.find_element(By.XPATH,f'/html/body/section/div/div[3]/div[4]/div[1]/ul/li[{numero_do_anuncio}]/a/div[2]/div[2]/div[2]/div[1]/ul/li[3]/h3').text.split('\n')[-1]
            try:
                garagem = driver.find_element(By.XPATH,f'/html/body/section/div/div[3]/div[4]/div[1]/ul/li[{numero_do_anuncio}]/a/div[2]/div[2]/div[2]/div[1]/ul/li[4]/h3').text.split('\n')[-1]
            except:
                garagem = 0
            preco = driver.find_element(By.XPATH,f'/html/body/section/div/div[3]/div[4]/div[1]/ul/li[{numero_do_anuncio}]/a/div[2]/div[2]/div[2]/div[2]/p').text.replace('A partir de ','')
            link = driver.find_element(By.XPATH,f'/html/body/section/div/div[3]/div[4]/div[1]/ul/li[{numero_do_anuncio}]/a').get_attribute("href")
        if link is None:
            # Fazer uma função para pegar os links das diferentes imobiliarias que estão anunciando esse imovel
            link = 'Tem mais de um anuncio nesse imovel'
        adicionar_dados_brutos(titulo,endereço,metro,quarto,banheiro,garagem,preco,link)
    print('Web scrping da pagina feito com susceso')
def aceitar_cooks():
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="adopt-accept-all-button"]').click()
def proxima_tabela(driver):
    driver.find_element(By.XPATH, '/html/body/section/div/div[3]/div[4]/div[1]/div/nav/button[2]').click()
    time.sleep(2)

def scrapy_zap():
    driver = navegador()
    driver.get('https://www.zapimoveis.com.br/venda/apartamentos/go+goiania++setor-marista/')
    n_anuncio = numero_anuncio(driver)
    paginas = int(n_anuncio / 30) + 1
    for pagina in range(paginas):
        dados_tabela(driver)
        proxima_tabela(driver)



