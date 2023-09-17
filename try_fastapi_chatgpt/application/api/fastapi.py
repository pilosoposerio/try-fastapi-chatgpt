from enum import Enum

from fastapi import FastAPI, Query, HTTPException, status
from typing_extensions import Annotated

from try_fastapi_chatgpt.travel_recommendation import (
    TravelRecommender,
    BoringTravelRecommendationStrategy,
    ChatGPTTravelRecommendationStrategy,
    UnknownCountryError,
    TravelRecommendationStrategyError,
)

app = FastAPI()

travel_recommender = TravelRecommender(ChatGPTTravelRecommendationStrategy())


class Season(str, Enum):
    FALL = "fall"
    WINTER = "winter"
    SPRING = "spring"
    SUMMER = "summer"
    AUTUMN = "autumn"


@app.get("/")
def root():
    """
    API root path.
    """
    return {"message": "Hello World"}


@app.get("/recommend")
def recommend_travel_activities(
    country: Annotated[
        str,
        Query(
            min_length=2,
            description=(
                "Travel destination; accepts ISO codes, country name;"
                " we try to intelligently detect the country"
                " based from your input."
            ),
        ),
    ],
    season: Annotated[
        Season, Query(min_length=3, description="Four major seasons.")
    ],
):
    """
    Recommends three travel activities for a given country and season.
    """
    try:
        recommendations = travel_recommender.recommend(country, season)
        return {
            "country": recommendations[0].country,
            "season": season,
            "recommendations": [
                recommendation.recommendation
                for recommendation in recommendations
            ],
        }
    except UnknownCountryError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{exc}",
        ) from exc
    except TravelRecommendationStrategyError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"{exc}"
        ) from exc
