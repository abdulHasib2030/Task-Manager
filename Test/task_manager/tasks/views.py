from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from tasks.models import *
from tasks.forms import *
from django.views.generic.list import ListView
from django.views import View
# Create your views here.

###### Home View ########
class HomeView(ListView):
    template_name = 'index.html'
    
    def get(self, request):
      tasks = Task.objects.filter(user=request.user)
      return render(request, self.template_name, {'tasks':tasks})


######## Add Task View ########
class addTaskView(View):
  template_name = 'task_add.html'
  
  def get(self, request):
    t_form = TaskForm()
    img_form = ImageForm()
    return render(request, self.template_name, {'t_form':t_form, 'img_form':img_form})
  
  def post(self, request):
    t_form = TaskForm(request.POST)
    img_form = ImageForm(request.POST, request.FILES)
    
    if t_form.is_valid() and img_form.is_valid():
      task = t_form.save(commit=False)
      task.user = request.user
      task.save()
      img = request.FILES.getlist('photo')
      for i in img:
        s = multiplePhoto.objects.create(task=task, photo=i)
        s.save()
      return redirect('home')
    else:
      t_form = TaskForm()
      img_form = ImageForm()
    return render(request, self.template_name, {'t_form':t_form, 'img_form':img_form})

# ######## Add Task View ########
# def addTaskView(request):
#   t_form = TaskForm(request.POST)
#   img_form = ImageForm(request.POST, request.FILES)
  
#   if t_form.is_valid() and img_form.is_valid():
#     task = t_form.save(commit=False)
#     task.user = request.user
#     task.save()
#     img = request.FILES.getlist('photo')
#     for i in img:
#       s = multiplePhoto.objects.create(task=task, photo=i)
#       s.save()
#     return redirect('home')
#   else:
#     t_form = TaskForm()
#     img_form = ImageForm()
#   return render(request, 'task_add.html', {'t_form':t_form, 'img_form':img_form})

####### Detail Task View #######
class DetailTaskView(View):
  template_name = 'task_detail.html'
  def get(self, request, pk):
    task_detail = Task.objects.get(pk=pk)
    img = multiplePhoto.objects.filter(task=task_detail)
    return render(request, self.template_name, {'task_detail':task_detail, 'img':img})

# @login_required
# def DetailTaskView(request,pk):
  # task_detail = Task.objects.get(pk=pk)
  # img = multiplePhoto.objects.filter(task=task_detail)
  # return render(request, 'task_detail.html', {'task_detail':task_detail, 'img':img})

####### Update Task View #######
class UpdateTaskView(View):
  template_name = 'task_add.html'
  def get(self, request, pk):
    task = Task.objects.get(pk =pk)
    t_form = TaskForm(instance=task)
    img_form = ImageForm()
    return render(request, self.template_name, {'t_form': t_form, 'img_form': img_form})
    
  def post(self, request, pk):
    task = Task.objects.get(pk =pk)
    if request.method == 'POST':
        t_form = TaskForm(request.POST,  instance=task) 
        img_form = ImageForm(request.POST, request.FILES)
        if t_form.is_valid() or img_form.is_valid():
            tasks = t_form.save()
            img = request.FILES.getlist('photo')
            for i in img:
              s = multiplePhoto.objects.create(task=tasks, photo=i)
              s.save()       
            return redirect('task-detail', pk)
    else:
        t_form = TaskForm(instance=task)
        img_form = ImageForm()
    return render(request, self.template_name, {'t_form': t_form, 'img_form': img_form})
  
# @login_required
# def UpdateTaskView(request, pk):
#     # task = get_object_or_404(Task, pk=task_id)
#     task = Task.objects.get(pk =pk)
   
#     if request.method == 'POST':
#         t_form = TaskForm(request.POST,  instance=task) 
#         img_form = ImageForm(request.POST, request.FILES)
#         if t_form.is_valid() or img_form.is_valid():
#             tasks = t_form.save()
#             img = request.FILES.getlist('photo')
#             for i in img:
#               s = multiplePhoto.objects.create(task=tasks, photo=i)
#               s.save()
              
#             return redirect('task-detail', pk)
#     else:
#         t_form = TaskForm(instance=task)
#         img_form = ImageForm()
#     return render(request, 'task_add.html', {'t_form': t_form, 'img_form': img_form})

####### Delete Photo View #########
class DeletePhotoView(ListView):
  def post(self, request, pk):
    img = multiplePhoto.objects.get(pk=pk)
    k = img.task.id
    img.delete()
    return redirect('task-detail', k)

# @login_required
# def DeletePhotoView(request,pk):
#   img = multiplePhoto.objects.get(pk=pk)
#   k = img.task.id
#   img.delete()
#   return redirect('task-detail', k)

####### Delete Task View ###########
class DeleteTaskView(ListView):
  def post(self, request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('home')
  
# @login_required
# def DeleteTaskView(request, pk):
    # task = Task.objects.get(pk=pk)
    # task.delete()
    # return redirect('home')

#### Complete Task View ##########
class CompleteTaskView(ListView):
  def get(self, request, pk):
    task = Task.objects.get(pk = pk)
    if task.is_complete == False:
      task.is_complete = True
      task.save() 
    return redirect('complete-show-task')

# def CompleteTaskView(requset, pk):
#   task = Task.objects.get(pk = pk)
#   if task.is_complete == False:
#     task.is_complete = True
#     task.save() 
#   return redirect('home')

#### show complete Task
class ShowComplete_task(ListView):
  template_name = 'complete_task.html'
  def get(self, request):
    task = Task.objects.filter(user=request.user, is_complete=True)
    return render(request, self.template_name, {'task':task})

# def ShowComplete_task(request):
#   task = Task.objects.filter(user=request.user, is_complete=True)
#   return render(request, 'complete_task.html', {'task':task})


#### Search Task Title  And Filter Task ###########
class TaskListView(ListView):
    model = Task
    template_name = 'index.html' 
    context_object_name = 'tasks'
    ordering = ['-created_at']

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        tasks = Task.objects.filter(user=self.request.user)

        if keyword:
            tasks = tasks.filter(title__icontains=keyword)

        creation_date = self.request.GET.get('creation_date')
        due_date = self.request.GET.get('due_date')
        priority = self.request.GET.get('priority')
        is_complete = self.request.GET.get('is_complete')

        if creation_date:
            tasks = tasks.filter(created_at=creation_date)

        if due_date:
            tasks = tasks.filter(due_date=due_date)

        if priority:
            tasks = tasks.filter(priority=priority)

        if is_complete:
            tasks = tasks.filter(is_complete=is_complete)
        print(tasks)
        return tasks