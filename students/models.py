import datetime
from django.db import models
from faker import Faker
from django.core.validators import MinLengthValidator
from .validators import adult_validator
from dateutil.relativedelta import relativedelta

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=100,
                                  validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=100,
                                 validators=[MinLengthValidator(2)])
    age = models.PositiveIntegerField()
    birthday = models.DateField(default=datetime.date.today,
                                validators=[adult_validator])

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.age}'

    def save(self, *args, **kwargs):
        self.age = relativedelta(datetime.date.today(), self.birthday).years
        super().save(*args, **kwargs)

    @staticmethod
    def gen_students(cnt=10):
        fk = Faker()
        for _ in range(cnt):
            st = Student(first_name=fk.first_name(),
                         last_name=fk.last_name(),
                         age=fk.random_int(min=18, max=60),
                         birthday=fk.date_between(start_date='-65y',
                                                  end_date='-15y'))
            st.save()
