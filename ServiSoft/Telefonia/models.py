from django.db import models
#Aca se representan los modelos, el aspecto logico de nuestro sistema

#Clase que representa a un usuario del sistema.
#Puede ser un usuario administrador, o un cliente
#de la empresa
class Usuario(models.Model):
  name = models.CharField(max_length=30)
  password = models.CharField(max_length=30)
  tipo_usuario = models.CharField(max_length=30)
  
  def __unicode__(self):
      return self.name

#Clase que representa a un cliente de la compania
#de telefonia. Contiene un nombre,direccion y su
#identificador, sera cedula o rif.
class Cliente(models.Model):
  name=models.CharField(max_length=30)
  direccion=models.CharField(max_length=60)
  identificador=models.IntegerField()
  
  def __unicode__(self):
    return "Nombre:"+self.name+" Direccion:"+self.direccion


#Clase representante de un plan de servicios de la compania.
#Posee un nombre, una descripcion, un valor "ilimitado" que
#delimita el tipo de plan que es, y la renta correspondiente
class Plan(models.Model):
  name=models.CharField(max_length=30)
  descripcion=models.CharField(max_length=90)
  ilimitado=models.IntegerField()
  renta=models.IntegerField()
  
  def __unicode__(self):
    return "Plan:"+self.name+" Renta:"+str(self.renta)
    
    
#Clase usada para representar que se incluye en un plan dado.
#Tenemos una clave foranea al plan del cual se especifica lo
#que esta incluido (tipo) y en que cantidad (cantidad)
class Incluido_Plan(models.Model):
  plan= models.ForeignKey(Plan, related_name="incluido_plan") 
  tipo=models.CharField(max_length=30) #Lo que se incluye en el plan name
  cantidad=models.IntegerField()
  
  def __unicode__(self):
    return "Incluido:"+self.tipo+"cantidad:"+str(self.cantidad)

#Clase que representa un servicio adicional, paquete o afin que
#ofrece la compania y que se puede asociar a algun producto
class Servicio(models.Model):
  name=models.CharField(max_length=30)
  costo=models.IntegerField()
  
  def __unicode__(self):
    return "Servicio:"+self.name+" Costo:"+str(self.costo)
    
#Clase cuya funcion es analoga al Incluido_Plan, solo que para servicios       
class Incluido_Servicio(models.Model):
  servicio=models.ForeignKey(Servicio, related_name="incluido_servicio")
  tipo=models.CharField(max_length=30) #Lo que se incluye en el servicio <name>
  cantidad=models.IntegerField()
  
  def __unicode__(self):
     return "Incluido:"+self.tipo+"cantidad:"+str(self.cantidad)

#Clase que representa un producto de la compania. Dicho producto
#pertenece a algun cliente, tiene un nombre y un identificador
#numerico, y esta asociado a algun plan.
class Producto(models.Model):
  cliente=models.ForeignKey(Cliente, related_name="productos")
  plan=models.ForeignKey(Plan, related_name="plan_producto")
  identificador=models.IntegerField()
  name=models.CharField(max_length=30)
  saldo=models.IntegerField()
  
  def __unicode__(self):
    return "Producto:"+self.name+" ID:"+str(self.identificador)
 
#Clase que representa la asociacion de un producto y un servicio extra.
#El producto adiciona un servicio.
class Adiciona(models.Model):
    producto=models.ForeignKey(Producto, related_name="adicionas")
    servicio=models.ForeignKey(Servicio, related_name="adicionados")
    
    def __unicode__(self):
      return "Adiciona"

#Clase con la que se representa un consumo realizado por algun producto.
#Se especifica que se consumio (tipo) y cuanto (costo).
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

#Clase que representa una factura en el sistema.La factura se hizo
#para un cliente, en un mes y anio dado y por un monto especifico.
class Factura(models.Model):
  cliente=models.ForeignKey(Cliente, related_name="facturas")
  monto=models.IntegerField()
  mes=models.IntegerField()
  anio=models.IntegerField()
  
  def __unicode__(self):
    return "Factura del mes :"+str(self.mes)+", dia:"+str(self.anio)+"Monto total:"+str(self.monto)+"del cliente "+str(self.cliente)
        
    
  
  