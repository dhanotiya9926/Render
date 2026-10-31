from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {
        "Message":"Hello this is my first render project"
    }