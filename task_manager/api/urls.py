from django.urls import path
from api.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  
  path('register/', UserRegistrationView.as_view(), name='user-register-api'),
  path('login/', obtain_auth_token, name='login-api'),
  
  path('logout/', LogoutView.as_view(), name = 'logout-api'),
  
  ### add Task Url ##
  path('create/', TaskCreateView.as_view(), name = 'add-task-api'),
  path('task/', AllTaskAPIView.as_view(), name='all-task-api'),
  path('task/<int:pk>/', TaskRetrieveUpdateDeleteView.as_view(), name='all-task-edit-api'),
     
  ## Single Image Delete ##
  path('delete/<int:pk>/', PhotoDeleteAPIView.as_view(), name ='single-photo-delete-api')
]
