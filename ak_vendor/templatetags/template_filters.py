from django import template

register = template.Library()


@register.filter
def format_status(value):
    """Replace underscores with spaces in status strings."""
    if value:
        return value.replace("_", " ")
    return value
