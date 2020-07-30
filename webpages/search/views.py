from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
search_query = ""

def home(request):
    # template = loader.get_template('templates/search/home.html')
    # return HttpResponse("Hello")
    search_query = request.GET.get('search_query')
    return render(request,'search.html')