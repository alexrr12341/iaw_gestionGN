
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Departamentos(models.Model):
	Abr = models.CharField(max_length=4)
	Nombre = models.CharField(max_length=30)

	def __str__(self):
		return self.Nombre

	class Meta:
		verbose_name="Departamento"
		verbose_name_plural="Departamentos"


class Areas(models.Model):
	   
	Nombre = models.CharField(max_length=30)
	Departamentos=models.ManyToManyField(Departamentos,blank=True)

	def __str__(self):
		return self.Nombre

	class Meta:
		verbose_name="Área"
		verbose_name_plural="Áreas"



class Profesores(models.Model):
	Nombre = models.CharField(max_length=20)
	Apellidos = models.CharField(max_length=30)
	Telefono = models.CharField(max_length=9,blank=True)
	Movil = models.CharField(max_length=9,blank=True)
	Email = models.EmailField()
	Departamento = models.ForeignKey(Departamentos,blank=True,null=True,on_delete=models.SET_NULL)
	Baja = models.BooleanField(default=False)
	Ce = models.BooleanField(default=False,verbose_name="Consejo Escolar")
	Etcp = models.BooleanField(default=False)
	Tic = models.BooleanField(default=False)
	Bil = models.BooleanField(default=False,verbose_name="Bilingüe")
	
	

	def __str__(self):
		return self.Nombre+" "+self.Apellidos

	class Meta:
		verbose_name="Profesor"
		verbose_name_plural="Profesores"

class Cursos(models.Model):
	
	Curso = models.CharField(max_length=30)
	Tutor = models.ForeignKey(Profesores, related_name='Tutor_de',blank=True,null=True,on_delete=models.SET_NULL)
	EquipoEducativo=models.ManyToManyField(Profesores, verbose_name="Equipo Educativo",blank=True)

	def __str__(self):
		return self.Curso

	class Meta:
		verbose_name="Curso"
		verbose_name_plural="Cursos"

class Alumnos(models.Model):
	Nombre = models.CharField(max_length=50)
	DNI = models.CharField(max_length=10)
	Direccion = models.CharField(max_length=60)
	CodPostal = models.CharField(max_length=5,verbose_name="Código postal")
	Localidad = models.CharField(max_length=30)
	Fecha_nacimiento = models.DateField('Fecha de nacimiento')
	Provincia = models.CharField(max_length=30)
	Unidad = models.ForeignKey(Cursos,blank=True,null=True,on_delete=models.SET_NULL)
	Ap1tutor = models.CharField(max_length=20,verbose_name="Apellido 1 Tutor")
	Ap2tutor = models.CharField(max_length=20,verbose_name="Apellido 2 Tutor")
	Nomtutor = models.CharField(max_length=20,verbose_name="Nombre tutor")
	Telefono1 = models.CharField(max_length=12,blank=True)
	Telefono2 = models.CharField(max_length=12,blank=True)
	Obs=models.TextField(blank=True,verbose_name="Observaciones")

	def __str__(self):
		return self.DNI+" - "+self.Nombre 

	class Meta:
		verbose_name="Alumno"
		verbose_name_plural="Alumnos"


class Modulos(models.Model):	
     Abr = models.CharField(max_length=4)
     Nombre = models.CharField(max_length=50)
     Unidad = models.ForeignKey(Cursos,blank=True,null=True,on_delete=models.SET_NULL)
		
     def __unicode__(self):
         return self.Abr+" - "+self.Nombre 		

     class Meta:
         verbose_name="Modulo"
         verbose_name_plural="Modulos"
