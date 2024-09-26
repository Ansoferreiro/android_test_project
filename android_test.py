from appium import webdriver
import time
import unittest

class AndroidTests(unittest.TestCase):
    
    def setUp(self):
        # Definindo as capacidades do dispositivo
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Android Emulator",
            "appPackage": "com.android.calculator2",  # Pacote de exemplo para a calculadora
            "appActivity": "com.android.calculator2.Calculator",
            "automationName": "UiAutomator2"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def test_calculator(self):
        # Teste da calculadora
        self.driver.find_element_by_id("digit_1").click()  # Pressionar '1'
        self.driver.find_element_by_accessibility_id("plus").click()  # Pressionar '+'
        self.driver.find_element_by_id("digit_2").click()  # Pressionar '2'
        self.driver.find_element_by_accessibility_id("equals").click()  # Pressionar '='
        
        # Aguardar um tempo para ver o resultado
        time.sleep(2)

    def test_camera(self):
        # Abrir a câmera e tirar uma foto
        self.driver.start_activity("com.android.camera", "com.android.camera.Camera")
        time.sleep(2)  # Esperar a câmera abrir
        
        # Simular o clique do botão de captura
        self.driver.find_element_by_id("com.android.camera:id/shutter_button").click()
        time.sleep(2)  # Esperar a foto ser tirada
        self.driver.quit()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
def test_contacts(self, setup):
    self.driver.start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
    time.sleep(2)  # Aguardar o aplicativo abrir

    # Aqui você pode implementar mais interações com o aplicativo de contatos, como clicar em um contato
    # Por exemplo, clicar no primeiro contato
    self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.android.contacts:id/name']").click()
    time.sleep(2)

    # Fechar o aplicativo de contatos
    self.driver.quit()
