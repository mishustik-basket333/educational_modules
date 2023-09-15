from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from categories.models import Category
from categories.pagination import CategoriesPagination
from categories.serializers import CategoriesSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    """ view set for Categories"""
    serializer_class = CategoriesSerializer
    pagination_class = CategoriesPagination

    def get_queryset(self):
        return Category.objects.all()
        # if self.request.user.is_staff or self.request.user.is_superuser:
        #     return Course.objects.all()
        # if self.request.user.is_superuser:
        #     return Course.objects.all()
        # return Course.objects.filter(owner=self.request.user)

    default_permission_class = [AllowAny()]
    # permissions = {
    #     'create': [IsSuperUserPermission()],
    #     'list': [IsAuthenticated() or IsModeratorPermission() or IsSuperUserPermission()],
    #     'retrieve': [IsAuthenticated() or IsModeratorPermission() or IsSuperUserPermission()],
    #     'update': [IsAuthenticated() or IsModeratorPermission() or IsSuperUserPermission()],
    #     'partial_update': [IsAuthenticated() or IsModeratorPermission() or IsSuperUserPermission()],
    #     'destroy': [IsSuperUserPermission()],
    #
    # }
