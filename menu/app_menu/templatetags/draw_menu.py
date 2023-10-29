from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.db import connection

from app_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('app_menu/menu.html')
def draw_menu(menu_name, current_url):
    current_url = current_url.split('/')
    current_url = current_url[1:-1]

    nesting_level = len(current_url)
    select_related_argument = 'parent'
    if nesting_level >= 2:
        select_related_argument = '__'.join(
            ['parent' for _ in range(nesting_level)]
        )

    menu_items = (
        MenuItem.objects
        .filter(menu_name=menu_name)
        .select_related(select_related_argument)
    )

    if len(current_url) < 1:
        current_url = 'main'
    else:
        current_url = current_url[-1]

    menu_dict = {}
    current_item = None
    for item in menu_items:
        menu_dict[item] = []
        if not item.parent:
            top_item = item
        if item.named_url == current_url:
            current_item = item

    if not current_item:
        current_item = top_item

    top_item_url = reverse(top_item.named_url)
    result = f'<ul><li><a href="{top_item_url}">{top_item.title}</a></li></ul>'

    for item in menu_items:
        if item.parent:
            menu_dict[item.parent].append(item)

    def render_menu_items(menu_dict, current):

        menu_html = '<p>======================</p>'
        if menu_dict[current]:
            menu_html += '<ul>'
            for child in menu_dict[current]:
                url = reverse(child.named_url)
                menu_html += f'<li><a href="{url}">{child.title}</a></li>'
            menu_html += '</ul>'
        if current.parent:
            menu_html = render_menu_items(menu_dict, current.parent) + menu_html
        return menu_html

    result += render_menu_items(menu_dict, current_item)

    result = mark_safe(result)

    # Only one query to DB for each menu
    queries = connection.queries
    print(len(queries))
    for query in queries:
        print(query)
    return {'menu': result}
