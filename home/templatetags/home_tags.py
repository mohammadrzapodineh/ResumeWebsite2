from django import template

register = template.Library()


@register.simple_tag
def active_tag(request, view_name, *args):
    view_name = [view_name]
    for view in args:
        view_name.append(view)
    if request.resolver_match.view_name in view_name:
        return "active"