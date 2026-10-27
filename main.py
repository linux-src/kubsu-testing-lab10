from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")  # http://127.0.0.1:8000
def root():
    return FileResponse("public/index.html")


@app.get("/hello")  # http://127.0.0.1:8000/hello
def hello():
    return {"message": "Hello world!"}


@app.get("/about")  # http://127.0.0.1:8000/about
def about():
    return {"message": "О сайте"}


@app.get("/users/{user_id}")  # http://127.0.0.1:8000/users/123
def user_by_id(user_id: int):
    return {"user_id": user_id}


@app.get("/users")  # http://127.0.0.1:8000/users?name=Tom&age=38
def get_user(name: str, age: int):
    return {"user_name": name, "user_age": age}


@app.get("/sum")  # http://127.0.0.1:8000/sum?a=2&b=3
def calc_sum(a: float, b: float):
    return {"result": a + b}


@app.get("/multiply")  # http://127.0.0.1:8000/multiply?a=4&b=5
def multiply(a: float, b: float):
    return {"result": a + b}


@app.get("/notfound", status_code=404)  # http://127.0.0.1:8000/notfound
def notfound():
    return {"message": "Resource Not Found"}
