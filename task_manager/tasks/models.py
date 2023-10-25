from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Priority(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)

class multiplePhoto(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to= 'task_photos/', null=True, blank= True)
    
   
