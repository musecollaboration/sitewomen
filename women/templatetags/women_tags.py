from django import template
from women.models import Category, TegPost
import women.views as views


register = template.Library()


@register.inclusion_tag('women/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {
        "cats": cats,
        "cat_selected": cat_selected,
    }


@register.inclusion_tag('women/list_tags.html')
def show_all_tags():
    return {"tags": TegPost.objects.all()}
