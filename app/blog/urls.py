from django.urls import path
from . import views


app_name = 'blog'


urlpatterns = [
    path('', views.get_post, name='get_post'),
    path('tag/<slug:tag_slug>/',views.get_post, name='post_list_by_tag'),
   # path('<int:id>/', views.post_detail, name='post_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/',views.post_share, name='post_share'),
    path('<int:post_id>/comment/',views.post_comment, name='post_comment'),


]