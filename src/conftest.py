import pytest

from utils.driver_factory import create_driver, load_config
from utils.screenshot import save_screenshot
from utils.api_client import ApiClient
from utils.logger import get_logger


@pytest.fixture(scope="session")
def config_data() -> dict:
    return load_config()


@pytest.fixture(scope="session")
def logger():
    return get_logger("test_run")


@pytest.fixture
def driver(config_data, logger):
    logger.info("Creating WebDriver instance")
    driver = create_driver()
    base_url = config_data.get("base_url")
    if base_url:
        logger.info(f"Opening base URL: {base_url}")
        driver.get(base_url)
    yield driver
    logger.info("Quitting WebDriver instance")
    driver.quit()


@pytest.fixture(scope="session")
def api_client():
    return ApiClient()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook used to detect test failures and attach screenshots to the HTML report.
    """
    outcome = yield
    report = outcome.get_result()

    # Solo nos interesa cuando el test ya ejecutó el cuerpo (when == "call")
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        is_ui_test = "ui" in item.keywords

        if driver is not None and is_ui_test:
            test_name = item.name
            screenshot_path = save_screenshot(driver, test_name)

            # Intentar adjuntar la imagen al reporte HTML
            try:
                from pytest_html import extras

                extra = getattr(report, "extra", [])
                # Usar image con ruta de archivo (pytest-html se encarga de leerla y embederla)
                extra.append(extras.image(str(screenshot_path)))
                report.extra = extra
            except ImportError:
                # Si pytest-html no está disponible, simplemente ignorar
                pass
