from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Final, Tuple


@dataclass(frozen=True)
class TravelRecommendation:
    country: str
    season: str
    recommendation: str


@dataclass(frozen=True)
class TravelRecommendationStrategy(ABC):
    @abstractmethod
    def recommend(
        self, country: str, season: str
    ) -> List[TravelRecommendation]:
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
        return self.recommender.recommend(country, season)


@dataclass(frozen=True)
class BoringTravelRecommendationStrategy(
    TravelRecommendationStrategy
):
    BORING_RECOMMENDATIONS: Final[Tuple[str, ...]] = (
        (
            "Just think of happy things, and your heart will fly on wings, "
            "forever, in {country}"
        ),
        (
            "Baby you're all that I want... "
            "When you're lyin' here in my arms... "
            "I'm findin' it hard to believe... "
            "We're in {country}"
        ),
        (
            "They say in heaven love comes first... "
            "We'll make heaven a place on {country}."
        ),
    )

    def recommend(
        self, country: str, season: str
    ) -> List[TravelRecommendation]:
        return [
            TravelRecommendation(
                country,
                season,
                recommendation_template.format(country=country),
            )
            for recommendation_template in self.__class__.BORING_RECOMMENDATIONS
        ]
