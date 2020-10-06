from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'slug', 'start_date', 'created_at'] #mostra no admin esses campos em cada registro que foi criado
    search_fields = ['name', 'slug'] #Pesquisar na tabela
    prepopulated_fields = {'slug': ('name',)} #pega o que foi escrito em nome e joga no campo slug

admin.site.register(Course, CourseAdmin)
