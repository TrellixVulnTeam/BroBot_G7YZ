from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from googlesearch import search
from youtubesearchpython import SearchVideos
from random import randrange
import requests


class InitialForm(FormAction):

    def name(self):
        return "initial_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name", "age", "gender", "sleep_time", "eat_healthy", "today_goal"]

    def submit(
            self,
            dispatcher: "CollectingDispatcher",
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "name": [
                self.from_entity(entity="name"),
                # self.from_entity(intent="deny")
            ],
            "age": [
                self.from_entity(entity="age"),
                # self.from_entity(intent="deny"),
            ],
            "gender": [
                self.from_entity(entity="gender"),
            ],
            "sleep_time": [
                self.from_entity(entity="sleep_time"),
            ],
            "eat_healthy": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
            ],
            "today_goal": [
                self.from_entity(entity="today_goal"),
                self.from_text(intent="inform_today_goal"),
            ]
        }


# recommendation using the user interest
class Recommendation(Action):
    def name(self) -> Text:
        return "action_get_recommendation_interest"

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        intent_recommendation = {
            "mood_love": ["music", "romance"],
            "mood_anger": ["videos", "funny"],
            "mood_joy": ["article", "Data Science"],
            "mood_fear": ["videos", "motivation"],
            "mood_surprise": ["music", "peaceful"],
            "mood_sadness": ["videos", "Things to be happy about"],
        }
        intent_confidence = tracker.latest_message['latest_message']['intent']['confidence']
        intent = tracker.get_intent_of_latest_message(skip_fallback_intent=True)
        print("intent of last message: ", intent)
        type_of_category = intent_recommendation[intent][0].lower()
        interest_topic = intent_recommendation[intent][1].lower()
        # fetch these recommendations from Database. These are dummy values.
        # type_of_category = "music"
        # type_of_category = type_of_category.lower()
        # interest_topic = "ali zafar"

        max_searches = 10
        number = randrange(max_searches)

        link = ""

        # for searching on google related to articles , book , news
        if type_of_category == "article" or type_of_category == 'book' or type_of_category == 'news':
            query = "'" + interest_topic + "'" + " " + type_of_category
            gen = list(search(query, num=max_searches, start=0, stop=max_searches, tld='com'))
            link = gen[number]

        # for searching on youtube related to music , videos
        elif type_of_category == 'music' or type_of_category == 'videos':
            result = SearchVideos(interest_topic, offset=0, mode="dict", max_results=max_searches)
            link = result.result()['search_result'][number]['link']
            # print(result.result()['search_result'][number]['title'])
        else:
            print("Sorry No Recommendation Can be Suggested At The Moment.Category should be in [article,book,news,"
                  "music,videos]")
        dispatcher.utter_message("Here is something for you:\n" + link)

        return []


class ElizaResponse(Action):

    def name(self) -> Text:
        return "action_eliza_response"

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        url = '127.0.0.1:9010'
        post_obj = {'input': tracker.latest_message['text']}

        x = requests.post(url, data=post_obj)

        dispatcher.utter_message(x.text + '\n')
        return []
