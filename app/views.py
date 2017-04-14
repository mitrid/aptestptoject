from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.views.generic import View
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def index(request):
    #QuerySets 
    posts = Post.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'index.html', {'posts': posts})
    
def profile(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'profile.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('/')
#открываю пост в отдельной странице
def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'post_detail.html', {'post': post})
