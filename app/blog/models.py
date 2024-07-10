from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Uso de URLs canonicas
from django.urls import reverse
# Adminsitrador de etiuqetas tags 
from taggit.managers import TaggableManager

# Gestor de modelo
class PublishedManager(models.Manager):
  # solo devuelve publicaciones por su estado 
   def get_queryset(self):
       return super().get_queryset().filter(status=Post.Status.PUBLISHED)
    

class Post(models.Model):

    # Opciones disponibles del estados (borrador y publicado)
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250, verbose_name="Titulo")
    slug = models.SlugField(max_length=250,unique_for_date='publish', verbose_name="Slug URL")
    # definimos el autor del Post (related_name : buscar en relación inversa)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts', default=1)
    body = models.TextField(name='body')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager
    
    #etiqueta
    tags = TaggableManager()
    
    # orden por defecto
    class Meta():
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]

    # return object default   
    def __str__(self):
        return self.title
    
    # uso de urls canonicas , url de busqueda en retorno
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[
                           self.publish.year,
                           self.publish.month,
                           self.publish.day,
                           self.slug
                           ])

class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'