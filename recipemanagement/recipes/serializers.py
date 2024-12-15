from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Recipe
from rest_framework.exceptions import PermissionDenied
from login.serializers import UserSerializer
class RecipeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested user serializer

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'image','is_veg','quantity', 'ingredients','description','user']
        
        extra_kwargs = {
            'user': {'read_only': True}  # Ensure the user field is read-only
        }

    def create(self, validated_data):        
        user = self.context['request'].user
        recipe = Recipe.objects.create(user=user,**validated_data)
        return recipe
    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.user != user:
            raise PermissionDenied("You do not have permission to update this recipe.")
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.is_veg = validated_data.get('is_veg', instance.is_veg)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.ingredients = validated_data.get('ingredients', instance.ingredients)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
