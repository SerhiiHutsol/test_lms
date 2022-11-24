import datetime

from django.core.exceptions import ValidationError

AGE_LIMIT = 18


def adult_validator(birthday):
    age = datetime.date.today().year - birthday.year
    if age < AGE_LIMIT:
        raise ValidationError('Are should be greater that 18 y.o. ')
