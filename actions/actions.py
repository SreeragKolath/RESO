# Import Libraries
from typing import Any, Text, Dict, List
import re
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import mysql.connector

# Function to connect to database and inserting the records into Database
def data_update(name, email, phone_number, tariff_type, adults, children, check_in, check_out):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="resortbooking"  # Database
    )
    cursor = mydb.cursor()
    sql = 'INSERT INTO bookings1 (Name, Email, PhoneNumber,RoomType, Adults, Childrens, Checkin, Checkout) VALUES ("{' \
          '0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}");'.format(name, email, phone_number, tariff_type, adults,
                                                                   children, check_in, check_out)
    cursor.execute(sql)
    mydb.commit()
    print(cursor.rowcount, "Record inserted successfully")

# Class for validating form values

class ValidateBookForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_book_form"
    """Validate `name` value."""
    def validate_name(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `name` value."""
        print(slot_value)
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"name": None}
        else:
            return {"name": slot_value}

    """Validate `email` value."""
    def validate_email(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, slot_value):
            return {"email": slot_value}
        else:
            dispatcher.utter_message(text=f"email-id is invalid Please provide correct email-id.")
            return {"email": None}

    """Validate `phone number` value."""
    def validate_phone_number(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        regex = r'\b[7-9]{1}[0-9]{9}\b'
        if re.fullmatch(regex, slot_value):
            return {"phone_number": slot_value}
        else:
            dispatcher.utter_message(text=f"Phone Number is invalid Please provide correct Phone Number.")
            return {"phone_number": None}

    """Validate `check_in` value."""
    def validate_check_in(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        if re.search(r"\d{2}/\d{2}/\d{4}", slot_value):
            return {"check_in": slot_value}
        else:
            dispatcher.utter_message(text=f"The entered date isn't valid one")
            return {"check_in": None}

    """Validate `check_out` value."""
    def validate_check_out(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        if re.search(r"\d{2}/\d{2}/\d{4}", slot_value):
            return {"check_out": slot_value}
        else:
            dispatcher.utter_message(text=f"The entered date isn't valid one")
            return {"check_out": None}


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        email = tracker.get_slot("email")
        phone_number = tracker.get_slot("phone_number")
        tariff_type = tracker.get_slot("tariff_type")
        package_type = tracker.get_slot("addition_act")
        adults = tracker.get_slot("adults")
        children = tracker.get_slot("children")
        check_in = tracker.get_slot("check_in")
        check_out = tracker.get_slot("check_out")
        dispatcher.utter_message(
            text=f"We have received your booking Request\n Full name of the registrant: {name}\n Email address: {email}\n Phone number: {phone_number}\n Number of adults staying: {adults}\n Number of children staying: {children}\n Room type: {tariff_type}\n Compliment Activitiy:{package_type}\n Check-in date: {check_in}\n Check-out date: {check_out}\n front desk staff will connect you within 10 minutes . \n Thank you!")
        data_update(name, email, phone_number, tariff_type, adults, children, check_in, check_out)

        return []
