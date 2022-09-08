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
        self.driver = webdriver.Chrome(
            executable_path=
            'C:\\Users\\Juliana.bueno\\Desktop\\ConsultasServicos\\drivers\\chromedriver.exe')


    def teardown_method(self):
        self.driver.quit()

    def test_pessoal(self):
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
                                 "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[7]/div[2]/div[1]/a[1]/div[1]").click()

        # verificacao de disponibilidade das consultas

        self.driver.find_element(By.XPATH, "//div[@class='panel-body'][contains(.,'Consulta')]").click()
        self.driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Buscar na rede credenciada')]").click()
        self.driver.find_element(By.ID, "especialidades").send_keys("pediatria")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//div[@tabindex='-1'][contains(.,'00010057 | Consulta em Pediatria - Especialidade Básica')]"))).click()
        print("Consulta pediatria encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Alergia e imunologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//div[@tabindex='-1'][contains(.,'00010015 | Consulta em Alergia e imunologia')]"))).click()
        print("Consulta Alergia e imunologia encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Angiologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//div[@tabindex='-1'][contains(.,'00010017 | Consulta em Angiologia')]"))).click()
        print("Consulta Angiologia encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Dermatologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//div[@tabindex='-1'][contains(.,'00010031 | Consulta em Dermatologia')]"))).click()
        print("Consulta Dermatologia encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Endocrinologia e metabologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//div[@tabindex='-1'][contains(.,'00010032 | Consulta em Endocrinologia e metabologia')]"))).click()
        print("Consulta Endocrinologia e metabologia encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Gastroenterologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//div[@tabindex='-1'][contains(.,'00010033 | Consulta em Gastroenterologia')]"))).click()
        print("Consulta Gastroenterologia encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Geriatria")
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//div[@tabindex='-1'][contains(.,'00010035 | Consulta em Geriatria')]"))).click()
        print("Consulta Geriatria encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Ginecologia e obstetrícia")
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//div[@tabindex='-1'][contains(.,'00010036 | Consulta em Ginecologia e obstetrícia')]"))).click()
        print("Consulta Ginecologia e obstetrícia encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Neurologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//div[@tabindex='-1'][contains(.,'00010052 | Consulta em Neurologia')]"))).click()
        print("Consulta Neurologia encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Nutrologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//div[@tabindex='-1'][contains(.,'00010053 | Consulta em Nutrologia')]"))).click()
        print("Consulta Nutrologia encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Oftalmologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010054 | Consulta em Oftalmologia - Especialidade Básica')]"))).click()
        print("Consulta Oftalmologia encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Ortopedia e traumatologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "//div[@tabindex='-1'][contains(.,'00010055 | Consulta em Ortopedia e traumatologia - Especialidade Básica')]"))).click()
        print("Consulta Ortopedia e traumatologia encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Otorrinolaringologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010056 | Consulta em Otorrinolaringologia')]"))).click()
        print("Consulta Otorrinolaringologia encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Coloproctologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010030 | Consulta em Coloproctologia')]"))).click()
        print("Consulta Coloproctologia encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Psiquiatria")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010059 | Consulta em Psiquiatria')]"))).click()
        print("Consulta Psiquiatria encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Urologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010061 | Consulta em Urologia')]"))).click()
        print("Consulta Urologia encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Pneumologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010058 | Consulta em Pneumologia')]"))).click()
        print("Consulta Pneumologia encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("ambulatorial por nutricionista")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '50000560 | Consulta ambulatorial por nutricionista')]"))).click()
        print("Consulta ambulatorial por nutricionista encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("psicologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '50000462 | Consulta em psicologia')]"))).click()
        print("Consulta psicologia encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Reumatologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010060 | Consulta em Reumatologia')]"))).click()
        print("Consulta Reumatologia encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Cirurgia vascular")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010028 | Consulta em Cirurgia vascular')]"))).click()
        print("Consulta Cirurgia vascular encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Hepatologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010062 | Consulta em Hepatologia')]"))).click()
        print("Consulta Hepatologia encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("nutrológica")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '20101074 | Avaliação nutrológica (inclui consulta)')]"))).click()
        print("Consulta nutrológica encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Cirurgia cardiovascular")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010020 | Consulta em Cirurgia cardiovascular')]"))).click()
        print("Consulta Cirurgia cardiovascular encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Homeopatia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010038 | Consulta em Homeopatia')]"))).click()
        print("Consulta Homeopatia encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Nefrologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                        "// div[ @ tabindex = '-1'][contains(., '00010050 | Consulta em Nefrologia')]"))).click()
        print("Consulta Nefrologia encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Mastologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010040 | Consulta em Mastologia')]"))).click()
        print("Consulta Mastologia encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("fonoaudiologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '50000586 | Consulta individual ambulatorial de fonoaudiologia')]"))).click()
        print("Consulta fonoaudiologia encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Cirurgia plástica")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010026 | Consulta em Cirurgia plástica')]"))).click()
        print("Consulta Cirurgia plástica encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Hematologia e hemoterapia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010037 | Consulta em Hematologia e hemoterapia')]"))).click()
        print("Consulta Hematologia e hemoterapia encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Infectologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010039 | Consulta em Infectologia')]"))).click()
        print("Consulta Infectologia encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Neurocirurgia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010051 | Consulta em Neurocirurgia')]"))).click()
        print("Consulta Neurocirurgia encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Fisioterapia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '71010009 | Fisioterapia consulta')]"))).click()
        print("Consulta Fisioterapia encontrada")
        time.sleep(4)


        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("aparelho digestivo")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010023 | Consulta em Cirurgia do aparelho digestivo')]"))).click()
        print("Consulta aparelho digestivo encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Cancerologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010018 | Consulta em Cancerologia')]"))).click()
        print("Consulta Cancerologia encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Cirurgia da mão")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010021 | Consulta em Cirurgia da mão')]"))).click()
        print("Consulta Cirurgia da mão encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Genética médica")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010034 | Consulta em Genética médica')]"))).click()
        print("Consulta Genética médica encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Medicina do trabalho")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010043 | Consulta em Medicina do trabalho')]"))).click()
        print("Consulta Medicina do trabalho encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Cirurgia pediátrica")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010025 | Consulta em Cirurgia pediátrica')]"))).click()
        print("Consulta Cirurgia pediátrica encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Anestesiologia")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010016 | consulta em Anestesiologia')]"))).click()
        print("Consulta Anestesiologia encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Cirurgia de cabeça e pescoço")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010022 | Consulta em Cirurgia de cabeça e pescoço')]"))).click()
        print("Consulta Cirurgia de cabeça e pescoço encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Pronto Socorro")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '10101039 | Consulta Pronto Socorro')]"))).click()
        print("Consulta Pronto Socorro encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("família e comunidade")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010042 | Consulta em Medicina de família e comunidade')]"))).click()
        print("Consulta família e comunidade encontrada")
        time.sleep(4)

        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("terapia ocupacional")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(.,'50000055 | Consulta individual ambulatorial, em terapia ocupacional')]"))).click()
        print("Consulta terapia ocupacional encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Medicina esportiva")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010045 | Consulta em Medicina esportiva')]"))).click()
        print("Consulta Medicina esportiva encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("nutricionista")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '50000578 | Consulta domiciliar por nutricionista')]"))).click()
        print("Consulta nutricionista encontrada")
        time.sleep(4)
        self.driver.find_element(By.ID, "especialidades").clear()
        self.driver.find_element(By.ID, "especialidades").send_keys("Cirurgia torácica")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "// div[ @ tabindex = '-1'][contains(., '00010027 | Consulta em Cirurgia torácica')]"))).click()
        print("Consulta Cirurgia torácica encontrada")
        # # Fim do programa
        self.driver.close()
