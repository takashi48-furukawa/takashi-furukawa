from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Task
from .forms import CustomUserCreationForm

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'userapp/signup.html'
    success_url = reverse_lazy('incomplete_task_list')

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(self.request, user)
        return redirect(self.success_url)

class CustomLoginView(LoginView):
    template_name = 'userapp/login.html'
    success_url = reverse_lazy('incomplete_task_list')

    def get_success_url(self):
        return self.success_url

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('incomplete_task_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'userapp/signup.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('incomplete_task_list')
            else:
                return render(request, 'userapp/login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = AuthenticationForm()
    return render(request, 'userapp/login.html', {'form': form})

def incomplete_task_list(request):
    incomplete_tasks = Task.objects.filter(completed=False)
    return render(request, 'incomplete_task_list.html', {'incomplete_tasks': incomplete_tasks})

def completed_task_list(request):
    completed_tasks = Task.objects.filter(completed=True)
    return render(request, 'completed_task_list.html', {'completed_tasks': completed_tasks})

def create_task(request):
    return render(request, 'create_task.html')

def home(request):
    return render(request, 'home.html')
