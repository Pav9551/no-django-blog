
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Post, Tag
from .forms import ContactForm, PostForm
from django.core.mail import send_mail



# Create your views here.
def main_view(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/index.html', context={'posts': posts})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Получить данные из формы
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            send_mail(
                'Contact message',
                f'Ваш сообщение {message} принято',
                'from@example.com',
                [email],
                fail_silently=True,
            )
            print(email)
            return HttpResponseRedirect(reverse('blog:index'))
        else:
            return render(request, 'blogapp/contact.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'blogapp/contact.html', context={'form': form})

def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blogapp/post.html', context={'post': post})
def create_post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'blogapp/create.html', context={'form': form})
    else:
        form = PostForm(request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:index'))
        else:
            return render(request, 'blogapp/create.html', context={'form': form})
class TagListView(ListView):
    model = Tag
    template_name = 'blogapp/tag_list.html'
class TegDetailView(DetailView):
    model = Tag
    template_name = 'blogapp/tag_detail.html'


