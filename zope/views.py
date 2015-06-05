from django.shortcuts import render
from django.template.context import RequestContext
# Create your views here.

def home(request):
    # Login Page
    context = RequestContext(request, {'request': request, 'user': request.user})
    return render(request, "zope/index.html", context_instance=context)


def register(request):
    # Registration view
    return render(request, "zope/register.html", )
