from django import template
from django.utils.safestring import mark_safe
import markdown
import re
from ..models import Post

register = template.Library()

@register.filter
def format_titles_in_content(value):
    pass

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

@register.filter(name='markdown')
def markdown_format(text):
 return mark_safe(markdown.markdown(text))