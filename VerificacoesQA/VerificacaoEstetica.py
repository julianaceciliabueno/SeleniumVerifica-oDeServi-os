# minhas importacoes
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
fake = Faker('pt_BR')


class Test_busca_rede():
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=
                                       'C:\\Users\\Juliana.bueno\\Desktop\\ConsultasServicos\\drivers\\chromedriver.exe')
    def teardown_method(self):
        self.driver.quit()

    def test_configuracao(self):
        self.driver.get("https://qa.clude.com.br/cluder/Login/Index2")
        self.driver.maximize_window()

        # Login
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("@uorak.com")
        self.driver.find_element(By.ID, "senha").click()
        self.driver.find_element(By.ID, "senha").send_keys("xxx")
        self.driver.find_element(By.XPATH, "//button[@class='btn-primary'][contains(.,'Entrar na conta')]").click()
        time.sleep(3)


        # iniciando
        self.driver.find_element(By.XPATH, "//span[contains(.,'Saúde')]")
        self.driver.find_element(By.XPATH, "//span[contains(.,'Saúde')]").click()
        self.driver.find_element(By.XPATH,
                                 "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[2]/div[1]/a[1]/div[1]").click()

        # verificacao de disponibilidade das Sessões de estética
        self.driver.find_element(By.XPATH, "//div[@class='panel-body'][contains(.,'Estética')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Buscar na rede credenciada')]").click()
        self.driver.find_element(By.ID, "especialidades").send_keys("limpeza")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'95111111 | Limpeza de pele')]"))).click()
        print("Consulta estética Limpeza de pele encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("drenagem")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                "//div[@tabindex='-1'][contains(.,'95111114 | Drenagem linfatica corporal')]"))).click()
        time.sleep(4)
        print("Consulta estética encontrada")

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Peeling")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                "// div[@ tabindex='-1'][contains(., '95111139 | Peeling Diamante')]"))).click()
        time.sleep(4)
        print("Consulta estética drenagem encontrada")

        # Fim do programa
        self.driver.close()
