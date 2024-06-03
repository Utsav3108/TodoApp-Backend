from django.urls import path
from todoApp.views import User, Tasks

urlpatterns = [
    path ('register', User.as_view(), name = 'hello'),
    path('allusers', User.as_view(), name = 'all users'),
    path ('showtasks/<int:pk>', Tasks.as_view(), name = 'tasks'),
    path('<int:pk>/createtask', Tasks.as_view(), name = 'createtask'),
    path('<int:pk>/updatetask/<int:taskid>', Tasks.as_view(), name='updatetask'),
    path('<int:pk>/delete/<int:taskid>', Tasks.as_view(), name = 'delete')
]