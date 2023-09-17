from rest_framework.routers import DefaultRouter

from .apps import CategoriesConfig
from .views import CategoriesViewSet

app_name = CategoriesConfig.name

router = DefaultRouter()
router.register(r'', CategoriesViewSet, basename='categories')


urlpatterns = [

] + router.urls
