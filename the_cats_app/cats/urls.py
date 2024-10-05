from django.urls import path

from .views import cat_detail, cat_list


urlpatterns = [
    path('', cat_list),
    path('<int:pk>/', cat_detail),
]
