from django.urls import path
from restaurants.views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView
)

from . import views

urlpatterns = [
    path('', RestaurantListView.as_view()),
    path('create/', RestaurantCreateView.as_view()),
    path('<slug>/', RestaurantDetailView.as_view()),
]