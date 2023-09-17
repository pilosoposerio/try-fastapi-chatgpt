from fastapi import FastAPI, Query, HTTPException.
from typing_extensions import Annotated

from try_fastapi_chatgpt.travel_recommendation.recommendation_strategy import (
    BoringTravelRecommendationStrategy,
)
from try_fastapi_chatgpt.travel_recommendation.travel_recommender import (
    TravelRecommender,
    UnknownCountryError,
)

app = FastAPI()

travel_recommender = TravelRecommender(BoringTravelRecommendationStrategy())


@app.get("/")
def root():
    """
    API root path.
    """
    return {"message": "Hello World"}


@app.get("/recommend")
def recommend_travel_activities(
    country: Annotated[str, Query(min_length=2)],
    season: Annotated[str, Query(min_length=3)],
):
    """
    Recommends three travel activities for a given country and season
    :param country: Name of a country.
    :param season: Name of a season (or weather condition).
    :return: A JSON list of objects with the country, season, and one activity.
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
        raise HTTPException(detail=f"Unknown country: {country}")
