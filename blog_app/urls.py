from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsView.as_view(), name='home'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
