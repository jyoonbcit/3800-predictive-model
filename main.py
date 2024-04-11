from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from mangum import Mangum
from api.api_v1.api import router as api_router

app = FastAPI()

# Should be adjusted to the live site for eventual deployment.
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def main():
    return {"Hello": "World"}

# Adds the routes defined in api_v1/api.py to the app
app.include_router(api_router, prefix="/api/v1")

# handler = Mangum(app)