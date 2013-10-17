from Telefonia.models import Usuario,Cliente, Plan, Incluido_Plan, Servicio, Incluido_Servicio, Producto, Adiciona, Consumo, Factura
#from nose.tools import assert_not_equal
from django.http import HttpResponse
import datetime
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from auxiliar import facturarPostpago, facturarPrepago

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class Pruebas_Modulos(TestCase):
    
    def test_Usuario1(self):
        usuario1 = Usuario(name='Pedro', password='123', tipo_usuario='Cliente Regular')
        usuario1.save()
        respuesta = Usuario.objects.get(name='Pedro', password='123', tipo_usuario='Cliente Regular')
        
        self.assertEqual(respuesta, usuario1)

    def test_Usuario2(self):
        usuario2 = Usuario(name='Juan', password='1234', tipo_usuario='Administrador')
        usuario2.save()
        respuesta = Usuario.objects.get(name='Juan', password='1234', tipo_usuario='Administrador')
        
        self.assertEqual(respuesta, usuario2)
        
    def test_Cliente1(self):
	cliente1 = Cliente(name='Pedro', direccion='La Trinidad', identificador='21348206')
	cliente1.save()
	respuesta = Cliente.objects.get(name='Pedro', direccion='La Trinidad', identificador='21348206')
	
	self.assertEqual(respuesta, cliente1)
	
    def test_Cliente2(self):
	cliente2 = Cliente(name='Juan', direccion='Baruta', identificador='22448206')
	cliente2.save()
	respuesta = Cliente.objects.get(name='Juan', direccion='Baruta', identificador='22448206')
	
	self.assertEqual(respuesta, cliente2)
	
    def test_Plan1(self):
	plan1 = Plan( name='plan1', descripcion='super plan', ilimitado=1, renta=100)
	plan1.save()
	respuesta = Plan.objects.get( name='plan1', descripcion='super plan', ilimitado=1, renta=100)
	
	self.assertEqual(respuesta, plan1)

    def test_Plan2(self):
	plan2 = Plan( name='plan2', descripcion='super plan2', ilimitado=2, renta=200)
	plan2.save()
	respuesta = Plan.objects.get( name='plan2', descripcion='super plan2', ilimitado=2, renta=200)
	
	self.assertEqual(respuesta, plan2)

    def test_Incluido_Plan1(self):
	plan1 = Plan( name='plan1', descripcion='super plan', ilimitado=1, renta=100)
	plan1.save()
	Iplan1 = Incluido_Plan(plan= Plan.objects.get(name = 'plan1'), tipo='mensajes', cantidad=300)
	Iplan1.save()
	respuesta = Incluido_Plan.objects.get(plan = Plan.objects.get(name = 'plan1'), tipo='mensajes', cantidad=300)
	
	self.assertEqual(respuesta, Iplan1)
	
    def test_Incluido_Plan2(self):	
	plan2 = Plan( name='plan2', descripcion='super plan2', ilimitado=2, renta=200)
	plan2.save()
	Iplan2 = Incluido_Plan(plan= Plan.objects.get(name = 'plan2'), tipo='mensajes', cantidad=300)
	Iplan2.save()
	respuesta = Incluido_Plan.objects.get(plan=Plan.objects.get(name = 'plan2'), tipo='mensajes', cantidad=300)
	
	self.assertEqual(respuesta, Iplan2)
	
    def test_Servicio1(self):
	serv1 = Servicio(name='servicio1', costo=20)
	serv1.save()
	respuesta = Servicio.objects.get(name='servicio1', costo=20)
	
	self.assertEqual(respuesta, serv1)
  
    def test_Servicio2(self):
	serv2 = Servicio(name='servicio2', costo=40)
	serv2.save()
	respuesta = Servicio.objects.get(name='servicio2', costo=40)
	
	self.assertEqual(respuesta, serv2)
	
    def test_Incluido_Servicio1(self):
	serv1 = Servicio(name='servicio1', costo=20)
	serv1.save()
	Iserv1 = Incluido_Servicio(servicio=Servicio.objects.get(name='servicio1'),tipo='llamadas',cantidad='10')
	Iserv1.save()
	respuesta = Incluido_Servicio.objects.get(servicio=Servicio.objects.get(name='servicio1'),tipo='llamadas',cantidad='10')
	
	self.assertEqual(respuesta, Iserv1)
 
    def test_Incluido_Servicio2(self):
	serv2 = Servicio(name='servicio2', costo=40)
	serv2.save()
	Iserv2 = Incluido_Servicio(servicio=Servicio.objects.get(name='servicio2'),tipo='mensajes',cantidad='10')
	Iserv2.save()
	respuesta = Incluido_Servicio.objects.get(servicio=Servicio.objects.get(name='servicio2'),tipo='mensajes',cantidad='10')
	
	self.assertEqual(respuesta, Iserv2) 
	
    def test_Producto1(self):
	cliente1 = Cliente(name='Pedro', direccion='La Trinidad', identificador='21348206')
	plan1 = Plan( name='plan1', descripcion='super plan', ilimitado=1, renta=100)
	cliente1.save()
	plan1.save()
	producto1 = Producto(cliente=Cliente.objects.get(name = 'Pedro'), plan=Plan.objects.get(name='plan1'), identificador= 0001, name='producto1', saldo=200)
	producto1.save()
	respuesta = Producto.objects.get(cliente=Cliente.objects.get(name = 'Pedro'), plan=Plan.objects.get(name='plan1'), identificador= 0001, name='producto1', saldo=200)
	
	self.assertEqual(respuesta, producto1) 
	
    def test_Producto2(self):
	cliente2 = Cliente(name='Juan', direccion='Baruta', identificador='22448206')
	plan2 = Plan( name='plan2', descripcion='super plan2', ilimitado=2, renta=200)
	cliente2.save()
	plan2.save()
	producto2 = Producto(cliente=Cliente.objects.get(name = 'Juan'), plan=Plan.objects.get(name='plan2'), identificador= 0002, name='producto2', saldo=200)
	producto2.save()
	respuesta = Producto.objects.get(cliente=Cliente.objects.get(name = 'Juan'), plan=Plan.objects.get(name='plan2'), identificador= 0002, name='producto2', saldo=200)
	
	self.assertEqual(respuesta, producto2) 
	
	
    def test_Adiciona1(self):
	cliente1 = Cliente(name='Pedro', direccion='La Trinidad', identificador='21348206')
	plan1 = Plan( name='plan1', descripcion='super plan', ilimitado=1, renta=100)
	cliente1.save()
	plan1.save()
	producto1 = Producto(cliente=Cliente.objects.get(name = 'Pedro'), plan=Plan.objects.get(name='plan1'), identificador= 0001, name='producto1', saldo=200)
	producto1.save()
	serv1 = Servicio(name='servicio1', costo=20)
	serv1.save()
	adiciona1 = Adiciona(producto = Producto.objects.get(identificador = 0001), servicio = Servicio.objects.get(name = 'servicio1'))
	adiciona1.save()
	respuesta = Adiciona.objects.get(producto = Producto.objects.get(identificador = 0001), servicio = Servicio.objects.get(name = 'servicio1'))
	
	self.assertEqual(respuesta, adiciona1)	
	
	
    def test_Adiciona2(self):
	cliente2 = Cliente(name='Juan', direccion='Baruta', identificador='21348206')
	plan2 = Plan( name='plan2', descripcion='super plan', ilimitado=1, renta=100)
	cliente2.save()
	plan2.save()
	producto2 = Producto(cliente=Cliente.objects.get(name = 'Juan'), plan=Plan.objects.get(name='plan2'), identificador= 0002, name='producto2', saldo=200)
	producto2.save()
	serv2 = Servicio(name='servicio2', costo=20)
	serv2.save()
	adiciona2 = Adiciona(producto = Producto.objects.get(identificador = 0002), servicio = Servicio.objects.get(name = 'servicio2'))
	adiciona2.save()
	respuesta = Adiciona.objects.get(producto = Producto.objects.get(identificador = 0002), servicio = Servicio.objects.get(name = 'servicio2'))
	
	self.assertEqual(respuesta, adiciona2)	
	
      
    def test_Consumo1(self):
	cliente1 = Cliente(name='Pedro', direccion='La Trinidad', identificador='21348206')
	plan1 = Plan( name='plan1', descripcion='super plan', ilimitado=1, renta=100)
	cliente1.save()
	plan1.save()
	producto1 = Producto(cliente=Cliente.objects.get(name = 'Pedro'), plan=Plan.objects.get(name='plan1'), identificador= 0001, name='producto1', saldo=200)
	producto1.save()
	consumo1 = Consumo(producto=Producto.objects.get(identificador = 0001), tipo='mensajes',mes=04,anio=2013,dia=22,hora='12.30',costo=200)
	consumo1.save()
	respuesta = Consumo.objects.get(producto=Producto.objects.get(identificador = 0001), tipo='mensajes',mes=04,anio=2013,dia=22,hora='12.30',costo=200)
	
	self.assertEqual(respuesta, consumo1)	
	
    def test_Consumo2(self):
	cliente2 = Cliente(name='Juan', direccion='Baruta', identificador='21348206')
	plan2 = Plan( name='plan2', descripcion='super plan', ilimitado=1, renta=100)
	cliente2.save()
	plan2.save()
	producto2 = Producto(cliente=Cliente.objects.get(name = 'Juan'), plan=Plan.objects.get(name='plan2'), identificador= 0002, name='producto2', saldo=200)
	producto2.save()
	consumo2 = Consumo(producto=Producto.objects.get(identificador = 0002), tipo='mensajes',mes=10,anio=2013,dia=10,hora='12.30',costo=200)
	consumo2.save()
	respuesta = Consumo.objects.get(producto=Producto.objects.get(identificador = 0002), tipo='mensajes',mes=10,anio=2013,dia=10,hora='12.30',costo=200)
	
	self.assertEqual(respuesta, consumo2)	
      
    def test_Factura1(self):
	cliente1 = Cliente(name='Juan', direccion='Baruta', identificador='21348206')
	cliente1.save()
	factura1= Factura(cliente = Cliente.objects.get(name='Juan'), monto = 2000, mes=10 , anio = 2013)
	factura1.save()
	respuesta = Factura.objects.get(cliente = Cliente.objects.get(name='Juan'), monto = 2000, mes= 10, anio = 2013)
	
	self.assertEqual(respuesta, factura1)
      
    def test_Factura2(self):
	cliente2 = Cliente(name='Pedro', direccion='La Trinidad', identificador='21348206')
	cliente2.save()
	factura2= Factura(cliente = Cliente.objects.get(name='Pedro'), monto = 2000, mes= 04, anio = 2013)
	factura2.save()
	respuesta = Factura.objects.get(cliente = Cliente.objects.get(name='Pedro'), monto = 2000, mes= 04, anio = 2013)
	
	self.assertEqual(respuesta, factura2)
	