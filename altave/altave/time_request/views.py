from django.http import HttpResponse
import datetime

# Create your views here.

def home(request):
    now = datetime.datetime.now()
    return HttpResponse(f'Its time Request {now}')
