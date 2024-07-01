from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task

def task_list(request):
    sort_by = request.GET.get('sort_by', '-due_date')  
    tasks = Task.objects.all().order_by(sort_by)
    return render(request, 'task_list.html', {'tasks': tasks})

def incomplete_task_list(request):
    sort_by = request.GET.get('sort_by', '-due_date') 
    tasks = Task.objects.filter(completed=False).order_by(sort_by)
    return render(request, 'incomplete_task_list.html', {'tasks': tasks})

def completed_task_list(request):
    sort_by = request.GET.get('sort_by', '-due_date')  
    completed_tasks = Task.objects.filter(completed=True).order_by(sort_by)
    return render(request, 'completed_task_list.html', {'completed_tasks': completed_tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.completed = form.cleaned_data['completed'] if 'completed' in form.cleaned_data else False
            task.save()
            return redirect('incomplete_task_list') 
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form': form})

def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            if 'from_incomplete' in request.GET:
                return redirect('incomplete_task_list')  
            else:
                return redirect('task_detail', pk=pk)  
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_update.html', {'form': form})

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('incomplete_task_list')
    return render(request, 'task_delete.html', {'task': task})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task, 'from_incomplete': True if 'from_incomplete' in request.GET else False})