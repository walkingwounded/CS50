####Response Validation lab
from validator_collection import validators, checkers, errors


def main():
    print(validator(input("What's your email address? ")))


def validator(e):
    try:
        email_address = validators.email(e)
        if email_address == e:
            return("Valid")
        else:
            return("Invalid")
    except (errors.EmptyValueError, errors.InvalidEmailError):
        return("Invalid")




if __name__ == "__main__":
    main()