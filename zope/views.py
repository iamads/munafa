from django.shortcuts import render
from django.template.context import RequestContext
from zope.forms import UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def home(request):
    # Login Page
    context = RequestContext(request, {'request': request, 'user': request.user})
    return render(request, "zope/index.html", context_instance=context)


def register(request):
    # Registration view
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render(request, "zope/../templates/registration/register.html", {'user_form': user_form, 'registered': registered})


def login(request):
    # Login view
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your Account is disabled.")
        else:
            print "Invalid Login details provided: {0}, {1}".format(email, password)
            return HttpResponse("Invalid Login details supplied.")
    else:
        return render(request, "zope/../templates/registration/login.html", {})
