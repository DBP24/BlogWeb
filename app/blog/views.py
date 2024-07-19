from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from app.page.models import ProfessionalProfile
from django.shortcuts import redirect
# http404
from django.http import Http404
# paginación
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
# envio de correo electronico y comentario
from django.views.decorators.http import require_POST
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
# urls reverse
from django.urls import reverse

# etiquetas
from taggit.models import Tag
# caracteres
from unidecode import unidecode
# orm django
'''
 • Avg: The mean value
 • Max: The maximum value
 • Min: The minimum value
 • Count: The total number of objects
'''
from django.db.models import Count
# BUSQUEDA
from .forms import EmailPostForm, CommentForm, SearchForm 
from django.db.models import Q



# Listar los Post
def get_post(request,tag_slug=None):

    #etiquetas
    posts_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts_list = posts_list.filter(tags__in=[tag])
    # busqueda
    form = SearchForm()
    query = None
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            posts_list = posts_list.filter(Q(title__icontains=query)|Q(body__icontains=query))
            # posts_list = posts_list.filter(title__icontains=query)
    # paginación
    paginator = Paginator(posts_list, 3)
    page_number = request.GET.get('page', 1)

    profile = ProfessionalProfile.objects.get()
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    context = {
        'posts' : posts,
        'profile' : profile,
        'tag' : tag,
        'form' : form,
        'query' : query
    }
    return render(request,'blog/list.html',context)

# Listar detalle de post

def post_detail(request, year, month, day, post):
 
    post = get_object_or_404(Post,status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    profile = ProfessionalProfile.objects.get()
    # Comentarios
    comments = post.comments.filter(active=True)
    form = CommentForm()
    
    # Listamos los post similares
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                 .order_by('-same_tags','-publish')[:4]
    context = {
        'post': post,
        'profile' : profile,
        'comments' :comments,
        'form' : form,
        'similar_posts': similar_posts
    }
    return render(request,'blog/details.html',context)


# envio de correo electronico
def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    profile = ProfessionalProfile.objects.get()
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f"{cd['name']} recommends you read " \
                    f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                    f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'diegobonattipajuelo1@gmail.com',
                    [cd['to']])
            sent = True

            # Rediret a ListPost
            # return redirect('blog:get_post')
    else:
        form = EmailPostForm()
    return render(request, 'blog/share.html',
                   {
                       'post': post, 
                       'form': form,
                       'sent' : sent,
                       'profile' :profile
                       })


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    # A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
       # Create a Comment object without saving it to the database
       comment = form.save(commit=False)
       # Assign the post to the comment
       comment.post = post
       # Save the comment to the database
       comment.save()
    return redirect(post.get_absolute_url()) 
#    return render(request, 'blog/comment.html',
#                           {'post': post,
#                            'form': form,
#                            'comment': comment})

# shears
from django.contrib.postgres.search import SearchVector


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.filter(title__icontains=query)
    return render(request,
                  'blog/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})