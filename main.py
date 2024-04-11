from fastapi import FastAPI
# from mangum import Mangum
from api.api_v1.api import router as api_router

app = FastAPI()

@app.get("/")
def main():
    return {"Hello": "World"}

# Adds the routes defined in api_v1/api.py to the app
app.include_router(api_router, prefix="/api/v1")

# handler = Mangum(app)