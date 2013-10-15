from Telefonia.models import Usuario,Cliente, Plan, Incluido_Plan, Servicio, Incluido_Servicio, Producto, Adiciona, Consumo, Factura
from django.http import HttpResponse
import datetime
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from auxiliar import facturarPostpago, facturarPrepago

#View que se encarga de verificar,crear la cuenta de usuario y redireccionar
def creacion_cuenta(request):
  #Reviso que no hayan dejado campos vacios
  if (('nombre' in request.POST) & ('clave' in request.POST)):
    #Reviso que el cliente no exista ya
    lista_usuarios=Usuario.objects.all()
    nombre=request.POST['nombre']
    clave=request.POST['clave']
    tipo=request.POST['tipo_usuario']
    usuario_temporal=Usuario(name=nombre, password=clave, tipo_usuario=tipo)
    if ((usuario_temporal not in lista_usuarios) & (nombre <> '') & (clave <> '')):
      usuario_temporal.save()
      return render (request, 'exitocreacioncuenta.html')
    else:
      return render (request, 'creacionerronea.html')
    
 
#Inicia la sesion del usuario si su info es correcta
def inicio_sesion(request):
  if (not(('nombre' in request.POST) & ('clave' in request.POST))):
    return render (request, 'inicioerroneo.html')
  nombre=request.POST['nombre']
  clave=request.POST['clave']
  coincidencias=Usuario.objects.filter(name=nombre, password=clave)
  
  #Veo si realmente existe ese usuario con esa clave
  if (len(coincidencias) > 0):
    usuario=Usuario.objects.get(name=nombre, password=clave)
    if (usuario.tipo_usuario == 'admin'):
      return render (request, 'inicioadmin.html')
    else:
      return render (request, 'iniciocliente.html')
  else:
    return render (request, 'inicioerroneo.html')
    
#Da acceso a la gestion de clientes
def gestion_clientes(request):
  return render (request, 'gestionclientes.html')

#Da acceso a la pagina de inicio del administrador
def inicio_admin(request):
   return render (request, 'inicioadmin.html')
  
#View que maneja la creacion de un nuevo cliente
def creacion_cliente(request):
  nombre=request.POST['nombre']
  direccion1=request.POST['direccion']
  identificador1=request.POST['identificador']
  #Falta verificar campos vacios
  
  #Verifico si el cliente ya existe
  lista_clientes=Cliente.objects.filter(name=nombre, identificador=identificador1)
  if (len(lista_clientes) == 0):
    #EL cliene no existe
    cliente=Cliente(name=nombre, direccion=direccion1, identificador=identificador1)
    cliente.save()
    return render (request, 'operacionexitosa.html')
  else:
    return render (request, 'creacionclientefalla.html')
    
def modificacion_cliente(request):
  identificador1=request.POST['identificador']
  campo=request.POST['campo_modificar']
  nuevo_valor=request.POST['modificado']
  
  #Revisamos si es un cliente que existe
  lista_clientes=Cliente.objects.filter(identificador=identificador1)
  if (len(lista_clientes) == 1):
    #El cliente existe
    cliente=Cliente.objects.get(identificador=identificador1)
    if (campo == 'direccion'):
      cliente.direccion=nuevo_valor
    else:
      cliente.name=nuevo_valor
    cliente.save()
    return render (request, 'operacionexitosa.html')
  else:
    return render (request, 'modificacionfalla.html')
    
def listar_clientes(request):
  clientes=Cliente.objects.all()
  return render (request, 'listadoclientes.html', { 'clientes' : clientes })

def insertar_planes(request):
  return render (request, 'insertarplanes.html')
  
def insercion_planes(request):
  nombre=request.POST['nombre']
  descripcion1=request.POST['descripcion']
  ilimitado1=request.POST['tipo_plan']
  renta1=request.POST['renta']
  boole= ((len(nombre) <> 0) & (len(descripcion1) <> 0) & (len(str(ilimitado1)) <> 0) & (len(str(renta1)) <> 0))
  
  
  tipo1=request.POST['tipo']
  cantidad1=request.POST['cantidad']
  boole22= ((len(str(cantidad1)) <> 0) & (len(tipo1) <> 0))
  
  tipo2=request.POST['tipo2']
  cantidad2=request.POST['cantidad2']
  boole2= ((len(str(cantidad2)) <> 0) & (len(tipo2) <> 0))
  
  tipo3=request.POST['tipo3']
  cantidad3=request.POST['cantidad3']
  boole3= ((len(str(cantidad3)) <> 0) & (len(tipo3) <> 0))
  
  tipo4=request.POST['tipo4']
  cantidad4=request.POST['cantidad4']
  boole4= ((len(str(cantidad4)) <> 0) & (len(tipo4) <> 0))
  
  tipo5=request.POST['tipo5']
  cantidad5=request.POST['cantidad5']
  boole5= ((len(str(cantidad5)) <> 0) & (len(tipo5) <> 0))
  
  tipo6=request.POST['tipo6']
  cantidad6=request.POST['cantidad6']
  boole6= ((len(str(cantidad6)) <> 0) & (len(tipo6) <> 0))
  
  if (boole):
    #Almaceno las instancias
    plan1=Plan(name=nombre, descripcion=descripcion1, ilimitado=int(ilimitado1), renta=int(renta1))
    plan1.save()
    plantemp=Plan.objects.get(name=nombre)
    
    if ((boole22) | (boole2) | (boole3) | (boole4) | (boole5) | (boole6)):
      
      if (boole22):
	incl1=Incluido_Plan(plan=plantemp, tipo=tipo1, cantidad=int(cantidad1))
	incl1.save()
      if (boole2):
	incl2=Incluido_Plan(plan=plantemp, tipo=tipo2, cantidad=int(cantidad2))
	incl2.save()
      if (boole3):
	incl3=Incluido_Plan(plan=plantemp, tipo=tipo3, cantidad=int(cantidad3))
	incl3.save()
      if (boole4):
	incl4=Incluido_Plan(plan=plantemp, tipo=tipo4, cantidad=int(cantidad4))
	incl4.save()
      if (boole5):
	incl5=Incluido_Plan(plan=plantemp, tipo=tipo5, cantidad=int(cantidad5))
	incl5.save()
      if (boole6):
	incl6=Incluido_Plan(plan=plantemp, tipo=tipo6, cantidad=int(cantidad6))
	incl6.save()
      elif (not(((boole22) | (boole2) | (boole3) | (boole4) | (boole5) | (boole6)))):
	return render (request, 'creacionplanfalla.html')
    else:
      return render (request, 'creacionplanfalla.html')
  else:
    return render (request, 'creacionplanfalla.html')
    
  return render (request, 'operacionexitosa.html')
  
  
def insertar_servicios(request):
  return render (request, 'insertarservicios.html')
  
def insercion_servicios(request):
  nombre=request.POST['nombre']
  costo1=request.POST['costo']
  decision=request.POST['incluye']
  boole=False
  boole1=False
  boole2=False
  boole3=False
  boole4=((len(nombre) == 0) | (len(costo1) == 0) | (len(decision) == 0))
  
  if ((boole4)):
    return render (request, 'falloservicio.html')
    
  costo1=int(request.POST['costo'])
  decision=int(request.POST['incluye'])
  if (decision == 1):
    
    boole=True
    tipo1=request.POST['tipo']
    cantidad1=request.POST['cantidad']
    if ((len(tipo1) <> 0) & (len(cantidad1) <> 0)):
      cantidad1=int(request.POST['cantidad'])
      boole1=True
    
    tipo2=request.POST['tipo2']
    cantidad2=request.POST['cantidad2']
    if ((len(tipo2) <> 0) & (len(cantidad2) <> 0)):
      cantidad2=int(request.POST['cantidad2'])
      boole2=True
   
    tipo3=request.POST['tipo3']
    cantidad3=request.POST['cantidad3']
    if ((len(tipo3) <> 0) & (len(cantidad3) <> 0)):
      cantidad3=int(request.POST['cantidad3'])
      boole3=True
  
  #Almaceno las instancias
  servicio1=Servicio(name=nombre, costo=costo1)
  servicio1.save()
  
  if (boole):
    servtemp=Servicio.objects.get(name=nombre)
    if (boole1):
      incl1=Incluido_Servicio(servicio=servtemp, tipo=tipo1, cantidad=cantidad1)
      incl1.save()
    elif (boole2):
      incl1=Incluido_Servicio(servicio=servtemp, tipo=tipo2, cantidad=cantidad2)
      incl1.save()
    elif (boole3):
      incl1=Incluido_Servicio(servicio=servtemp, tipo=tipo3, cantidad=cantidad3)
      incl1.save()
  
  return render (request, 'operacionexitosa.html')
  
def gestion_productos(request):
  return render (request, 'gestionproductos.html')
  
def creacion_producto(request):
  nombre=request.POST['nombreproducto']
  idproducto=request.POST['identificador']
  idcliente=request.POST['identificadorcliente']
  nombreplan=request.POST['nombreplan']
  
  #Verficiaciones:
  boole=((len(nombre) <> 0) & (len(idproducto) <> 0) & (len(idcliente) <> 0) & (len(nombreplan) <> 0))
  if (boole):
    clientes=Cliente.objects.filter(identificador=int(idcliente))
    if (len(clientes) == 1):
      #El cliente existe
      planes=Plan.objects.filter(name=nombreplan)
      if (len(planes) == 1):
	cliente1=Cliente.objects.get(identificador=int(idcliente))
	plan1=Plan.objects.get(name=nombreplan)
	producto=Producto(name=nombre, identificador=int(idproducto), cliente=cliente1, plan=plan1, saldo=0)
	producto.save()
	productos=Producto.objects.all()
	return render (request, 'operacionexitosa.html', { 'prods' : productos})
      else:
	return render (request, 'falloproducto.html')
    else:
      return render (request, 'falloproducto.html')
  else:
    return render (request, 'falloproducto.html')

    
def afiliar_servicio(request):
  idproducto=request.POST['idproducto']
  nombreserv=request.POST['nomservicio']

  boole= ((len(idproducto) <> 0) & (len(nombreserv) <> 0))
  if (boole):
    productos=Producto.objects.filter(identificador=int(idproducto))
    if (len(productos) == 1):
      #El producto existe
      servs=Servicio.objects.filter(name=nombreserv)
      if (len(servs) == 1):
	#Listo con verificaciones, puedo proceder
	producto1=Producto.objects.get(identificador=int(idproducto))
	servicio1=Servicio.objects.get(name=nombreserv)
	adiciona=Adiciona(producto=producto1, servicio=servicio1)
	adiciona.save()
	return render (request, 'operacionexitosa.html')
      else:
	return render (request, 'falloproductoserv.html')
    else:
      return render (request, 'falloproductoserv.html')
  else:
    return render (request, 'falloproductoserv.html')
    
def insertar_consumo(request):
  return render (request, 'insercionconsumos.html')

def insercionde_consumo(request):
  idproducto1=request.POST['idproducto']
  mes1=request.POST['mes']
  anio1=request.POST['anio']
  dia1=request.POST['dia']
  hora1=request.POST['hora']
  costo1=request.POST['costo']
  tipo1=request.POST['tipo']
  
  boole= ((len(idproducto1) <> 0) & (len(mes1) <> 0) & (len(anio1) <> 0) & (len(dia1) <> 0)) 
  boole2=  ((len(tipo1) <> 0) & (len(costo1) <> 0) & (len(hora1) <> 0))
  boole= ((boole) & (boole2))
  
  if (boole):
    producto=Producto.objects.filter(identificador=int(idproducto1))
    if (len(producto) > 0):
      #El producto existe
      producto1=Producto.objects.get(identificador=int(idproducto1))
      #Resto el saldo, debo restarlo solo si el producto es prepago
      if (producto1.plan.ilimitado == 2):
	producto1.saldo=producto1.saldo-int(costo1)
      consumo=Consumo(producto=producto1, mes=int(mes1), dia=int(dia1),hora=hora1, tipo=tipo1, anio=anio1, costo=int(costo1))
      consumo.save()
      producto1.save()
      return render (request, 'operacionexitosa.html')
    else:
      return render (request, 'falloconsumo.html')
  else:
    return render (request, 'falloconsumo.html')
    
def gestion_facturas(request):
  return render (request, 'facturas.html')

def facturar_cliente(request):
  idcliente1=request.POST['idcliente']
  mes1=request.POST['mes']
  anio1=request.POST['anio']
  tipofact1=request.POST['tipofact']
  lprods=[]
  
  #Verficiar campos vacioes
  boole= ((len(idcliente1) <>0) & (len(mes1) <> 0) & (len(anio1) <> 0))
  
  if (boole):
    #Verifico existencia del cliente
    clientes=Cliente.objects.filter(identificador=int(idcliente1))
    if (len(clientes) > 0):
      #Cliente existe:)
      #Llamar metodos dependiendo si es pre o post
      cliente1=Cliente.objects.get(identificador=int(idcliente1))
      if (tipofact1 == 'post'):
	montototal=facturarPostpago(cliente1,mes1,anio1)
	factura=Factura(cliente=cliente1, monto=montototal[0], mes=mes1, anio=anio1)
	lprods.append(montototal[1])
      else:
	montototal=facturarPrepago(cliente1)
	factura=Factura(cliente=cliente1, monto=montototal[0], mes=mes1, anio=anio1)
	lprods.append(montototal[1])
      factura.save()
      return render (request, 'exitofactura.html', { 'factura' : factura , 'lprods' : lprods })

def facturar_todo(request):
  mes1=request.POST['mes']
  anio1=request.POST['anio']
  tipofact1=request.POST['tipofact'] 
  lfacturas=[]
  clientes=Cliente.objects.all()
  for a in clientes:
    if (tipofact1 == 'post'):
      montototal=facturarPostpago(a,mes1,anio1)
      factura=Factura(cliente=a, monto=montototal[0], mes=mes1, anio=anio1)
      if (montototal[0]<>0):
	factura.save()
	lfacturas.append(factura)
    else:
      montototal=facturarPrepago(a)
      factura=Factura(cliente=a, monto=montototal, mes=mes1, anio=anio1)
      if (montototal <>0):
	factura.save()
	lfacturas.append(factura)
      
  
  return render (request, 'todasfacturas.html', { 'facts': lfacturas })
  
def consultar_ultfactura(request):
  cedrif=request.POST['cedrif']
  #Verficiar si esta vacio
  
  #Verifico que sea un cliente existente
  clientes=Cliente.objects.filter(identificador=int(cedrif))
  if (len(clientes) > 0):
    cliente=Cliente.objects.get(identificador=int(cedrif))
    facturas=cliente.facturas.all()
    #Verifico que el cliente tenga realmene facturas en el sistema
    if (len(facturas) > 0):
      maxanio=0
      maxmes=0
      #Obtengo el anioo/mes mas reciente de facturacion
      for a in facturas:
	if (a.anio >= maxanio):
	  maxanio=a.anio
	  if (a.mes >= maxmes):
	    maxmes=a.mes
	    
      #Una vez obtenido esto, retorno dicha factura
      factura_reciente=cliente.facturas.filter(anio=maxanio, mes=maxmes)
      factura_reciente=factura_reciente[0]
      return render (request, 'facturareciente.html', { 'factura': factura_reciente })
    else:
      pass
  else:
    pass
      
def inicio_cliente(request):
  return render (request, 'iniciocliente.html')
  
def consultar_saldo(request):
  cedrif=request.POST['cedrif']
  #Verificar si esta vacio
  
  #Verifico que sea un cliente existente
  clientes=Cliente.objects.filter(identificador=int(cedrif))
  if (len(clientes) > 0):
    cliente=Cliente.objects.get(identificador=int(cedrif))
    productos=cliente.productos.all()
    return render (request, 'consultasaldo.html', { 'productos' : productos })
  else:
    pass
    
    
  
  

      
      
    
    