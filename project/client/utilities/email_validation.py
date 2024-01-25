import re


class EmailValidation:
    @staticmethod
    def is_valid_email(email):
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', re.VERBOSE)
        return bool(email_regex.match(email))
