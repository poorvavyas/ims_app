from django.urls import path
from account.api import AddUser, LoginUser, logout_user


urlpatterns = [
    path('', LoginUser.as_view()),
    path('add_user/', AddUser.as_view(), name='add_user'),
    path('login_user/', LoginUser.as_view(), name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
]
