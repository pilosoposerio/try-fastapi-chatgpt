from fastapi import FastAPI

from try_fastapi_chatgpt.travel_recommendation.recommendation_strategy import (
    BoringTravelRecommendationStrategy,
)
from try_fastapi_chatgpt.travel_recommendation.travel_recommender import (
    TravelRecommender,
)

app = FastAPI()

travel_recommender = TravelRecommender(
    BoringTravelRecommendationStrategy()
)


@app.get("/")
async def root():
    """
    API root path.
    """
    return {"message": "Hello World"}


@app.get("/recommend")
async def recommend_travel_activities(country: str, season: str):
    """
    Recommends three travel activities for a given country and season
    :param country: Name of a country.
    :param season: Name of a season (or weather condition).
    :return: A JSON list of objects with the country, season, and one activity.
    """
    return [
        {
            "country": recommendation.country,
            "season": recommendation.season,
            "activity": recommendation.recommendation,
        }
        for recommendation in travel_recommender.recommend(
            country, season
        )
    ]
