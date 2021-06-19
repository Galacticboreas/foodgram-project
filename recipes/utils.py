RECIPES_TAGS = ['breakfast', 'lunch', 'dinner']

PAGINATION_PAGES_FOR_ALL = 6
PAGINATION_PAGES_FOR_MY_SUBSCRIPTIONS = 3


def get_ingredients(request):
    ingredients = {}
    for key in request.POST:
        if key.startswith('nameIngredient'):
            ingr = key.split('_')[1]
            ingredients[request.POST[key]] = request.POST[
                'valueIngredient_' + ingr]
    print(f'ingredients: {ingredients}')
    return ingredients
