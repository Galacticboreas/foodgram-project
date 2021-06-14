recipes_tags = ['breakfast', 'lunch', 'dinner']

pagination_pages = 6


def get_ingredients(request):
    ingredients = {}
    for key in request.POST:
        if key.startswith('nameIngredient'):
            ingr = key.split('_')[1]
            ingredients[request.POST[key]] = request.POST[
                'valueIngredient_' + ingr]
    return ingredients
