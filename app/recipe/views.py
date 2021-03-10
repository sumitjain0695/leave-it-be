from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient

from recipe import serializers


class BaseRecipeAttrViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    """
    base viewset for user owned recipe attributes
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        return object for current authenticated user
        """
        return self.queryset.filter(user=self.request.user).order_by('-name')
    
    def perform_create(self, serializer):
        """
        create a new tag
        """
        serializer.save(user=self.request.user)


class TagViewset(BaseRecipeAttrViewSet):
    """
    manage tags in database
    """
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
class IngredientViewSet(BaseRecipeAttrViewSet):
    """
    Manage ingredients in the database
    """
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer