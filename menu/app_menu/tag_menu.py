from django import template
from .models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name, current_url):
    menu_items = MenuItem.objects.filter(menu_name=menu_name)
    menu_dict = {}

    for item in menu_items:
        if not item.parent:
            menu_dict[item] = []

    for item in menu_items:
        if item.parent:
            menu_dict[item.parent].append(item)

    def render_menu_items(menu_dict, parent=None):
        result = ""
        for item in menu_dict.get(parent, []):
            result += f'<li><a href="{item.url or item.named_url}">{item.title}</a>'
            if item in menu_dict:
                result += "<ul>"
                result += render_menu_items(menu_dict, item)
                result += "</ul>"
            result += "</li>"
        return result

    menu_html = render_menu_items(menu_dict)
    return menu_html