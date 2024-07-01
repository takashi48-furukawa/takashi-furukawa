from django.urls import path
from UserApp.views import incomplete_task_list, create_task, completed_task_list, signup, custom_login

urlpatterns = [
    path('user/signup', signup, name='signup'),
    path('user/login', custom_login, name='login'),
    path('task/incomplete/', incomplete_task_list, name='incomplete_task_list'),
    path('task/create/', create_task, name='create_task'),
    path('task/completed/', completed_task_list, name='completed_task_list'),
]