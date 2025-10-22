import os
from datetime import datetime
import pytest

def _ensure_dirs():
    os.makedirs("reports/screenshots", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Si el test falla y existe la fixture 'driver', guarda:
      - Screenshot (PNG)
      - HTML de la página
    en reports/screenshots/.
    Además, agrega las rutas como propiedades del test.
    """
    outcome = yield
    rep = outcome.get_result()
    if rep.when != "call" or rep.passed:
        return

    driver = item.funcargs.get("driver")
    if driver is None:
        return

    _ensure_dirs()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = item.name.replace("/", "_").replace("\\", "_")
    png_path = f"reports/screenshots/{safe_name}_{ts}.png"
    html_path = f"reports/screenshots/{safe_name}_{ts}.html"

    try:
        driver.save_screenshot(png_path)
    except Exception:
        png_path = "(screenshot error)"

    try:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(driver.page_source)
    except Exception:
        html_path = "(page_source error)"

    rep.user_properties = rep.user_properties or []
    rep.user_properties.append(("screenshot", png_path))
    rep.user_properties.append(("page_source", html_path))
