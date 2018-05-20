from django.http import HttpResponse
from .models import Recipe

def index(request):
    all_recipes = Recipe.objects.all()
    html = ''
    for recipe in all_recipes:
        url = '/recipe/' + str(recipe.id) + '/'
        html += '<a href="' + url + '">' + recipe.food_title + '</a><br>'
    return HttpResponse(html)

def detail(request,recipe):
    return HttpResponse("<h2>Details for :" + str(recipe) + "</h2>")