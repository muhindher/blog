from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from post.models import Post
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PostForm
# Create your views here.


@login_required(login_url='login')
def index(request):
    post=Post.objects.order_by('-post_date')
    print(post)
    # category=Category.objects.all()[:5]
    context = {'blog_entry':post}
    return render(request,'post/index.html',context)

def home(request):
    post=Post.objects.order_by('-post_date')
    print(post)
    # category=Category.objects.all()[:5]
    context = {'blog_entry':post}
    return render(request,'post/home.html',context)

def AddPost(request):
    form=PostForm()
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context={'form':form}
    return render(request,'post/add_post.html',context)


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('Detail_post', args=[str(pk)]))

def Detailpost(request,pk):
    post=Post.objects.get(id=pk)
    total_likes = post.total_likes()
    print(total_likes)
    liked = bool
    if post.likes.filter(id=request.user.id).exists():
        liked = True
    context={'post':post}
    context["total_likes"] = total_likes
    context["liked"] = liked
    
    return render(request,'post/detail_post.html',context)


