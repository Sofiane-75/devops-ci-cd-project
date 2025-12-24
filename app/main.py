from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Azul, c'est Sofiane !"}

