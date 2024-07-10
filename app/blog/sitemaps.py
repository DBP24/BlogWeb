from django.contrib.sitemaps import Sitemap
from .models import Post

# class PostSitemap(Sitemap):
#     changefreq = 'weekly'
#     priority = 0.9

# def items(self):
#     # return Post.published.all()
#     return Post.objects.all()[:5]
# def lastmod(self, obj):
#     return obj.updated

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return Post.objects.all()  # Devuelve los primeros 5 posts, sin filtrar

    def location(self, obj):
        return obj.get_absolute_url()
    
    def lastmod(self, obj):
        return obj.update