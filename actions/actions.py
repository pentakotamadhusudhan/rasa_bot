from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHandleIssue(Action):
    def name(self) -> Text:
        return "action_handle_issue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        last_message = tracker.latest_message.get('text')
        dispatcher.utter_message(text=f"Thank you for the info. I've created a ticket for your issue: \"{last_message}\". We'll get back to you shortly.")
        return []
