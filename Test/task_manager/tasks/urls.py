from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from tasks.views import *

urlpatterns = [ 
    path('', HomeView.as_view(), name = 'home'),
    path('add-task/', addTaskView.as_view(), name='add-task'),
    path('detail/<int:pk>/', DetailTaskView.as_view(), name='task-detail'),
    path('update/<int:pk>/', UpdateTaskView.as_view(), name='update-task'),
    path('delete-img/<int:pk>/', DeletePhotoView.as_view(), name='delete-img'),
    path('delete-task/<int:pk>/', DeleteTaskView.as_view(), name='delete-task'),
    
    path('complete/<int:pk>/', CompleteTaskView.as_view(), name = 'complete-task'),
    path('complete-task/', ShowComplete_task.as_view(), name = 'complete-show-task'),
    path('search/', TaskListView.as_view(), name = 'search'),
  
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
