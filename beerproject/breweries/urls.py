from django.urls import path

from .views import BreweriesView

urlpatterns = [
    path('', BreweriesView.as_view(), name='index'),
]