from django.urls import path
from .views import *

urlpatterns = [
    path('create-user/', CreateUserView.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),

]
