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

        # verificacao de disponibilidade dos exames
        self.driver.find_element(By.XPATH, "//div[@class='panel-body'][contains(.,'Exames')]").click()
        self.driver.find_element(By.XPATH,
                                 "//button[@type='button'][contains(.,'Prefiro fazer o orçamento sozinho')]").click()
        self.driver.find_element(By.ID, "especialidades").send_keys("mamografia")
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'40808041 | RX_Mamografia digital bilateral')]").click()
        print("Exame encontrado")
        time.sleep(3)


        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("lactose")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'40302164 | Lactose, teste de tolerancia')]"))).click()
        print("Exame encontrado")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Hemograma")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'40304361 | Hemograma com contagem de plaquetas ou fracoes (eritrograma, leucograma, plaquetas)')]"))).click()
        print("Exame encontrado")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Colesterol")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'40301583 | Colesterol (HDL), dosagem')]"))).click()
        print("Exame encontrado")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Colesterol")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'40301591 | Colesterol (LDL), dosagem')]"))).click()
        print("Exame encontrado")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Colesterol")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'40301605 | Colesterol total, dosagem')]"))).click()
        print("Exame encontrado")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Colesterol")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'40302695 | Colesterol (VLDL), dosagem')]"))).click()
        print("Exame encontrado")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Colesterol")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'40302750 | Perfil lipídico / lipidograma (lípidios totais, colesterol, triglicerídios e eletroforese lipoproteínas), dosagem')]"))).click()
        print("Exame encontrado")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Ureia e Creatinina")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'40301508 | Clearance de creatinina')]"))).click()
        print("Exame encontrado")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Ureia e Creatinina")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'40301524 | Clearance de ureia')]"))).click()
        print("Exame encontrado")
        time.sleep(4)


        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Ureia e Creatinina")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'40301630 | Creatinina, dosagem')]"))).click()
        print("Exame encontrado")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Ureia e Creatinina")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                 "//div[@tabindex='-1'][contains(.,'40302580 | Uréia, dosagem')]"))).click()
        print("Exame encontrado")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Ureia e Creatinina")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//div[@tabindex='-1'][contains(.,'40309444 | Rotina do líquido amniótico-amniograma (citológico espectrofotometria, creatinina e teste de clements)')]"))).click()
        print("Exame encontrado")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("fezes")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//div[@tabindex='-1'][contains(.,'40310370 | Microsporidia, pesquisa nas fezes')]"))).click()
        print("Exame encontrado")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Glicemia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//div[@tabindex='-1'][contains(.,'40302032 | Glicemia após sobrecarga com dextrosol ou glicose, dosagem')]"))).click()
        print("Exame encontrado")
        time.sleep(4)



        # # Fim do programa
        self.driver.close()
