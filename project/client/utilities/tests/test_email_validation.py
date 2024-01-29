# import pytest
from ..email_validation import EmailValidation


class TestEmailValidation:
    def test_valid_emails(self):
        valid_emails = [
            "test@example.com",
            "user123@gmail.com",
            "john.doe123@yahoo.co.uk",
            "first.last@subdomain.example.com"
        ]

        for email in valid_emails:
            result = EmailValidation.is_valid_email(email)
            assert result

    def test_invalid_emails(self):
        invalid_emails = [
            "invalidemail.com",
            "user@domain",
            "user@domain.",
            "user@.com",
            "@example.com",
            "user@example"
        ]

        for email in invalid_emails:
            result = EmailValidation.is_valid_email(email)
            assert not result
