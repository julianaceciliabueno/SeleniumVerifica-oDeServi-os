# minhas importacoes
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker

fake = Faker('pt_BR')


class Test_logindiario_segunda_parte():
    def setup_method(self):
        self.driver = webdriver.Firefox(
            executable_path='C:\\Users\\Juliana.bueno\\Desktop\\ConsultaServicos\\drivers\\geckodriver.exe')

    def teardown_method(self):
        self.driver.quit()

    def test_pessoal(self):
        self.driver.get("https://qa.clude.com.br/cluder/Login/Index2")
        # self.driver.set_window_size(1382, 744)
        self.driver.maximize_window()

        # Login
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("@uorak.com")
        self.driver.find_element(By.ID, "senha").click()
        self.driver.find_element(By.ID, "senha").send_keys("xxx")
        self.driver.find_element(By.XPATH, "//button[@class='btn-primary'][contains(.,'Entrar na conta')]").click()
        time.sleep(10)
        # self.driver.implicitly_wait(30)

        # iniciando
        self.driver.find_element(By.XPATH, "//span[contains(.,'Saúde')]")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Saúde')]").click()
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[2]/div[1]/a[1]/div[1]").click()


        # consulta
        self.driver.find_element(By.XPATH,"//div[@class='panel-body'][contains(.,'Consulta')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Buscar na rede credenciada')]").click()
        self.driver.find_element(By.ID, "especialidades").send_keys("pediatria")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@tabindex='-1'][contains(.,'00010057 | Consulta em Pediatria - Especialidade Básica')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//td[@class='text-center']").click()
        element = self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']")
        actionchains = ActionChains(self.driver)
        actionchains.double_click(element).perform()
        self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']").click()
        time.sleep(10)


        # exames
        self.driver.find_element(By.XPATH, "//div[@class='panel-body'][contains(.,'Exames')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Prefiro fazer o orçamento sozinho')]").click()
        self.driver.find_element(By.ID, "especialidades").send_keys("mamografia")
        time.sleep(5)
        self.driver.find_element(By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'40808041 | RX_Mamografia digital bilateral')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'1')]").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success'][contains(.,'Finalizar')]").click()

        element = self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']")
        actionchains = ActionChains(self.driver)
        actionchains.double_click(element).perform()
        self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']").click()
        time.sleep(10)


        # vacinas
        self.driver.find_element(By.XPATH, "//div[@class='panel-body'][contains(.,'Vacinas')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Buscar na rede credenciada')]").click()
        self.driver.find_element(By.ID, "especialidades").send_keys("gripe")
        time.sleep(5)
        self.driver.find_element(By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'90000024 | Gripe')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]").click()
        element = self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']")
        actionchains = ActionChains(self.driver)
        actionchains.double_click(element).perform()
        self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']").click()
        time.sleep(10)

        # Sessões e terapias
        self.driver.find_element(By.XPATH, "//div[@class='panel-body'][contains(.,'Sessões e terapias')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Buscar na rede credenciada')]").click()
        self.driver.find_element(By.ID, "especialidades").send_keys("psicologia")
        time.sleep(5)
        self.driver.find_element(By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'21190001 | Sessao de Psicologia')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]").click()
        element = self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']")
        actionchains = ActionChains(self.driver)
        actionchains.double_click(element).perform()
        self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']").click()
        time.sleep(10)

        # Odontologia
        self.driver.find_element(By.XPATH, "//div[@class='panel-body'][contains(.,'Odontologia')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Buscar na rede credenciada')]").click()
        self.driver.find_element(By.ID, "especialidades").send_keys("consulta")
        time.sleep(5)
        self.driver.find_element(By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'800000010 | Consulta odontológica')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]").click()
        element = self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']")
        actionchains = ActionChains(self.driver)
        actionchains.double_click(element).perform()
        self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']").click()
        time.sleep(10)

        # Estética
        self.driver.find_element(By.XPATH, "//div[@class='panel-body'][contains(.,'Estética')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Buscar na rede credenciada')]").click()
        self.driver.find_element(By.ID, "especialidades").send_keys("limpeza")
        time.sleep(5)
        self.driver.find_element(By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'95111111 | Limpeza de pele')]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[2]/div[1]/div[3]/table[1]/tbody[1]/tr[1]/td[1]").click()
        element = self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']")
        actionchains = ActionChains(self.driver)
        actionchains.double_click(element).perform()
        self.driver.find_element_by_xpath("//img[@src='/cluder/Imagens/icone_voltar.png']").click()
        time.sleep(10)
# (em QA não estão funcionando pronto socorro e  Práticas Integrativas )
    # Fim do programa
        self.driver.close()
