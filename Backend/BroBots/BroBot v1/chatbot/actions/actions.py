from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


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
