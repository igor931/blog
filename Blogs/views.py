from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User
##
if User.username != User.objects:
   username = "<a href='url 'register'>Зарегистрируйтесь</a>"
else:
   username = User.username
##
from .forms import PostForm, CommentForm
# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'Blogs/index.html', {'posts': posts, 'user': username})

def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		comment = CommentForm(request.POST)
		if comment.is_valid():
			comment.post = post
			comment.save()
	else:
		form = CommentForm()
	return render(request, 'Blogs/post.html', {'post': post,
											   'form': form,
											   'user': username})

def comment_add(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request, 'Blogs/post.html', {'form': form})

def new_post(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'Blogs/post_edit.html', {'form': form, 'user': username})

def about(request):
    users = User.objects.all()
    post_obj = Post.objects.all()
    return render(request, 'Blogs/about.html', locals())
