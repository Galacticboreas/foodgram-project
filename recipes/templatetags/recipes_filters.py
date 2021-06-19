from django import template

from itertools import groupby

from recipes.views import RECIPES_TAGS, new_recipe

register = template.Library()


@register.filter(name='make_tags')
def make_tags(request, tag):
    new_request = request.GET.copy()
    if not request.GET.getlist('tags'):
        tags_list = list(RECIPES_TAGS)
    else:
        tags_list = new_request.getlist('tags')
    tags_list = [el for el, _ in groupby(tags_list)]
    if tag.value in tags_list:
        tags_list.remove(tag.value)
        new_request.setlist('tags', tags_list)
    else:
        new_request.appendlist('tags', tag.value)
    return new_request.urlencode()


@register.filter(name='is_follower')
def is_follower(request, profile):
    return request.user.follower.filter(author=profile)


@register.filter(name='is_favorite')
def is_favorite(request, recipe):
    return request.user.favorites.filter(recipe=recipe).exists()


@register.filter(name='is_in_purchases')
def is_in_purchases(request, recipe):
    return request.user.shop_list.filter(recipe=recipe).exists()


@register.filter(name='purchases_count')
def purchases_count(request):
    return request.user.shop_list.count()
