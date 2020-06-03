from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/dashboard.html')

@login_required(login_url='login')
def allPosts(request):
    all_posts = Post.objects.all()
    context = {'post': all_posts}
    return render(request, 'accounts/allPosts.html', context)

    
@login_required(login_url='login')
def userPage(request):
    my_post = Post.objects.filter(user = request.user).order_by('date_created')
    return render(request, 'accounts/user.html', {'post': my_post})

@login_required(login_url='login')
def deletePost(request, pk):
    curr_post = Post.objects.get(id = pk)
    context = {'Post': curr_post}
    if request.method == 'POST':
        curr_post.delete()
        return redirect('/')
    return render(request, 'accounts/deletePost.html', context)
        
@login_required(login_url='login')
def createPost(request):
    form = ResultsForm()
    context = {'form': form}  
    if request.method == "POST":
        form = ResultsForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user = request.user
            instance.save()
    return render(request, 'accounts/createPost.html', context)

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for: " + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)
    
@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else: 
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def like_post(request):
    user = request.user
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id = post_id)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, post_id = post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
        next = request.META.get('HTTP_REFERER')
        return HttpResponseRedirect(next)

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('allPosts')
    else:
        form = CommentForm()
    return render(request, 'accounts/add_comment_to_post.html', {'form': form})


