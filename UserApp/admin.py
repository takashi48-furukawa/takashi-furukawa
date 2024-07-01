from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_active')  
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('password',)}),  
        ('Personal info', {'fields': ('first_name', 'last_name', 'birthday')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('password1', 'password2', 'first_name', 'last_name', 'birthday', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('username', 'first_name', 'last_name')  
    ordering = ('first_name',)  
        
admin.site.register(CustomUser, CustomUserAdmin)
