recipes_tags = ['breakfast', 'lunch', 'dinner']

pagination_pages_for_all = 6
pagination_pages_for_my_subscriptions = 3


def get_ingredients(request):
    ingredients = {}
    for key in request.POST:
        if key.startswith('nameIngredient'):
            ingr = key.split('_')[1]
            ingredients[request.POST[key]] = request.POST[
                'valueIngredient_' + ingr]
    return ingredients
