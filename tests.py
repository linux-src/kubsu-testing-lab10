"""Автотесты API. TestClient вызывает приложение напрямую, без запуска сервера uvicorn."""
import unittest

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class AppTests(unittest.TestCase):

    def test_root_returns_html(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello World!", response.text)

    def test_hello(self):
        response = client.get("/hello")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello world!"})

    def test_about(self):
        response = client.get("/about")
        self.assertEqual(response.json(), {"message": "О сайте"})

    def test_user_by_id(self):
        response = client.get("/users/123")
        self.assertEqual(response.json(), {"user_id": 123})

    def test_user_by_id_not_a_number(self):
        # id должен быть числом — иначе FastAPI сам отвечает 422 (ошибка валидации)
        response = client.get("/users/abc")
        self.assertEqual(response.status_code, 422)

    def test_users_query(self):
        response = client.get("/users?name=Bob&age=30")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"user_name": "Bob", "user_age": 30})

    def test_users_missing_param(self):
        response = client.get("/users?name=Bob")
        self.assertEqual(response.status_code, 422)

    def test_sum(self):
        response = client.get("/sum?a=2&b=3.5")
        self.assertEqual(response.json(), {"result": 5.5})

    def test_notfound(self):
        response = client.get("/notfound")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
