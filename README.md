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
- rasa train

**Run actions.py in another terminal and keep it running**
- rasa run actions

**Use the chatbot after training as**
- rasa shell

## Use Cases:

**Book Resort**

User: I want to book the resort.

Bot: Please provide your Complete Name:

User: Rahul S

Bot: Please provide your Valid Email Address:

User: rahulnair@gmail.com

Bot: Please provide your Valid Phone Number:

User: 9567342361

Bot: What kind of Residence Facility Are you looking for?\n
-   ? Our Tariff Plans: : You selected: (Use arrow keys)                                                                                                               
-  » 1: LUXURY COTTAGE ROOMS WITH MOUNTAIN VIEW (LUXURY COTTAGE ROOMS WITH MOUNTAIN VIEW)
-    2: SUITE COTTAGE ROOMS WITH NATURE VIEW (SUITE COTTAGE ROOMS WITH NATURE VIEW)
-   3: TREE TOP STUDIO COTTAGE (TREE TOP STUDIO COTTAGE)
-   4: TREE TOP DUPLEX COTTAGE (TREE TOP DUPLEX COTTAGE)
-  5: MUD STUDIO COTTAGE (MUD STUDIO COTTAGE)
-  6: MUD DUPLEX COTTAGE (MUD DUPLEX COTTAGE)
-  Type out your own message...
 
User: (Clicks on Button 1)
(Clicking on buttons is handled similarly)
 
Bot: Please pick any compliment Activities with Reso?
? Our activities: : You selected: (Use arrow keys)                                                                                                                      » 1: Forest Edge walking to the View Point (Forest Edge walking to the View Point)
   2: Meditation in the lap of Mother Nature (Meditation in the lap of Mother Nature)
   3: Night Trekking-The Program to see stars on the Land (Night Trekking-The Program to see stars on the Land)
   4: Sun Rise & Bison Sighting (Sun Rise & Bison Sighting)
   5: Come Back to Your Roots (Come Back to Your Roots)
   6: A Truly Wild Welcome (A Truly Wild Welcome)
   Type out your own message...
   
User: (Clicks on Button 1)
(Clicking on buttons is handled similarly)

Bot: How many adults (10 or above years old) will be staying ?
? Number of Adults: : You selected: (Use arrow keys)                                                                                                                    » 1: 1 - 2 (1 - 2)
   2: 3 - 4 (3 - 4)
   3: 5 people or more (5 people or more)
   Type out your own message...
User: (Clicks on Button 1)
(Clicking on buttons is handled similarly)

Bot: How many children (below 10 years old) will be staying?
? Number of Children: : You selected: (Use arrow keys)                                                                                                                  » 1: 0 (0)
   2: 1 - 2 (1 - 2)
   3: 3 - 4 (3 - 4)
   Type out your own message...
User: (Clicks on Button 1)
(Clicking on buttons is handled similarly)

Bot: When you like to have check-in ? Eg: 12/12/2022

User: 20/12/2022

Bot: When would you like to checkout ? Eg: 14/12/2022

User: 21/12/2022

Bot: We have received your booking Request
     Full name of the registrant: Rahul S
     Email address: rahulnair@gmail.com
     Phone number: 9567342361
     Number of adults staying: 1 - 2
     Number of children staying: 0
     Room type: LUXURY COTTAGE ROOMS WITH MOUNTAIN VIEW
     Compliment Activitiy:Forest Edge walking to the View Point
     Check-in date: 20/12/2022
     Check-out date: 21/12/2022
     front desk staff will connect you within 10 minutes .
     Thank you!
     
**The details will be updated in the database**


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








