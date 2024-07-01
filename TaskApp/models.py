from django.db import models
from django.utils import timezone

class Priority(models.TextChoices):
    LOW = '低', '低'
    MEDIUM = '中', '中'
    HIGH = '高', '高'

class Category(models.TextChoices):
    WORK = '仕事', '仕事'
    STUDY = '勉強', '勉強'
    HOBBY = '趣味', '趣味'

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.LOW)  
    category = models.CharField(max_length=10, choices=Category.choices, default=Category.WORK)  
    due_date = models.DateTimeField(null=True, blank=True, default=timezone.now)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    
def __str__(self):
    return self.title
