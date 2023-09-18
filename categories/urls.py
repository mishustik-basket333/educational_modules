from django.urls import path

from .apps import CategoriesConfig
from .views import CategoriesCreateAPIView, CategoriesListAPIView, CategoriesRetrieveAPIView, CategoriesUpdateAPIView, \
    CategoriesDestroyAPIView

# from .views import CategoriesViewSet
# from rest_framework.routers import DefaultRouter

app_name = CategoriesConfig.name

urlpatterns = [
    path('create/', CategoriesCreateAPIView.as_view(), name='categories_create'),
    path('', CategoriesListAPIView.as_view(), name='categories'),
    path('<int:pk>/', CategoriesRetrieveAPIView.as_view(), name='category'),
    path('update/<int:pk>/', CategoriesUpdateAPIView.as_view(), name='modules_update'),
    path('delete/<int:pk>/', CategoriesDestroyAPIView.as_view(), name='modules_delete'),
]

# router = DefaultRouter()
# router.register(r'', CategoriesViewSet, basename='categories')
#
#
# urlpatterns = [
#
# ] + router.urls
