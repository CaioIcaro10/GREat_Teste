from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class teste():
    servico = Service(GeckoDriverManager().install())

    navegador = webdriver.Firefox(service=servico)

    navegador.get("https://testlink.org/")

    ase_1 = navegador.find_element(By.XPATH, '/html/body/div/div[1]/h3').text
    ase_2 = navegador.find_element(By.XPATH, '/html/body/div/div[4]/p').text

    assert ase_1 == "TestLink"
    assert ase_2 == "© TestLink Development Team 2013/2018"

    navegador.find_element(By.XPATH,'/html/body/div/div[3]/div/a[3]').click()
    navegador.implicitly_wait(5)

    ase_3 = navegador.find_element(By.XPATH, '/html/body/div[4]/div/main/turbo-frame/div/div/div/div[3]/div[1]/readme-toc/div/div[2]/article/ol[1]/li[6]/a').text

    assert ase_3 == "TestLink Team"

    navegador.implicitly_wait(10)



servico = Service(GeckoDriverManager().install())

navegador = webdriver.Firefox(service=servico)
navegador.get('https://github.com/TestLinkOpenSourceTRMS/testlink-code/tree/testlink_1_9_20_fixed/')
navegador.find_element(By.CLASS_NAME, value='form-control js-site-search-focus header-search-input jump-to-field js-jump-to-field js-site-search-field is-clearable').send_keys('tesklink')