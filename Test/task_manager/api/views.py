from django.shortcuts import render
from rest_framework import views, status, response, generics, permissions
from api.serializers import *
from tasks.models import *
from rest_framework.authtoken.models import Token
from . import signals

# Create your views here.

class UserRegistrationView(views.APIView):
    def post(self, request):
        data = {}
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration Successful'
            data['username'] = account.username
            data['email'] = account.email
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            token = Token.objects.get(user=account).key
            data['token'] = token         
        else:
            data = serializer.errors
        return response.Response(data)

####### User Logout API View ######
class LogoutView(views.APIView):
  def post(self, request):
    request.user.auth_token.delete()
    return response.Response(status=status.HTTP_200_OK)

####### Task Add API View #########
class TaskCreateView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = TaskAddSerializers(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            task.user = request.user
            task.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

######## All Task API View #######
class AllTaskAPIView(generics.ListCreateAPIView):
  serializer_class = ShowTaskSerializers
  permission_classes = [permissions.IsAuthenticated]
  
  def get_queryset(self):
    task = Task.objects.filter(user=self.request.user)
    return task
  
####### Task Edit Delete View #####
class TaskRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes  = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = ShowTaskSerializers

####### Single Photo Delete View ####
class PhotoDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = multiplePhoto.objects.all()
    serializer_class = TaskImageSerializers
    