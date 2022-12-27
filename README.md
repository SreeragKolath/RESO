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

## Usage:

**Train the chatbot**
- rasa train

**Run actions.py in another terminal and keep it running**
- rasa run actions

**Use the chatbot after training as**
- rasa shell

## Requirements

**Python 3.9.13** is used for this project and use a fresh virtual environment for installing all dependencies.

- **pip install -r requirements.txt**








