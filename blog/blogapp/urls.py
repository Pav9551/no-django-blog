
from django.urls import path
from blogapp import views
app_name = 'blogapp'
urlpatterns = [
path('', views.main_view, name='index'),
path('contact', views.contact_view, name='contact'),
path('create', views.create_post, name='create'),
path('post/<int:id>/', views.post, name='post'),
path('tag-list', views.TagListView.as_view(), name='tag-list'),
path('tag-ditail/<int:pk>/', views.TegDetailView.as_view(), name='tag_detail'),
]