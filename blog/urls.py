from django.urls import path
from . import views



urlpatterns = [
    # no addition to the url sends users to main page containing post lists
    path('', views.post_list, name='post_list'),
]