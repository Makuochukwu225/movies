from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
data = {
    'movies':
    [
        {
            'id': 1,
            'title': "Legend of seeker ",
            'year': 1669
        },
        {
            'id': 2,
            'title': "Harry potter",
            'year': 1669
        }, {
            'id': 3,
            'title': "Dawn of justice",
            'year': 1669
        }, {
            'id': 4,
            'title': "Hello world",
            'year': 1669
        },
    ]

}


def movies(request):
    return render(request, 'movies/movies.html', data)


def home(request):
    return HttpResponse("Home page")
