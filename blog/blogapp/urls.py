
from django.urls import path
from blogapp import views
app_name = 'blogapp'
urlpatterns = [
path('', views.main_view, name='index'),

]