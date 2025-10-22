from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.saucedemo.com/'
USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():

    # options  = Options()
    # options.add_argument('--start-maximized')


    #instalacion de driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver

def login_saucedemo( driver ):
    driver.get(URL)
    
    # Espera explícita y Credenciales
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "user-name"))
    ).send_keys(USERNAME)
    driver.find_element(By.NAME,'password').send_keys(PASSWORD)
    driver.find_element(By.ID,'login-button').click()

    
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "inventory_container"))
    )
