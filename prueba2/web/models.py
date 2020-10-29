from django.db import models

# Create your models here.
class usuario(models.Model):
    id_usuario       = models.AutoField(db_column='id_usuario', primary_key=True)
    nombre           = models.CharField(max_length=20, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=20, blank=True, null=True)
    apellido_materno = models.CharField(max_length=20, blank=True, null=True)
    dirrecion        = models.CharField(max_length=20, blank=True, null=True)
    celular          = models.CharField(max_length=13, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    Email            = models.CharField(max_length=50, blank=True, null=True)
    Contraseña       = models.CharField(max_length=50, blank=True, null=True)
    Pais             = models.CharField(max_length=50, blank=True, null=True)
    genero           = models.CharField(max_length=10, blank=True, null=True)
    Numero_Documento = models.CharField(max_length=10, unique=True)

class producto(models.Model):
    id_producto_d    = models.AutoField(db_column='id_producto_d', primary_key=True)
    codigo           = models.IntegerField(unique=True, null=True)
    marca            = models.CharField(max_length=20, blank=True, null=True)
    modelo           = models.CharField(max_length=20, blank=True, null=True)
    descripcion      = models.CharField(max_length=200, blank=True, null=True)
    precio           = models.CharField(max_length=20, blank=True, null=True)
    Foto_producto_d  = models.ImageField(upload_to='fotos_d', blank=True, null=True)
    activo           = models.IntegerField(blank=True, null=True)
    tipo             = models.CharField(max_length=200, blank=True, null=True)
    destacado        = models.IntegerField(blank=True, null=True)
