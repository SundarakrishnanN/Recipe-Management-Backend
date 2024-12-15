from django.db import models
from login.models import CustomUser

class Recipe(models.Model):
  
    name = models.CharField(max_length=255)
    
    
    image = models.ImageField(upload_to='recipes/images/')
    
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    
    is_veg = models.BooleanField(default=True)
    
    quantity = models.CharField(max_length=255)
    
    ingredients = models.TextField()
    
    
    description = models.TextField()

 
    def __str__(self):
        return self.name

  
    def get_ingredients_list(self):
        return self.ingredients.split(",")  

