from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello! My FastAPI app is live "}


@app.get("/hello")
def hello():
    return {"message": "Hello from my deployed API!"}


@app.get("/about")
def about():
    return {
        "project": "Basic FastAPI Deployment",
        "status": "running@3"
    }