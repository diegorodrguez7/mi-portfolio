from django.db import models

# Create your models here.

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    link = models.URLField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='proyectos_imagenes/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    
class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.IntegerField(help_text="Nivel de habilidad (1-100)")
    descripcion = models.TextField(blank=True, null=True)
    icono = models.ImageField(upload_to='habilidades_iconos/', blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Resumen(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion_principal = models.TextField()
    descripcion_secundaria = models.TextField()

    def __str__(self):
        return self.titulo
    
class Servicio(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.CharField(max_length=50, help_text="Clase FontAwesome, ej: 'fas fa-code'")

    def __str__(self):
        return self.titulo

class EntradaBlog(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='blog_imagenes/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
