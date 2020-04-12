from django.db import models

# Create your models here.
#models are actually database
class Note(models.Model):
   title=models.CharField(max_length=150)
   content=models.TextField()
   created_at=models.DateTimeField(auto_now=True)
   updated_at=models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.title
    