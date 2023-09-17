from dataclasses import dataclass


@dataclass(frozen=True)
class TravelRecommendation:
    country: str
    season: str
    recommendation: str
