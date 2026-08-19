from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "true"}

@app.get("/other")
def main():
     return {"status": "true"}

