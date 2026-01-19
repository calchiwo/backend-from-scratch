from fastapi import FastAPI

app = FastAPI()

@app.get("/health_check")
async def ping():
    return {"result": "healthy"}
