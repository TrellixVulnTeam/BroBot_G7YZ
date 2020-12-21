from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from googlesearch import search
from youtubesearchpython import SearchVideos
from random import randrange

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
class recommendation(Action):
    def name(self)->Text:
        return ("action_get_recommendation_interest");

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        typeOfCategory = "music"
        typeOfCategory = typeOfCategory.lower()
        interestTopic = "ali zafar"

        max_searches = 10
        number = randrange(max_searches)

        link=""

        # for searching on google related to articles , book , news
        if typeOfCategory == "article" or typeOfCategory == 'book' or typeOfCategory == 'news':
            query = "'" + interestTopic + "'" + " " + typeOfCategory
            gen = list(search(query, num=max_searches, start=0, stop=max_searches, tld='com'))
            link = gen[number]

        # for searching on youtube related to music , videos
        elif typeOfCategory == 'music' or typeOfCategory == 'videos':
            result = SearchVideos(interestTopic, offset=0, mode="dict", max_results=max_searches)
            link = result.result()['search_result'][number]['link']
            # print(result.result()['search_result'][number]['title'])
        else:
            print("Sorry No Recommendation Can be Suggested At The Moment.Category should be in [article,book,news,"
                  "music,videoes]")
        dispatcher.utter_message("Here is something for you:\n" +link);
        return [];