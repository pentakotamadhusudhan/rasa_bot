from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import smtplib, ssl

# from rasa_sdk.events. import SessionEnded

class ActionHandleIssue(Action):
    def name(self) -> Text:
        return "action_handle_issue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        last_message = tracker.latest_message.get('text')
        dispatcher.utter_message(text=f"Thank you for the info. I've created a ticket for your issue: \"{last_message}\". We'll get back to you shortly.")
        return []




class ActionPrintMessage(Action):
    def name(self) -> str:
        return "action_print_message"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        # Print a message to the console
        print("User reported being unable to book an appointment.")

        # Optionally, send a message to the user
        dispatcher.utter_message(text="We have received your issue and will look into it shortly.")

        return []



sender_email = "pentakotamadhu74@gmail.com"
receiver_email = "hemadhu7@gmail.com"
app_password = "bhoxrazprhssixqb"  # Replace with your App Password


class ActionSendEmail(Action):

    def name(self):
        return "action_send_email"

    def run(self, dispatcher, tracker, domain):
        # Retrieve user details from slots
        user_name = tracker.get_slot("name")
        user_email = tracker.get_slot("email")
        message = "Unable to book appointment"
        sendMail(message)

        # Email configuration
       


class ActionSendDoctorAbsenctEmail(Action):

    def name(self):
        return "action_send_Doctor_absenct_email"

    def run(self, dispatcher, tracker, domain):
        # Retrieve user details from slots
        user_name = tracker.get_slot("name")
        user_email = tracker.get_slot("email")
        message = "Doctor didn't join"
        sendMail(message)

        # Email configuration
       

       
def sendMail(message):
     

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    # message = "user unable to book the appoointment"
    # sender_email = "my@gmail.com"
    password = app_password

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        stat = server.login(sender_email, password)
        print("login status",stat)
        server.sendmail(sender_email, receiver_email, message)
        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()





class ActionSessionStart(Action):
    def name(self):
        return "action_session_start"

    def run(self, dispatcher, tracker, domain):
        # Custom logic to set specific slots
        return [SlotSet("user_name", None), SlotSet("user_email", None)]

