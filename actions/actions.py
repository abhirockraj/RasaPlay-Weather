from typing import Any, Text, Dict, List
import random
import requests
 
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
 
# computer_choice & determine_winner functions refactored from
# https://github.com/thedanelias/rock-paper-scissors-python/blob/master/rockpaperscissors.py, MIT liscence
 
class ActionPlayRPS(Action):
   
    def name(self) -> Text:
        return "action_play_rps"
 
    def computer_choice(self):
        generatednum = random.randint(1,3)
        if generatednum == 1:
            computerchoice = "rock"
        elif generatednum == 2:
            computerchoice = "paper"
        elif generatednum == 3:
            computerchoice = "scissors"
       
        return(computerchoice)
 
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
 
        # play rock paper scissors
        user_choice = tracker.get_slot("choice")
        dispatcher.utter_message(text=f"You chose {user_choice}")
        comp_choice = self.computer_choice()
        dispatcher.utter_message(text=f"The computer chose {comp_choice}")
 
        if user_choice == "rock" and comp_choice == "scissors":
            dispatcher.utter_message(text="Congrats, you won!")
        elif user_choice == "rock" and comp_choice == "paper":
            dispatcher.utter_message(text="The computer won this round.")
        elif user_choice == "paper" and comp_choice == "rock":
            dispatcher.utter_message(text="Congrats, you won!")
        elif user_choice == "paper" and comp_choice == "scissors":
            dispatcher.utter_message(text="The computer won this round.")
        elif user_choice == "scissors" and comp_choice == "paper":
            dispatcher.utter_message(text="Congrats, you won!")
        elif user_choice == "scissors" and comp_choice == "rock":
            dispatcher.utter_message(text="The computer won this round.")
        else:
            dispatcher.utter_message(text="It was a tie!")
 
        return []

class ActionWetherInfo(Action):
    def name(self) -> Text:
        return "action_wether_info"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_city = tracker.get_slot("city")  
        urlLoc = "https://foreca-weather.p.rapidapi.com/location/search/"+user_city  # type: ignore
       
        querystring = {"lang":"en","country":"in"}

        headersLoc = {
            "X-RapidAPI-Key": "48290658dfmsh63b6d043595c405p115375jsncfe5ed7a09e9",
            "X-RapidAPI-Host": "foreca-weather.p.rapidapi.com"
        }

        responseLoc = requests.request("GET", urlLoc, headers=headersLoc, params=querystring)

        url = "https://foreca-weather.p.rapidapi.com/current/"+str(responseLoc.json()['locations'][0]['id'])

        querystring = {"alt":"0","tempunit":"C","windunit":"MS","tz":"Europe/London","lang":"en"}

        headers = {
            "X-RapidAPI-Key": "48290658dfmsh63b6d043595c405p115375jsncfe5ed7a09e9",
            "X-RapidAPI-Host": "foreca-weather.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        temp = response.json()['current']['temperature']
        # dispatcher.utter_message(text="Temperature of "+user_city)
        dispatcher.utter_message(text="Temperature of "+user_city+" is "+str(temp))
        return []