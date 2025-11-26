from pathlib import Path
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def load_config() -> dict:
    root_dir = Path(__file__).resolve().parents[2]
    config_path = root_dir / "config" / "config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def str_to_bool(value: str) -> bool:
    return value.lower() in ("1", "true", "yes", "y", "on")


def create_driver():
    config = load_config()
    browser = config.get("browser", "chrome").lower()

    headless_env = os.getenv("HEADLESS")
    if headless_env is not None:
        headless = str_to_bool(headless_env)
    else:
        headless = config.get("headless", False)

    if browser == "chrome":
        options = Options()
        if headless:
            options.add_argument("--headless=new")

        # Opciones útiles para automatización
        options.add_argument("--start-maximized")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--incognito")

        # Desactivar el password manager y prompts de guardado de contraseña
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        }
        options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(config.get("implicit_wait", 5))
    driver.set_page_load_timeout(config.get("page_load_timeout", 20))

    return driver
