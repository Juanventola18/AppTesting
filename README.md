# AppTesting# TPO2: Automatización de Pruebas y Pipeline CI/CD

Este proyecto implementa un flujo de automatización utilizando **Python**, **Pytest** y **GitHub Actions**.

## Funcionalidad
La aplicación valida montos de facturas según categorías fiscales (A y B) y aplica límites de seguridad.

## Estructura del Proyecto
- `app/`: Contiene la lógica de negocio (`validador.py`).
- `tests/`: Contiene las pruebas unitarias automatizadas (`test_validador.py`).
- `.github/workflows/`: Contiene la definición del pipeline de CI/CD.

## Pipeline CI/CD
El pipeline se ejecuta automáticamente ante cada `push` en la rama principal. 
Realiza las siguientes tareas:
1. Configura el entorno Python.
2. Instala dependencias (`pytest`, `pytest-html`).
3. Ejecuta los tests automatizados.
4. Genera y publica un reporte HTML como artefacto de la ejecución.
