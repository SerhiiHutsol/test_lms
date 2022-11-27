import datetime

from django.core.exceptions import ValidationError

AGE_LIMIT = 18


def adult_validator(birthday):
    age = datetime.date.today().year - birthday.year
    if age < AGE_LIMIT:
        raise ValidationError('Are should be greater that 18 y.o. ')


def phone_number_validator(phone_number):
    from .models import Student
    # res = Student.objects.filter(phone_number=phone_number)
    res = Student.objects.filter(phone_number=phone_number).exists()
    print(res)
    if res:
        raise ValidationError(f'Phone number {phone_number} is not unique ')


# class AdultValidator:

#     def __init__(self, age_limit):
#         self.age_limit = age_limit
        

#     def __call__(self, *args, **kwargs):
#         age = datetime.date.today().year - args[0].year
#         if age < self.age_limit:
#             raise ValidationError(f'Are should be greater that {self.age_limit} y.o. ')