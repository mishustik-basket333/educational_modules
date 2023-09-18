from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import UsersCreateAPIView, UserListAPIView, UsersRetrieveAPIView, UsersUpdateAPIView, \
    UsersDestroyAPIView, UserPublishedListAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('create/', UsersCreateAPIView.as_view(), name='user_create'),
    path('', UserPublishedListAPIView.as_view(), name='users'),
    path('all/', UserListAPIView.as_view(), name='users_all'),
    path('<int:pk>/', UsersRetrieveAPIView.as_view(), name='user'),
    path('update/<int:pk>/', UsersUpdateAPIView.as_view(), name='users_update'),
    path('delete/<int:pk>/', UsersDestroyAPIView.as_view(), name='users_delete'),
]
