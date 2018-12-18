
from django.urls import path

from . import views
from model import views as modelViews

urlpatterns = [
        path('signup/', modelViews.signup, name='signup'),
        ]
