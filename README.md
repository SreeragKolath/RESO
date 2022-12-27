## RASA CHATBOT- RESORT BOOKING

A simple chatbot using **RASA framework(V.3)**. 

## About

This project is based on the **Resort booking** business use case. The chatbot collects all the informations from the consumer and store it in a database.

The chatbot responds to and handle the following basic functionalities

- Booking resort
- Handle FAQs
- Handle Greetings
- storing necessary information to database(**MySQL**)

## RASA File Configuration:

**__init__.py**:

An empty file that helps python find your actions

**data/rules.yml**:

In rules.yml file, 4 rules were created:

- To say goodbye anytime the user says goodbye.
- To say “I’m a bot” if bot_challenge intent is triggered.
- To activate the resort booking form when the resort_booking intent is triggered.
- Submit form, to confirm the details collected from the consumer.

















## Requirements

 is used for this project and use a fresh virtual environment for installing all dependencies.








