from dataclasses import dataclass
from typing import List

import pycountry
from try_fastapi_chatgpt.travel_recommendation.recommendation_strategy import (
    TravelRecommendationStrategy,
)
from try_fastapi_chatgpt.travel_recommendation.travel_recommendation import (
    TravelRecommendation,
)


class UnknownCountryError(ValueError):
    pass


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
        try:
            country_info = pycountry.countries.search_fuzzy(country)[0]
        except LookupError as exc:
            raise UnknownCountryError(
                f"No country matches: {country}"
            ) from exc
        return self.recommender.recommend(country_info.name, season)
