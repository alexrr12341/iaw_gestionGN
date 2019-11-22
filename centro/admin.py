# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.db import models
from centro.models import Cursos,Alumnos,Departamentos,Profesores,Areas,Modulos
from django.contrib.admin.widgets import FilteredSelectMultiple
# Register your models here.
class AlumnosAdmin(admin.ModelAdmin):
    #date_hierarchy = 'Fecha_nacimiento'
    actions_selection_counter=False
    list_filter = ['Unidad','Localidad']
    list_display = ["Nombre",'DNI','Localidad','Telefono1']
     
    search_fields = ['Nombre','DNI']

class PorfesoresAdmin(admin.ModelAdmin):
    #date_hierarchy = 'Fecha_nacimiento'
    actions_selection_counter=False
    list_filter = ['Departamento']
    list_display = ["Nombre",'Apellidos','Email','Departamento']
     
    search_fields = ['Nombre','Apellidos']

class CursosAdmin(admin.ModelAdmin):
    #date_hierarchy = 'Fecha_nacimiento'
    actions_selection_counter=False
    
    list_display = ["Curso",'Tutor']
     
    search_fields = ['Curso']

    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple("Profesores", is_stacked=False)},
    }
   
class AreasAdmin(admin.ModelAdmin):
    actions_selection_counter=False
    
    list_display = ["Nombre"]
     
    search_fields = ['Nombre']

    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple("Departamentos", is_stacked=False)},
    }
    # Register your models here.
admin.site.site_header="Gonzalo Nazareno"
admin.site.index_title="Gestión amonestaciones"
admin.site.register(Cursos,CursosAdmin)
admin.site.register(Departamentos)
admin.site.register(Areas,AreasAdmin)
admin.site.register(Alumnos,AlumnosAdmin)
admin.site.register(Profesores,PorfesoresAdmin)
admin.site.register(Modulos)
