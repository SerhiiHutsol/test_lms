from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from .utils import qs2html

from webargs.fields import Str, Int
from webargs import fields
from webargs.djangoparser import use_args

from .forms import StudentCreateForms

# Create your views here.


def index(request):
    return HttpResponse('LMS System!')


@use_args(
    {
        'first_name': Str(required=False),  # ,missing=None)
        'last_name': Str(required=False),
        'age': Int(required=False)
    },
    location='query')
def get_students(request, args):
    st = Student.objects.all()
    for key, value in args.items():
        st = st.filter(**{key: value})

    html_form = '''
    <form method='get'>
        <label for="fname">First name:</label><br>
        <input type="text" id="fname" name="first_name" placeholder="Bob"><br>
        <label for="fname">Last name:</label><br>
        <input type="text" id="lname" name="last_name" placeholder="Dilan"><br>
        <label for="lname">Age:</label><br>
        <input type="number" id="age_id" name="age" placeholder="33"><br><br>
        <input type="submit" value="Submit">
    </form> 
'''

    http = qs2html(st)
    response = html_form + http

    return HttpResponse(response)


@csrf_exempt
def create_students(request):
    if request.method == 'GET':
        form = StudentCreateForms()
    else:
        form = StudentCreateForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/st/')
    html_form = f'''
        <form method='post'>
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Submit">
        </form> 
    '''

    return HttpResponse(html_form)