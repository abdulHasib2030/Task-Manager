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
    
    
