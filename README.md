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

**data/stories.yml**:

- This is required for Rasa Core.
- It is used to provide the conversational flow to our bot.

**domain.yml**:
The Domain file is a directory of everything the assistant knows:

- **Responses**: These are the things the assistant can say to users.
- **Intents**: lists all intents used in your NLU data and conversation training data.
- **Slots**: act as a key-value store which can be used to store information the user provided as well as information gathered about the outside world.
- **Entities**: The entities section lists all entities that can be extracted by any entity extractor in your NLU pipeline.
- **Forms and Actions**: These add application logic and extend what our assistant can do.


**config.yml**:
configuration of your NLU and Core models.

**endpoints.yml**:
This file contains the different endpoints our bot can use.

**actions.py**:
- added customized actions for the bot, the details collected from the consumer is stored as dataframe, created a function **data_update** which connects with MySQL and saves it in the database.
- Secondly, created a class **ValidateBookForm** in this class, we're validating the slots one by one using Python.
- Finally, **ActionSubmit** class is made which inherits the Action from rasa sdk, here, we call the data update function to store the information collected using the slots, and a message for the user is uttered.
- Used **Regular Expressions** to validate each slots correctly.

## Requirements

**Python 3.9.13** is used for this project and use a fresh virtual environment for installing all dependencies.

- **pip install -r requirements.txt**

## Usage:

**Train the chatbot**
- 

**Run actions.py in another terminal and keep it running**
- rasa run actions

**Use the chatbot after training as**
- rasa shell

## Use Cases:

**FAQS**:

- **Check-in timings**

     User: What are your check-in timings?

     Bot: You can check-in between 10 AM - 11 AM. please contact our desk staff for early/late check-in

- **Check-out timings**

     User:  What are your check-out timings?

     Bot: You can check-out between 12 PM - 1 PM. please contact our desk staff for late check-out

- **cancel-bookings**

     User:  how do i cancel my bookings?

     Bot: For cancellation, please contact our desk support at +91 3456789769!

- **parking**

     User:  Does the resort provide parking?

     Bot: Yes, we do provide free parking for all our resort guests and visitors with 24*7 security Surveillance!
  
- **luggage**

     User:  Where i keep my luggage?

     Bot: Resort guests and visitors can store their luggage at the front desk security room. luggage can be held at the resort before or after your stay for up to 12           hours.
  
- **pool**

     User:  Does the resort have pool?

     Bot: Yes, Luxury pool measuring 12m long by 5m wide with elephant spouting water from their trunks. pool timings from 10 AM to 7 PM.








