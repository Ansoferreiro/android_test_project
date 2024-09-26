from appium import webdriver

def setup_driver():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "Seu_Versão_Android",  # Exemplo: "11.0"
        "deviceName": "Seu_Nome_Dispositivo",      # Exemplo: "emulator-5554" ou "Android Emulator"
        "app": "Caminho/para/seu/app.apk",         # Caminho para o APK que você deseja testar
        "automationName": "UiAutomator2",          # Se você estiver usando o driver UiAutomator2
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    return driver

if __name__ == "__main__":
    driver = setup_driver()
    # Adicione seu código de teste aqui

    print(desired_caps)

def test_calculator(driver):
    # Exemplo de interação com a calculadora
    driver.find_element_by_id("digit_1").click()  # Pressionar '1'
    driver.find_element_by_accessibility_id("plus").click()  # Pressionar '+'
    driver.find_element_by_id("digit_2").click()  # Pressionar '2'
    driver.find_element_by_accessibility_id("equals").click()  # Pressionar '='
    
    # Aguardar um tempo para ver o resultado
    time.sleep(2)

    # Fechar o aplicativo
    driver.quit()

if __name__ == "__main__":
    driver = setup_driver()
    test_calculator(driver)
