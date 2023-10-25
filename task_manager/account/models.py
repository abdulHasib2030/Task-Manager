from django.db import models
from django.contrib.auth.models import User
from account.contents import GENDER_TYPE

class UserAccount(models.Model):
  user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
  birth_date = models.DateField(null=True, blank=True)
  gender = models.CharField(max_length=10, choices=GENDER_TYPE)
  image = models.ImageField(upload_to='images/profile/', default = 'profile.jpg', null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  
  def __str__(self):
      return self.user.first_name + self.user.last_name