from django.db import models

class Empleado(models.Model):
    DNI = models.CharField(max_length=9, primary_key=True)
    Nombre = models.CharField(max_length=100)
    Pais = models.CharField(max_length=50)
    DEPARTAMENTO_CHOICES = (
        ('Marketing','Marketing'),
        ('RRHH','RRHH'),
        ('Informática','Informática'),
        ('Administración','Administración'),
        ('Obras','Obras'),
        ('SAT','SAT'),
        ('Presupuestos','Presupuestos'),
        ('Producción','Producción'),
        ('Delineante','Delineante'),
        ('Compras','Compras'),
        ('Comercial','Comercial'),
    )
    Departamento = models.CharField(max_length=20, choices=DEPARTAMENTO_CHOICES)
    Email = models.EmailField(max_length=254, default="null@mail.com")
    def __str__(self):
        return "%s" % (self.DNI)

class Prestamo(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    DISPOSITIVO_CHOICES = (
        ('Telefono','Telefono'),
        ('Ordenador','Ordenador'),
    )
    Dispositivo = models.CharField(max_length=9, choices=DISPOSITIVO_CHOICES)
    Identificador = models.CharField(max_length=30)
    Marca = models.CharField(max_length=30)
    Modelo = models.CharField(max_length=50)
    CPU = models.CharField(max_length=50, blank=True)
    RAM_CHOICES = (
        ('2GB','2GB'),
        ('3GB','3GB'),
        ('4GB','4GB'),
        ('8GB','8GB'),
        ('12GB','12GB'),
        ('16GB','16GB'),
        ('32GB','32GB'),
        ('64GB','64GB'),
    )
    RAM = models.CharField(max_length=5, choices=RAM_CHOICES)
    ALMACENAMIENTO_CHOICES = (
        ('16GB','16GB'),
        ('32GB','32GB'),
        ('64GB','64GB'),
        ('128GB','128GB'),
        ('256GB','256GB'),
        ('512GB','512GB'),
        ('1TB','1TB'),
    )
    Almacenamiento = models.CharField(max_length=6, choices=ALMACENAMIENTO_CHOICES)
    NumeroSerie = models.CharField(max_length=50)
    Observaciones = models.CharField(max_length=70, blank=True)
    FechaInicio = models.DateField('Fecha Inicio')
    FechaDevolucion = models.DateField('Fecha Entrega', blank=True, null=True)
    def __str__(self):
        return "%s %s" % (self.Marca, self.Modelo)
    
class Aplicaciones(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    programa = models.CharField(max_length=35, blank=True)
    detalles = models.CharField(max_length=70, blank=True)
    fecha = models.DateField('Fecha', blank=True, null=True)