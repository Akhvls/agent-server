from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "truee"}

@app.get("/other")
def main():
     return {"status": "true"}

