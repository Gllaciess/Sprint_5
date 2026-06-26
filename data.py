from helpers.helpers import generate_name, generate_email, generate_password

class TestData:

    VALID_NAME = generate_name()
    VALID_EMAIL = generate_email()
    VALID_PASSWORD = generate_password()

    INVALID_PASSWORD = "12345"

