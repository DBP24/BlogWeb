from django.shortcuts import render,get_object_or_404
from .models import Post
from app.page.models import ProfessionalProfile
# http404
from django.http import Http404
# paginación
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
# envio de correo electronico
from .forms import EmailPostForm
from django.core.mail import send_mail
# Listar los Post
def get_post(request):
    # paginación
    posts_list = Post.published.all()
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
        'profile' : profile
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
    context = {
        'post': post,
        'profile' : profile
    }
    return render(request,'blog/details.html',context)

    # try:
    #         post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    # raise Http404("No Post found.")


# envio de correo electronico
def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
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
    else:
        form = EmailPostForm()
    return render(request, 'blog/share.html',
                   {
                       'post': post, 
                       'form': form,
                       'sent' : sent
                       })