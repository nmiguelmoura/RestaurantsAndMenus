import re


class Validate_form_input:
    '''Class that performs validation of user input.'''

    def __init__(self):
        pass

    def validate_string(self, string, length):
        # Check if string length is under given value

        response = False
        error_message = ""

        if string:
            # Run if a string is passed.

            # Get string length.
            string_length = len(string)

            if 1 <= string_length <= length:
                # If string length is between 1 and maximum value passed,
                # response is True.
                response = True
            else:
                # If string length is 0 or greater than maximum value passed,
                # response continues False, and an error message is generated.
                error_message = u"The number of characters in the field must be " \
                                u"between 1 and %s." % length

        else:
            # If no string is passed, an error message is generated.
            error_message = u"Please insert valid data on field."

        return {
            "response": string if response else None,
            "error_message": error_message
        }

    def validate_course(self, course):
        # Validate course input.

        response = False
        error_message = u"Unexpected course selected! Please provide a valid " \
                        u"value."

        # List of available courses.
        course_list = ("Soap", "Salad", "Meat", "Fish", "Desert")

        # Loop through all courses in course_list
        for c in course_list:
            if c == course:
                # If course selected is on list of available courses,
                # erase error_message.
                response = course
                error_message = ""
                break

        return {
            "response": response,
            "error_message": error_message
        }

    def validate_price(self, price):
        # Check if price passed is a number.

        response = False
        error_message = ""
        if price:
            # If price exists, replace comma by point.
            price = price.replace(",", '.')

            # Regular expression to check if value is a digit with or without
            # point after units
            PRICE_RE = re.compile(r"^\d*\.?\d+$")
            result = PRICE_RE.match(price)

            if result:
                response = price
            else:
                error_message = u"Please insert only numeric characters and " \
                                u"decimal separator."
        else:
            error_message = u"Please insert a valid price for the menu."

        return {
            "response": response,
            "error_message": error_message
        }
