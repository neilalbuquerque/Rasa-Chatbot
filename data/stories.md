## happy path
* greet
  - utter_greet
  -action_festival_wish
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## medicare search
* greet
    - utter_greet
* search_provider{"facility_type":"hospital", "location":"Borivali"}
    - action_facility_search
    - slot{"address":"L I C Colony, Borivali West"}
* goodbye
    - utter_goodbye
 
## search hospital + location
* greet
    - utter_greet
* search_provider{"facility_type":"hospital"}
    - utter_ask_location
* inform{"location":"Borivali"}
    - action_facility_search
    - slot{"address":"L I C Colony, Borivali West"}
    - slot{"link":"www.google.com"}
* thanks
    - utter_goodbye
    
## tell me a joke
* greet
    - utter_greet
* ask_joke
    - utter_joke
* thanks
    - utter_goodbye
    
## tell me a joke + laugh
* greet
    - utter_greet
* mood_great
  - utter_happy
* ask_joke
    - utter_joke
* laugh_at_joke
    -utter_laugh_response
* goodbye
    - utter_goodbye

## greet_wish
* greet_wish
    -utter_greet_wish
* goodbye
    - utter_goodbye
    
## initialize
* hello
    -utter_hi
## festival wish
* festive
    - utter_festival
    - action_festival_wish
    