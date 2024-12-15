from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer  


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_permissions(self):

        self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    def perform_destroy(self, instance):

        if instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this recipe.")
        instance.delete()

    @action(detail=False, methods=['get'], url_path='my-recipes', permission_classes=[IsAuthenticated])
    def get_user_recipes(self, request):
        """
        Custom endpoint to get all recipes uploaded by the authenticated user.
        """
        user = request.user  # Get the authenticated user
        recipes = Recipe.objects.filter(user=user)  # Filter recipes uploaded by the user
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def get_recipe_by_id(self, request, pk=None):
        """
        Custom endpoint to get a specific recipe by its ID.
        """
        try:
            recipe = Recipe.objects.get(pk=pk)  # Retrieve the recipe by its primary key (ID)
            serializer = RecipeSerializer(recipe)
            return Response(serializer.data)
        except Recipe.DoesNotExist:
            return Response({"detail": "Recipe not found."}, status=404)

