# proyecto-final-automation-testing-jorge-noguera

Framework de automatización de pruebas en Python que combina pruebas de UI con Selenium WebDriver y pruebas de API con Requests, utilizando Pytest como framework de testing y generando reportes HTML. Este proyecto forma parte del trabajo final integrador del curso de automatización.

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
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/jorge-noguera/proyecto-final-automation-testing.git
cd proyecto-final-automation-testing
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv venv
```

**Windows**
```bash
venv\Scripts\activate
```

**macOS/Linux**
```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Configuración

El archivo `config/config.json` controla parámetros clave:

```json
{
  "base_url": "https://www.saucedemo.com",
  "browser": "chrome",
  "implicit_wait": 5,
  "headless": false
}
```

Podés modificar el navegador, el tiempo de espera o ejecutar en modo headless.

## Cómo ejecutar las pruebas

### Ejecutar todas las pruebas

```bash
pytest
```

### Ejecutar solo pruebas de UI

```bash
pytest -m ui
```

### Ejecutar solo pruebas de API

```bash
pytest -m api
```

### Generar reporte HTML

```bash
pytest --html=reports/report.html
```

El reporte se guardará en la carpeta `reports/`.

## Capturas de pantalla y logs

- Las capturas de fallos se guardan en `screenshots/`.  
- Los logs de ejecución se almacenan en `logs/`.  

## Integración continua (GitHub Actions)

El repositorio incluye un workflow de CI ubicado en:

```text
.github/workflows/ci.yml
```

Este workflow instala dependencias, ejecuta las pruebas y publica artefactos de la ejecución.

## Datos de prueba

Los archivos JSON en `data/` contienen los datos usados durante las pruebas:

- `ui_test_data.json`  
- `api_test_data.json`  
