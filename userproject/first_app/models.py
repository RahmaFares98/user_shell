from django.db import models
# Create your models here.
class User (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=25)	# if no age is entered for a new/existing, age will be set to 200
   #age = models.IntegerField(null=True)	# if no age is provided, the field will remain empty
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
def create_user(first_name, last_name, email, age):## to pass it in views ) 
    return User.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        age=age
    )