import re

class Validate_Form_Input:
    def __init__(self):
        pass

    def validate_string(self, string, length):
        response = False
        error_message = ""

        if string:
            string_length = len(string)

            if 1 <= string_length <= length:
                response = True
            else:
                error_message = u"The number of characters in the field must be between 1 and %s." % length

        else:
            error_message = u"Please insert valid data on field."

        return {
            "response": string if response else None,
            "error_message": error_message
        }

    def validate_course(self, course):
        response = False
        error_message = u"Unexpected course selected! Please provide a valid value."
        course_list = ("Soap", "Salad", "Meat", "Fish", "Desert")

        for c in course_list:
            if c == course:

                response = course
                error_message = ""
                break

        return {
            "response": response,
            "error_message": error_message
        }

    def validate_price(self, price):
        response = False
        error_message = ""
        if price:
            price = price.replace(",", '.')

            PRICE_RE = re.compile(r"^\d*\.?\d+$")
            result = PRICE_RE.match(price)

            if result:
                response = price
            else:
                error_message = u"Please insert only numeric characters and decimal separator."
        else:
            error_message = u"Please insert a valid price for the menu."

        return {
            "response": response,
            "error_message": error_message
        }
