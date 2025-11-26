# proyecto-final-automation-testing-jorge-noguera

Framework de automatización de pruebas en Python que combina pruebas de UI con Selenium WebDriver y pruebas de API con Requests, utilizando Pytest como framework de testing y generando reportes HTML. Forma parte del trabajo final integrador del curso de automatización.

## Tecnologías utilizadas

- Python 3.12
- Pytest
- Selenium WebDriver
- Requests
- pytest-html
- GitHub Actions
- Git y GitHub

## Estructura del proyecto

```text
proyecto-final-automation-testing-jorge-noguera/
│
├── config/
│   └── config.json
├── data/
│   ├── ui_test_data.json
│   └── api_test_data.json
├── logs/
├── reports/
├── screenshots/
├── src/
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   ├── tests/
│   │   ├── ui/
│   │   │   ├── test_login.py
│   │   │   └── test_cart_and_checkout.py
│   │   └── api/
│   │       └── test_users_api.py
│   ├── utils/
│   │   ├── driver_factory.py
│   │   ├── logger.py
│   │   ├── screenshot.py
│   │   └── api_client.py
│   └── conftest.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
