# mysite/views.py
from django.http import HttpResponse
from django.views.static import serve



def favicon_view(request):
    
    return serve(request, 'favicon.ico', 'mysite/static/favicon.ico')
    

