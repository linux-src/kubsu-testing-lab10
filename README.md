# Лабораторная работа 10 — автотесты в GitHub Actions

Простое FastAPI-приложение (`main.py`) и его автотесты (`tests.py`, unittest + TestClient).
При каждом push GitHub Actions поднимает Ubuntu, ставит зависимости и запускает тесты с отчётом покрытия
(`.github/workflows/test_on_push.yaml`).

Локально:

```bash
pip install -r requirements.txt coverage
coverage run -m unittest -v tests.py && coverage report -m
uvicorn main:app --reload   # http://127.0.0.1:8000
```
