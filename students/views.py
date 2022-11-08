from django.shortcuts import render
from django.http import HttpResponse

from .models import Student
from .utils import qs2html

from webargs.fields import Str, Int
from webargs import fields
from webargs.djangoparser import use_args

# Create your views here.


