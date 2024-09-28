from django.shortcuts import render
from recommender_system.models import Food
from django.db import connection
from django.shortcuts import get_object_or_404

# Create your views here.

def home_page(request):
    all_recipes = Food.objects.raw("""SELECT * FROM food;;""")
    if 'q' in request.GET:
        q = request.GET['q']
        top_recipes = Food.objects.filter(recipe_name__icontains=q)
    else:
        top_recipes = Food.objects.raw("SELECT * FROM food WHERE review_nums > 3500 ORDER BY review_nums DESC LIMIT 50;")
        
    return render(request, 'home.html', {'top_recipes':top_recipes, 'all_recipes':all_recipes})

def details_page(request, recipe_id):
    if 'q' in request.GET:
        q = request.GET['q']
        top_recipes = Food.objects.filter(recipe_name__icontains=q)
        all_recipes = Food.objects.raw("""SELECT * FROM food;;""")
        return render(request, 'home.html', {'top_recipes':top_recipes, 'all_recipes':all_recipes})

    else:
        recipe = Food.objects.raw(f'SELECT * FROM food WHERE recipe_id = {recipe_id};')
        similar = Food.objects.raw(f'''select *, (vectors <=> (select vectors from food where recipe_id ={recipe_id})) as cosine from food ORDER BY cosine LIMIT  5 offset 1;''')
        return render(request, 'details.html', {'recipe':recipe, 'similar':similar})
