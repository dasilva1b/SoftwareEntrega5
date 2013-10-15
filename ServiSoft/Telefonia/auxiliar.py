from Telefonia.models import Usuario,Cliente, Plan, Incluido_Plan, Servicio, Incluido_Servicio, Producto, Adiciona, Consumo
from django.http import HttpResponse
import datetime
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render



def facturarPostpago(cliente,mes1,anio1): 
  #Paso 1: Conseguir productos del cliente
  #todos_planespost=Plan.objects.filter(ilimitado < 2)
  productos_cliente=cliente.productos.all()
  productos_postpago=[]
  montoglobal=0
  listaproductos=[]
  for a in productos_cliente:
    plan=a.plan
    if (plan.ilimitado < 2):
      productos_postpago.append(a)
  
  #En productos_postpago quedan los prods postpago del cliente a facturar.
  #Iteraremos sobre cada producto
  for b in productos_postpago:
    renta=b.plan.renta
    listaproductos.append(b.name)
    montototal=0
    montototal=montototal+renta
    
    #Vemos los consumos de ese producto.
    consumossumados=[]
    consumos=b.consumos.filter(mes=mes1, anio=anio1)
    for c in consumos:
      if (c.tipo not in consumossumados):
	consumossumados.append(c.tipo)
	consumossumados.append(c.costo)
      else:
	pos=consumossumados.index(c.tipo)
	consumossumados[pos+1]+=c.costo
    
    #En consumos sumados tenemos una lista que contiene:
    #la suma de todo lo consumido dividdo por tipo de 
    #consumo (Llamada-100,Mensaje-200,etc)
    
    incluidossumados=[]
    incluidos=b.plan.incluido_plan.all()
    for c in incluidos:
      if (c.tipo not in incluidossumados):
	incluidossumados.append(c.tipo)
	incluidossumados.append(c.cantidad)
      else:
	pos=incluidossumados.index(c.tipo)
	incluidossumados[pos+1]+=c.cantidad
      
    #Obtendremos renta correspondiente por servicios adicionales
    #Veremos tambien lo que esta incluido en los servicios extra que posea el producto
    servicios=b.adicionas.all()
    rentaservs=0
    for w in servicios:
      rentaservs+=w.servicio.costo
      incluserv=w.servicio.incluido_servicio.all()
      for c in incluserv:
	if (c.tipo not in incluidossumados):
	  incluidossumados.append(c.tipo)
	  incluidossumados.append(c.cantidad)
	else:
	  pos=incluidossumados.index(c.tipo)
	  incluidossumados[pos+1]+=c.cantidad
      
    #Procedemos a restar lo que ha consumido menos lo que tenia incluido
    sobrepaso=0
    for w in consumossumados:
      for t in incluidossumados:
	if ((isinstance(w,unicode)) & (isinstance(t,unicode))):
	  if (w == t):
	    posw=consumossumados.index(w)+1
	    post=incluidossumados.index(t)+1
	    consumossumados[posw]-=incluidossumados[post]
	    
    #Obtenemos el monto de sobrepaso
    for w in consumossumados:
      if (isinstance(w,unicode)):
	sobrepaso+=0
      else:
	if (w > 0):
	  sobrepaso+=w

    montototal+=sobrepaso
    montototal+=rentaservs
    
    montoglobal+=montototal
    
 
  return (montoglobal, listaproductos)
  
def facturarPrepago(cliente):
  productos_cliente=cliente.productos.all()
  productos_pre=[]
  lprods=[]
  montoglobal=0
  montototal=0
  for a in productos_cliente:
    plan=a.plan
    if (plan.ilimitado == 2):
      productos_pre.append(a)
      
  montoglobal=0   
  for b in productos_pre:
    renta=b.plan.renta
    lprods.append(b.name)
    montototal=0
    montototal=montototal+renta
    
    servicios=b.adicionas.all()
    rentaservs=0
    for w in servicios:
      rentaservs+=w.servicio.costo
      
    montototal+=rentaservs
    
  montoglobal+=montototal
  
  return (montoglobal,lprods)
  