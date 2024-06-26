from fastapi import APIRouter
from api.api_v1.endpoints.model import use_model

router = APIRouter()

@router.get("/")
def predict(
    assessed_land: float,
    assessed_total: float,
    assessed_improvements: float,
    assessed_land_2022: float,
    assessed_total_2021: float
):
    input_data = {
        '2023 Assessed Land': assessed_land,
        '2022 Assessed Total': assessed_total,
        '2023 Assessed Improvements': assessed_improvements,
        '2022 Assessed Land': assessed_land_2022,
        '2021 Assessed Total': assessed_total_2021
    }
    return {"Data": use_model(input_data)}