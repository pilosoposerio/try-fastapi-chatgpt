import json
import logging
from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import List, Final, Tuple, Dict

import openai

from try_fastapi_chatgpt.travel_recommendation.travel_recommendation import (
    TravelRecommendation,
)


@dataclass(frozen=True)
class TravelRecommendationStrategy(ABC):
    @abstractmethod
    def recommend(
        self, country: str, season: str
    ) -> List[TravelRecommendation]:
        pass


@dataclass(frozen=True)
class BoringTravelRecommendationStrategy(TravelRecommendationStrategy):
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


@dataclass(frozen=True)
class ChatGPTTravelRecommendationStrategy(TravelRecommendationStrategy):
    N_RECOMMENDATIONS: Final[int] = 3
    MODEL: Final[str] = "gpt-3.5-turbo-0613"
    PROMPTS: Final[Tuple[Dict[str, str], ...]] = (
        {
            "role": "system",
            "content": (
                "Pretend to be an expert travel advisor who knows what to do"
                " during any season on any country in the world. You will be"
                " given a country name and a season separated by a colon and"
                " you will respond with three different recommendations. Each"
                " recommendation must be composed of up to three sentences"
                " describing the best activity to do during the given season"
                " on the given country. Do not include any explanations,"
                " only provide a  RFC8259 compliant JSON response."
            ),
        },
        {
            "role": "user",
            "content": "Estonia: winter",
        },
        {
            "role": "assistant",
            "content": json.dumps(
                [
                    "See frozen waterfalls. In the coldest months, the"
                    " unremarkable small streams of water in summer, become"
                    " spectacular frozen falls in winter, like the Jagala"
                    " waterfall, which becomes a wall of icicles that come"
                    " down from a fifty meter wide rock crest.",
                    "Enjoy winter sports. Visit Otepaa, the winter capital of"
                    " Estonia and do hiking, biking, skiing, sledging, and"
                    " snowshoeing in the sparkling winter scenery.",
                    "Visit Soomaa National Park. During winter, its flooded"
                    " forests turn into enchanting and mystical bayous",
                ]
            ),
        },
        {
            "role": "user",
            "content": "Philippines: winter",
        },
        {
            "role": "assistant",
            "content": json.dumps(
                [
                    "Beach hopping. Visit world-renowned islands and beaches like"
                    " Palawan, Siargao, and Boracay.",
                    "Attend festivals. Experience unique festivals like Sinulog in"
                    " Cebu, Ati-Atihan in Kalibo, and Panagbenga in Baguio. These "
                    " celebrations feature colorful parades, traditional dances,"
                    " and delicious food.",
                    "Trekking and Hiking. Explore the lush, tropical"
                    " jungles and mountainous regions. Some popular trekking"
                    " destinations include Mt. Pinatubo, Mt. Pulag, and Mt. Apo.",
                ]
            ),
        },
    )

    def recommend(
        self, country: str, season: str
    ) -> List[TravelRecommendation]:
        prompt: Dict[str, str] = {
            "role": "user",
            "content": f"{country}: {season}",
        }
        messages: List[Dict] = list(self.__class__.PROMPTS) + [prompt]
        response = openai.ChatCompletion.create(
            model=self.__class__.MODEL,
            messages=messages,
            temperature=0.8,
        )

        # log
        logging.debug(response)

        choices_json_str: str = response["choices"][0]["message"]["content"]

        try:
            recommendations: List = json.loads(choices_json_str)
        except json.decoder.JSONDecodeError as exc:
            logging.exception(f"JSON input: {choices_json_str}")
            raise

        assert len(recommendations) == self.__class__.N_RECOMMENDATIONS, (
            f"Expecting {self.__class__.N_RECOMMENDATIONS} recommendations, but"
            f"got {len(recommendations)}"
        )

        return [
            TravelRecommendation(country, season, recommendation)
            for recommendation in recommendations
        ]
