# minhas importacoes
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from faker import Faker
fake = Faker('pt_BR')


class Test_busca_rede():
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path =
        'C:\\Users\\Juliana.bueno\\Desktop\\ConsultasServicos\\drivers\\chromedriver.exe')

    def teardown_method(self):
        self.driver.quit()

    def test_config(self):
        self.driver.get("https://qa.clude.com.br/cluder/Login/Index2")
        self.driver.maximize_window()

        # Login
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("@uorak.com")
        self.driver.find_element(By.ID, "senha").click()
        self.driver.find_element(By.ID, "senha").send_keys("xxx")
        self.driver.find_element(By.XPATH, "//button[@class='btn-primary'][contains(.,'Entrar na conta')]").click()
        WebDriverWait(self.driver, 20)


        # iniciando
        self.driver.find_element(By.XPATH, "//span[contains(.,'Saúde')]")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Saúde')]").click()
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[2]/div[1]/a[1]/div[1]").click()


        # consulta
        self.driver.find_element(By.XPATH,"//div[@class='panel-body'][contains(.,'Consulta')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Buscar na rede credenciada')]").click()
        self.driver.find_element(By.ID, "especialidades").send_keys("pediatria")

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                         "//div[@tabindex='-1'][contains(.,'00010057 | Consulta em Pediatria - Especialidade Básica')]"))).click()

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                        "//td[@class='text-center']"))).click()
        # time.sleep(3)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[2]/button"))).click()
        element = self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']")
        actionchains = ActionChains(self.driver)
        actionchains.double_click(element).perform()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                        "//img[@src='/cluder/Imagens/icone_voltar.png']"))).click()

        print("Consulta verficada")

        # exames
        self.driver.find_element(By.XPATH, "//div[@class='panel-body'][contains(.,'Exames')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Prefiro fazer o orçamento sozinho')]").click()
        self.driver.find_element(By.ID, "especialidades").send_keys("mamografia")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'40808041 | RX_Mamografia digital bilateral')]"))).click()

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[2]"))).click()
        time.sleep(3)
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='button'][contains(.,'1')]"))).click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'1')]").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success'][contains(.,'Finalizar')]").click()

        element = self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']")
        actionchains = ActionChains(self.driver)
        actionchains.double_click(element).perform()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                    "//img[@src='/cluder/Imagens/icone_voltar.png']"))).click()
        print("Exame verficado")


        # vacinas
        self.driver.find_element(By.XPATH, "//div[@class='panel-body'][contains(.,'Vacinas')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Buscar na rede credenciada')]").click()
        self.driver.find_element(By.ID, "especialidades").send_keys("gripe")

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'90000024 | Gripe')]"))).click()

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                 "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]"))).click()
        element = self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']")
        actionchains = ActionChains(self.driver)
        actionchains.double_click(element).perform()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                "//img[@src='/cluder/Imagens/icone_voltar.png']"))).click()
        print("Vacina verficada")

        # Sessões e terapias
        self.driver.find_element(By.XPATH, "//div[@class='panel-body'][contains(.,'Sessões e terapias')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Buscar na rede credenciada')]").click()
        self.driver.find_element(By.ID, "especialidades").send_keys("psicologia")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'21190001 | Sessao de Psicologia')]"))).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                 "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]"))).click()
        element = self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']")
        actionchains = ActionChains(self.driver)
        actionchains.double_click(element).perform()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                            "//img[@src='/cluder/Imagens/icone_voltar.png']"))).click()
        print("Sessões e terapias verficadas")


        # Odontologia
        self.driver.find_element(By.XPATH, "//div[@class='panel-body'][contains(.,'Odontologia')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Buscar na rede credenciada')]").click()
        self.driver.find_element(By.ID, "especialidades").send_keys("consulta")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'800000010 | Consulta odontológica')]"))).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                 "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]"))).click()
        element = self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']")
        actionchains = ActionChains(self.driver)
        actionchains.double_click(element).perform()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                "//img[@src='/cluder/Imagens/icone_voltar.png']"))).click()
        print("Odontologia verficado")

        # Estética
        self.driver.find_element(By.XPATH, "//div[@class='panel-body'][contains(.,'Estética')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Buscar na rede credenciada')]").click()
        self.driver.find_element(By.ID, "especialidades").send_keys("limpeza")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'95111111 | Limpeza de pele')]"))).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                 "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]"))).click()
        element = self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']")
        actionchains = ActionChains(self.driver)
        actionchains.double_click(element).perform()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                    "//img[@src='/cluder/Imagens/icone_voltar.png']"))).click()
        print("Estética verficada")

#     # Fim do programa
        self.driver.close()
