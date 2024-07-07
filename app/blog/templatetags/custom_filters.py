from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def format_titles_in_content(value):
    pass