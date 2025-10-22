import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.helpers import login_saucedemo, get_driver



@pytest.fixture
def driver():
    # configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()

def test_login(driver):

    login_saucedemo(driver)
    # Espera explícita
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "inventory_container"))
    )
    assert "/inventory.html" in driver.current_url
    titulo = driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text.strip()
    assert titulo in ("Products", "Swag Labs")

def test_catalogo( driver ):
     login_saucedemo( driver )

     products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
     assert len(products) > 0

    # Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)
     assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
     assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()

    # Listar nombre y precio del primer producto (y opcionalmente asertar formato)
     first = products[0]
     name = first.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
     price = first.find_element(By.CLASS_NAME, "inventory_item_price").text.strip()
     print(f"Primer producto: {name} - {price}")
     assert name != "" and price.startswith("$")

def test_carrito(driver):
    login_saucedemo(driver)

    # agregar primer producto
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert products, "No hay productos para agregar al carrito"
    first = products[0]
    name = first.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
    first.find_element(By.TAG_NAME, "button").click()

    # validar que el contador del carrito pasó a 1
    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    ).text.strip()
    assert badge == "1"

    # ir al carrito y verificar item
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_list"))
    )
    names_in_cart = [e.text.strip()
                     for e in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
    assert name in names_in_cart, f"'{name}' no aparece en el carrito"