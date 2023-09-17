from dataclasses import dataclass
from typing import List

from try_fastapi_chatgpt.travel_recommendation.recommendation_strategy import (
    TravelRecommendationStrategy,
)
from try_fastapi_chatgpt.travel_recommendation.travel_recommendation import (
    TravelRecommendation,
)


@dataclass(frozen=True)
class TravelRecommender:
    """
    A class that uses any recommendation strategy to provide travel
    recommendations.
    """

    recommender: TravelRecommendationStrategy

    def recommend(
        self, country: str, season: str
    ) -> List[TravelRecommendation]:
        return self.recommender.recommend(country, season)
