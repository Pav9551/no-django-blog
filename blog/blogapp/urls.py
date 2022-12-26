
from django.urls import path
from blogapp import views
urlpatterns = [
path('', views.main_view())

]