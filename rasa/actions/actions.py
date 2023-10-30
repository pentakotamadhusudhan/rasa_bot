# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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
from  typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import Restarted, EventType, SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher
import requests
import re
import json

class ActionGetOptions(Action):

    def name(self) -> Text:
        return "Options"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
        Names = ['Student','Trainer','Organization','Job_Provider']
        buttons=[]
        for word in Names:
            button = {'title': word, 'payload': '/Options{"Options":"'+word+'"}'}   
            buttons.append(button)
        dispatcher.utter_message(text="Please select below Options!",buttons=buttons)

        return[]


class ActionRegister(Action):

    def name(self) -> Text:
        return "post_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        options = tracker.get_slot("Options")
        firstname = tracker.get_slot('Firstname')
        lastname = tracker.get_slot('Lastname')
        email = tracker.get_slot('Email')
        password = tracker.get_slot('Password')

        data = {
            'Options' : options,
            'Firstname' : firstname,
            'Lastname' : lastname,
            'Email' : email,
            'Password' : password
        }
        print(data)
        api = "http://localhost:8000/OpenHealthBot/otp_generation"
        headers = {'Content-Type': 'application/json',
                        'Authorization': 'Bearer <replace the token with open health bot Api (https://github.com/vivifyhealthcare/Open-Health-Bot-API) >'}
        

        print(data,'Data')
        r = requests.post(api, json=data, headers=headers)
        print(r)

        dispatcher.utter_message(text=f"Succesfully Registered your Details")
        
        return []