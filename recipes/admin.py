'''
    Docstring
'''

from django.contrib import admin

from recipes.models import (Recipe, Ingredient, Tag, Follow,
                         Favorite, ShopList, IngredientAmount)


class RecipeAdmin(admin.ModelAdmin):
    '''
        Docstring
    '''
    list_display = ('title', 'author')
    list_filter = ('title',)


class TagAdmin(admin.ModelAdmin):
    '''
        Docstring
    '''
    list_display = ('title', 'value')


class IngredientAdmin(admin.ModelAdmin):
    '''
        Docstring
    '''
    list_display = ('title', 'dimension')
    list_filter = ('title',)


class FollowAdmin(admin.ModelAdmin):
    '''
        Docstring
    '''
    list_display = ('author', 'user')


class FavoriteAdmin(admin.ModelAdmin):
    '''
        Docstring
    '''
    list_display = ('user', 'recipe')


class ShopListAdmin(admin.ModelAdmin):
    '''
        Docstring
    '''
    list_display = ('user', 'recipe')


class IngredientAmountAdmin(admin.ModelAdmin):
    '''
        Docstring
    '''
    list_display = ('recipe', 'ingredient')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShopList, ShopListAdmin)
admin.site.register(IngredientAmount, IngredientAmountAdmin)
