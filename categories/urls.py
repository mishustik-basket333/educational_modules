from django.urls import path

from .apps import CategoriesConfig
from .views import CategoriesListView

app_name = CategoriesConfig.name

urlpatterns = [

    path('', CategoriesListView.as_view(), name='list_view')
]
