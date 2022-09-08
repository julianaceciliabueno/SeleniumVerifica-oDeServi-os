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

        # verificacao de disponibilidade das Sessões de odonto
        self.driver.find_element(By.XPATH, "//div[@class='panel-body'][contains(.,'Odontologia')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Buscar na rede credenciada')]").click()
        self.driver.find_element(By.ID, "especialidades").send_keys("consulta")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'800000010 | Consulta odontológica')]"))).click()
        print("Consulta odontológica encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("consulta")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                "//div[@tabindex='-1'][contains(.,'800000020 | Consulta odontológica inicial')]"))).click()
        time.sleep(4)
        print("Consulta odontológica encontrada")


        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("consulta")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'800000029 | Consulta para avaliação técnica: auditoria inicial ou final')]"))).click()
        time.sleep(4)
        print("Consulta odontológica encontrada")


        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Consulta")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                "//div[@tabindex='-1'][contains(.,'800001264 | Controle de cárie incipiente - por consulta trimestral')]"))).click()
        time.sleep(4)
        print("Consulta odontológica encontrada")


        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Coroa")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                "//div[@tabindex='-1'][contains(.,'800000381 | Aumento de coroa clínica - por elemento')]"))).click()
        time.sleep(4)
        print("Consulta odontológica encontrada")

        # Fim do programa
        self.driver.close()
