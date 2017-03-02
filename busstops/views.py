from django.shortcuts import render
from private.secrets import GOOGLE_API_KEY, TRIMET_APP_ID

# Create your views here.

def home(request):

    context = {'google_key': GOOGLE_API_KEY, 'trimet_key': TRIMET_APP_ID}

    return render(request, 'home.html', context)