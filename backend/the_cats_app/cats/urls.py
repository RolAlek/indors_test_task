from django.urls import path

from .views import CatDetailView, CatListView


urlpatterns = [
    path('', CatListView.as_view()),
    path('<int:pk>/', CatDetailView.as_view()),
]
