from django import forms
from tasks.models import *

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['title', 'description', 'due_date', 'priority']
    
  def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            if field == 'is_complete':
              continue
            
            self.fields[field].widget.attrs.update({
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })
            
class ImageForm(forms.ModelForm):
  class Meta:
    model = multiplePhoto
    fields = ['photo']
    
    








# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True

# class MultipleFileField(forms.FileField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault("widget", MultipleFileInput())
#         super().__init__(*args, **kwargs)

#     def clean(self, data, initial=None):
#         single_file_clean = super().clean
#         if isinstance(data, (list, tuple)):
#             result = [single_file_clean(d, initial) for d in data]
#         else:
#             result = single_file_clean(data, initial)
#         return result


# class FileFieldForm(forms.Form):
#     file_field = MultipleFileField()
    
    


# class addTaskForm(forms.ModelForm):
#   class Meta:
#     model = Task
#     fields = ['title', 'description', 'due_date', 'priority', 'is_complete']
    
# class ImagesForm(forms.Form):
#   photos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
  
#   class Meta(addTaskForm.Meta):
#     fields = addTaskForm.Meta.fields + ['photos']
    
  # def create(self, validated_data):
  #   up_img = validated_data.pop('upload_photo')
  #   addtask = Task.objects.create(**validated_data)
  #   for i in up_img:
  #     multiplePhoto.objects.create(task=addtask, photo=i)
    
  #   return addtask













# class multiplePhotoForm(forms.ModelForm):
#   class Meta:
#     model = multiplePhoto
#     fields = ['photo']
#   def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs.update({
#                 'class': (
#                     'appearance-none block w-full bg-gray-200 '
#                     'text-gray-700 border border-gray-200 rounded '
#                     'py-3 px-4 leading-tight focus:outline-none '
#                     'focus:bg-white focus:border-gray-500'
#                 )
#             })

# class addtaskForm(forms.ModelForm):
#   photo = multiplePhotoForm()
#   class Meta:
#     model = Task
#     fields = ['title', 'description', 'due_date', 'priority', 'is_complete', 'photo']
    
    
    
#   def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields:
          
#             if field == 'is_complete':
#               continue
#             self.fields[field].widget.attrs.update({
#                 'class': (
#                     'appearance-none block w-full bg-gray-200 '
#                     'text-gray-700 border border-gray-200 rounded '
#                     'py-3 px-4 leading-tight focus:outline-none '
#                     'focus:bg-white focus:border-gray-500'
#                 )
#             })


# from django import forms
# from .models import Task

# class TaskForm(forms.ModelForm):
#     photos = forms.ModelMultipleChoiceField(
#         queryset=multiplePhoto.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=False
#     )

#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'due_date', 'priority', 'is_complete', 'photos']
