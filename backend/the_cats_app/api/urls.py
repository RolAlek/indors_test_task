from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from backend.the_cats_app.api.views import CatDetailView, CatListView, UserView

auth_patterns = [
    path('register/', UserView.as_view()),
    path('token-auth/', obtain_auth_token),
]

urlpatterns = [
    path('', CatListView.as_view()),
    path('<int:pk>/', CatDetailView.as_view()),
    path('users/', include(auth_patterns)),
]
