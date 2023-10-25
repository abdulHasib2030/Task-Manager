from django.contrib.auth.models import User
from rest_framework import serializers
from tasks.models import *
from account.models import *
from account.contents import GENDER_TYPE

####### User Register Serializer ######
class UserRegistrationSerializer(serializers.ModelSerializer):
  password2 = serializers.CharField(style={"input_type": 'password'}, write_only='True')
  
  class Meta:
    model = User
    fields = ['username', 'email', 'password', 'password2','first_name', 'last_name']
    extra_kwargs= {
      'password':{'write_only':True},
      
    }
  def save(self):
    username = self.validated_data['username']
    email = self.validated_data['email']
    password = self.validated_data['password']
    password2 = self.validated_data['password2']
    first_name = self.validated_data['first_name']
    last_name = self.validated_data['last_name']
    
    if password != password2:
      raise serializers.ValidationError({'error':'password does not matched'})
    if User.objects.filter(email=email).exists():
      raise serializers.ValidationError({'error':'email already exists'})
    account = User(username=username, email= email, first_name=first_name, last_name=last_name)
    account.set_password(password)
    
    account.save()
    return account

###### Task  Add Serializers #########
class TaskImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = multiplePhoto
        fields = "__all__"
      
class TaskAddSerializers(serializers.ModelSerializer):
    photo =  TaskImageSerializers(many=True, read_only=True)
    upload_photo = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Task
        fields = ["title", "description",'due_date', 'priority','photo', 'upload_photo']

    def create(self, validated_data):
        upload_photo = validated_data.pop("upload_photo")
        task = Task.objects.create(**validated_data)

        for i in upload_photo:
            multiplePhoto.objects.create(task=task, photo=i)

        return task

#### Show Edit Delete Task Serializers ####
class ShowTaskSerializers(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'
    
