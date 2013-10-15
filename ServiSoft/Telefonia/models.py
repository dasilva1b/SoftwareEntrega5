from django.db import models

# Create your models here.

class Usuario(models.Model):
  name = models.CharField(max_length=30)
  password = models.CharField(max_length=30)
  tipo_usuario = models.CharField(max_length=30)
  
  def __unicode__(self):
      return self.name
      
class Cliente(models.Model):
  name=models.CharField(max_length=30)
  direccion=models.CharField(max_length=60)
  identificador=models.IntegerField()
  
  def __unicode__(self):
    return "Nombre:"+self.name+" Direccion:"+self.direccion


class Plan(models.Model):
  name=models.CharField(max_length=30)
  descripcion=models.CharField(max_length=90)
  ilimitado=models.IntegerField()
  renta=models.IntegerField()
  
  def __unicode__(self):
    return "Plan:"+self.name+" Renta:"+str(self.renta)
    
    
        
class Incluido_Plan(models.Model):
  plan= models.ForeignKey(Plan, related_name="incluido_plan") 
  tipo=models.CharField(max_length=30) #Lo que se incluye en el plan name
  cantidad=models.IntegerField()
  
  def __unicode__(self):
    return "Incluido:"+self.tipo+"cantidad:"+str(self.cantidad)
    
class Servicio(models.Model):
  name=models.CharField(max_length=30)
  costo=models.IntegerField()
  
  def __unicode__(self):
    return "Servicio:"+self.name+" Costo:"+str(self.costo)
    
       
class Incluido_Servicio(models.Model):
  servicio=models.ForeignKey(Servicio, related_name="incluido_servicio")
  tipo=models.CharField(max_length=30) #Lo que se incluye en el servicio <name>
  cantidad=models.IntegerField()
  
  def __unicode__(self):
     return "Incluido:"+self.tipo+"cantidad:"+str(self.cantidad)
     
class Producto(models.Model):
  cliente=models.ForeignKey(Cliente, related_name="productos")
  plan=models.ForeignKey(Plan, related_name="plan_producto")
  identificador=models.IntegerField()
  name=models.CharField(max_length=30)
  saldo=models.IntegerField()
  
  def __unicode__(self):
    return "Producto:"+self.name+" ID:"+str(self.identificador)
    
class Adiciona(models.Model):
    producto=models.ForeignKey(Producto, related_name="adicionas")
    servicio=models.ForeignKey(Servicio, related_name="adicionados")
    
    def __unicode__(self):
      return "Adiciona"
      
class Consumo(models.Model):
          
  producto=models.ForeignKey(Producto, related_name="consumos")
  tipo=models.CharField(max_length=30)
  mes=models.IntegerField()
  anio=models.IntegerField()
  dia=models.IntegerField()
  hora=models.CharField(max_length=30)
  costo=models.IntegerField()
  
  def __unicode__(self):
    return "Consumo de costo:"+str(self.costo)+" a las: "+self.hora
    
class Factura(models.Model):
  cliente=models.ForeignKey(Cliente, related_name="facturas")
  monto=models.IntegerField()
  mes=models.IntegerField()
  anio=models.IntegerField()
  
  def __unicode__(self):
    return "Factura del mes :"+str(self.mes)+", dia:"+str(self.anio)+"Monto total:"+str(self.monto)+"del cliente "+str(self.cliente)
        
    
  
  