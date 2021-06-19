'''
    Docstring
'''

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    '''
        Docstring
    '''
    title = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    style = models.CharField(max_length=30)

    class Meta:
        '''
        Docstring
        '''
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class Ingredient(models.Model):
    '''
        Docstring
    '''
    title = models.CharField(max_length=100, db_index=True)
    dimension = models.CharField(max_length=10)

    class Meta:
        '''
            Docstring
        '''
        verbose_name = 'ingredient'
        verbose_name_plural = 'ingredients'


class Recipe(models.Model):
    '''
        Docstring
    '''
    title = models.CharField(max_length=200, null=True)
    text = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='recipes')
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    cooking_time = models.PositiveIntegerField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='recipes')
    ingredients = models.ManyToManyField(
        Ingredient, through='IngredientAmount',
        through_fields=('recipe', 'ingredient'))

    class Meta:
        '''
            Docstring
        '''
        ordering = ['-pub_date']
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'

    def __str__(self):
        return self.title


class Follow(models.Model):
    '''
        Docstring
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='following')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='follower')

    class Meta:
        '''
            Docstring
        '''
        verbose_name = 'follow'
        verbose_name_plural = 'follows'


class Favorite(models.Model):
    '''
        Docstring
    '''
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='favorite_recipes', )
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='favorites')

    class Meta:
        '''
            Docstring
        '''
        verbose_name = 'favorite'
        verbose_name_plural = 'favorites'

    def __str__(self):
        return self.recipe.title


class ShopList(models.Model):
    '''
        Docstring
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='shop_list')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='shop_list')

    class Meta:
        '''
            Docstring
        '''
        verbose_name = 'shopping list'
        verbose_name_plural = 'shopping lists'

    def __str__(self):
        return self.recipe.title


class IngredientAmount(models.Model):
    '''
        Docstring
    '''
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='recipe_amounts')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,
                                   related_name='ingredients')
    quantity = models.PositiveIntegerField()

    class Meta:
        '''
            Docstring
        '''
        verbose_name = 'ingredient quantity'
        verbose_name_plural = 'ingredient amounts'

    def __str__(self):
        return self.ingredient.title
