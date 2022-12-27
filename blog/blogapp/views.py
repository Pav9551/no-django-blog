from django.shortcuts import render
from .models import Post
posts = Post.objects.all()
# Create your views here.
def main_view(request):
    return render(request, 'blogapp/index.html', context = {'posts': posts})


def create_post(request):
    return render(request, 'blogapp/create.html')
