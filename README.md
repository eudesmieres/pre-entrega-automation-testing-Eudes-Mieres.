# Pre-Entrega Automation Testing – Eudes Mieres

Automatizaciones sobre [saucedemo.com](https://www.saucedemo.com) para la pre-entrega del curso.

## Objetivo
Cumplir las consignas obligatorias con **esperas explícitas**, código organizado, reporte **HTML**

- **Login**: navegar, ingresar credenciales válidas, validar `/inventory.html` y título (“Products”/“Swag Labs”) con **WebDriverWait**.

- **Catálogo**: validar título, existencia de productos, UI (menú y sort), listar **nombre y precio** del primer producto.
- **Carrito**: agregar primer producto, validar **badge=1**, navegar al carrito y confirmar que el ítem está presente.

## 🧰 Tecnologías
- Python
- Pytest
- Selenium WebDriver
- Webdriver-Manager (gestión automática de ChromeDriver) **o** Selenium Manager
- Pytest-HTML (reporte)

## 📁 Estructura
- README.md
- reports/ # (se genera en runtime)
- reporte.html # (pytest --html)
- screenshots/ # (autogenerado en fallos)
- test/
- test_saucedemo.py # login + catálogo + carrito
- utils/
- init.py
- helpers.py # driver + login (con esperas explícitas)

## requirements.txt mínimo:
selenium==4.36.0
webdriver-manager==4.0.2
pytest==8.4.2
pytest-html==4.1.1

## Cómo ejecutar todos los tests + reporte HTML auto-contenido
pytest -v --html=reports/reporte.html --self-contained-html

