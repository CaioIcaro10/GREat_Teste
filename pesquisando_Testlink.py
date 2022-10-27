from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


servico = Service(GeckoDriverManager().install())

navegador = webdriver.Firefox(service=servico)
#Clicando na barra de busca
navegador.get('https://github.com/TestLinkOpenSourceTRMS/testlink-code/tree/testlink_1_9_20_fixed/')
navegador.find_element(By.XPATH, value='/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label').click()

#Adicionando o que o usuário deseja
navegador.find_element(By.XPATH, value='/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]').send_keys('TestLink')

#Pressionando ENTER
navegador.find_element(By.XPATH, value='/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]').send_keys(Keys.ENTER)
navegador.implicitly_wait(3)

#Clicando para aparecer novos resultados
navegador.find_element(By.XPATH, value='/html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div/div[3]/div/div[1]/h3/small/a').click()
navegador.implicitly_wait(3)

#Indo para a página 2
navegador.find_element(By.XPATH, value='/html/body/div[1]/div[4]/main/div/div[3]/div/div[2]/div/a[1]').click()