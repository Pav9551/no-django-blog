from django.urls import path
from usersapp import views


app_name = 'usersapp'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
]
