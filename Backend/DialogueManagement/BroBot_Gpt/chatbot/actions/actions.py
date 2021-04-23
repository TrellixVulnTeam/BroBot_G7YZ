# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa.shared.core.events import UserUttered
from rasa_sdk.executor import CollectingDispatcher
import requests


#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class GptResponse(Action):

    def name(self) -> Text:
        return "action_response_from_therapist"

    def run(
            self,
            dispatcher,
            tracker: Tracker,
            domain: "DomainDict",
    ):
        last_msg = tracker.latest_message['text']
        print(last_msg)
        last_intent = tracker.get_intent_of_latest_message(
            skip_fallback_intent=True)
        print(last_intent)

        url = 'http://127.0.0.1:6900'
        post_obj = {'input': last_msg}

        x = requests.post(url, data=post_obj)
        gpt_response = x.text
        _split = gpt_response.split('.')
        gpt_response = ".".join(_split[:-1])
        if gpt_response is None:
            return [UserUttered(text="/bye", intent={"name": "goodbye", "confidence": 1.0})]
        dispatcher.utter_message(gpt_response + '\n')
        return []
