# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import random

class ActionFacilitySearch(Action):

    def name(self) -> Text:
        return "action_facility_search"

# Function to return address of the facility
def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        facility = tracker.get_slot("facility_type")
        address = "Karuna Hospital, LIC Colony Road, Jeevan Bima Nagar, near Bhagwati Hospital, Borivali West, " \
                  "Mumbai, Maharashtra 400103 "
        link = "https://www.practo.com/mumbai/hospital/karuna-hospital-borivali-west-1/doctors"
        dispatcher.utter_message("Here is the address of the {}:\n{} \n Link: {}".format(facility, address, link))

        return [SlotSet("address", address), SlotSet("link", link)]

# Function to return a greeting message
class ActionFestival(Action):

    def name(self) -> Text:
        return "action_festival_wish"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        currentMonth = datetime.now().month
        festival = {1: 'New Year', 2: 'Valentines Day', 3: 'Holi', 4: 'Easter', 5:'Buddha Purnima', 6:'Ganga Dussehra', 7:'Bakri Eid', 8:'Indian Independence Day', 9:'Ganesh Chaturthi',
                    10:'Dussehra', 11:'Diwali', 12:'Christmas'}

        search = festival[currentMonth] + "wishes"
        params = {"q": search}
        r = requests.get("https://www.bing.com/images/search", params=params)

        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.findAll("a", {"class": "thumb"})
        s=random.choice(results)
        k = s.attrs["href"]
        print(k)
        # for item in results:
        #     #img_obj = requests.get(item.attrs["href"])
        #     print("Link", item.attrs["href"])
        #dispatcher.utter_image_url(k)
        dispatcher.utter_message("Wishing you and your family a happy {}".format(festival[currentMonth]))
        #dispatcher.utter_message(attachment=k)
        dispatcher.utter_message(image= k)
        return []
