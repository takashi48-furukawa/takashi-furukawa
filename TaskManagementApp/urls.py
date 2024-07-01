from django.contrib import admin
from django.urls import path, include
from UserApp.views import signup, custom_login, home
from TaskApp.views import  task_list
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('user/', include('UserApp.urls')),
    path('task/', include('TaskApp.urls')),
    path('user/signup/', signup, name='signup'),
    path('user/login/', custom_login, name='login'),
    path('', task_list, name='task_list'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)