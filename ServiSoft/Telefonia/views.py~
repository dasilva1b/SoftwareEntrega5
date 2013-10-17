from Telefonia.models import Usuario,Cliente, Plan, Incluido_Plan, Servicio, Incluido_Servicio, Producto, Adiciona, Consumo, Factura
from django.http import HttpResponse
import datetime
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from auxiliar import facturarPostpago, facturarPrepago

#Aca estan las vistas, quienes manejaran los requests/formularios, procesaran l
#rediccionaran a donde sea pertinente.

#View que se encarga de verificar,crear la cuenta de usuario y redireccionar
def creacion_cuenta(request):
    nombre=request.POST['nombre']
    clave=request.POST['clave']
    tipo=request.POST['tipo_usuario']

    #Reviso que no hayan dejado campos vacios
    boole= ((len(nombre) <> 0) & (len(clave) <> 0) & (len(tipo) <> 0))
    if (boole):
       #Reviso que el cliente no exista ya
      lista_usuarios=Usuario.objects.filter(name=nombre, password=clave, tipo_usuario=tipo)
      if (len(lista_usuarios) == 0):
	#El usuario no existe
	usuario_temporal=Usuario(name=nombre, password=clave, tipo_usuario=tipo)
	usuario_temporal.save()
	return render (request, 'exitocreacioncuenta.html')
      else:
	return render (request, 'creacionerronea.html')
    else:
      return render (request, 'creacionerroneavacios.html')

	
 
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
  
  #Reviso que no hayan dejado campos vacios
  boole= ((len(nombre) <> 0) & (len(direccion1) <> 0) & (len (str(identificador1)) <> 0))
  if (boole):
    #Verifico si el cliente ya existe
    lista_clientes=Cliente.objects.filter(name=nombre, identificador=identificador1)
    if (len(lista_clientes) == 0):
      #EL cliene no existe
      cliente=Cliente(name=nombre, direccion=direccion1, identificador=identificador1)
      cliente.save()
      return render (request, 'operacionexitosa.html')
    else:
      return render (request, 'creacionclientefalla.html')
  else:
      return render (request, 'creacionclientefallavacios.html')
  
  
  
#View que maneja el request de modificar la informacion de un cliente.
def modificacion_cliente(request):
  identificador1=request.POST['identificador']
  campo=request.POST['campo_modificar']
  nuevo_valor=request.POST['modificado']
  
  #Revisamos que no hayan campos vacios
  boole = ((len(str(identificador1)) <> 0) & (len(campo) <> 0) & (len(nuevo_valor) <> 0))
  if (boole):
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
  else:
    return render (request, 'modificacionfalla.html')
    
    
#View que lista los clientes que esten almacenados en sistema
def listar_clientes(request):
  clientes=Cliente.objects.all()
  return render (request, 'listadoclientes.html', { 'clientes' : clientes })

  
  
#View que da acceso a la pagina donde se provee la informacion para insertar un plan.
def insertar_planes(request):
  return render (request, 'insertarplanes.html')

  
  
#View que realmente hace el procesamiento para insertar un plan en el sistema.
def insercion_planes(request):
  nombre=request.POST['nombre']
  descripcion1=request.POST['descripcion']
  ilimitado1=request.POST['tipo_plan']
  renta1=request.POST['renta']
  
  #Se revisa que no hayan campos vacios.
  boole= ((len(nombre) <> 0) & (len(descripcion1) <> 0) & (len(str(ilimitado1)) <> 0) & (len(str(renta1)) <> 0))
  
  
  #Se revisa para cada par (tipo,incluido) que se hayan especificado
  #correctamente (que no esten vacios)
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
  
  
  
  #Si los campos no son vacios
  if (boole):
    #verificar que no exista
    lista_planes = Plan.objects.filter(name=nombre)
    if (len(lista_planes) == 0):
      #Almaceno las instancias
      plan1=Plan(name=nombre, descripcion=descripcion1, ilimitado=int(ilimitado1), renta=int(renta1))
      plan1.save()
      plantemp=Plan.objects.get(name=nombre)
    else: 
      return render (request, 'planexistente.html')
      
    #Reviso que se haya especificado algun tipo,cantidad de lo que se incluye en el plan
    #y de ser asi, almaceno en el sistema
    if ((boole22) | (boole2) | (boole3) | (boole4) | (boole5) | (boole6)):
      
      if (boole22):
	incl1=Incluido_Plan(plan=plantemp, tipo=tipo1, cantidad=int(cantidad1))
	incl1.save()
      if (boole2):
	# De aca en adelante se verifica que no se agregue mas de una vez lo que incluye el plan
	lista_incluido = Incluido_Plan.objects.filter(plan=plantemp, tipo=tipo2)
	if (len(lista_incluido) == 0):
	  incl2=Incluido_Plan(plan=plantemp, tipo=tipo2, cantidad=int(cantidad2))
	  incl2.save()
	else:
	  plan1.delete()
	  return render (request, 'incluirplanfalla.html')
      if (boole3):
	lista_incluido2 = Incluido_Plan.objects.filter(plan=plantemp, tipo=tipo2)
	if (len(lista_incluido2) == 0):
	  incl3=Incluido_Plan(plan=plantemp, tipo=tipo3, cantidad=int(cantidad3))
	  incl3.save()
	else:
	  plan1.delete()
	  return render (request, 'incluirplanfalla.html')
      if (boole4):
	lista_incluido3 = Incluido_Plan.objects.filter(plan=plantemp, tipo=tipo2)
	if (len(lista_incluido3) == 0):
	  incl4=Incluido_Plan(plan=plantemp, tipo=tipo4, cantidad=int(cantidad4))
	  incl4.save()
	else:
	  plan1.delete()
	  return render (request, 'incluirplanfalla.html')
      if (boole5):
	lista_incluido4 = Incluido_Plan.objects.filter(plan=plantemp, tipo=tipo2)
	if (len(lista_incluido4) == 0):
	  incl5=Incluido_Plan(plan=plantemp, tipo=tipo5, cantidad=int(cantidad5))
	  incl5.save()
	else:
	  plan1.delete()
	  return render (request, 'incluirplanfalla.html')
      if (boole6):
	plan1.delete()
	lista_incluido5 = Incluido_Plan.objects.filter(plan=plantemp, tipo=tipo2)
	if (len(lista_incluido5) == 0):
	  incl6=Incluido_Plan(plan=plantemp, tipo=tipo6, cantidad=int(cantidad6))
	  incl6.save()
	else:
	  return render (request, 'incluirplanfalla.html')
      elif (not(((boole22) | (boole2) | (boole3) | (boole4) | (boole5) | (boole6)))):
	return render (request, 'creacionplanfalla.html')
    else:
      return render (request, 'creacionplanfalla.html')
  else:
    return render (request, 'creacionplanfalla.html')
    
  return render (request, 'operacionexitosa.html')
  
  
  
#Da acceso a la pagina donde se provee informacion para insertar un servicio al sistema. 
def insertar_servicios(request):
  return render (request, 'insertarservicios.html')
 
 
 
#View que realmente procesa y almacena un servicio en el sistema.Analoga a insercion_plan
def insercion_servicios(request):
  nombre=request.POST['nombre']
  costo1=request.POST['costo']
  decision=request.POST['incluye']
  boole=False
  boole1=False
  boole2=False
  boole3=False
  
  #Reviso campos vacios
  boole4=((len(nombre) == 0) | (len(costo1) == 0) | (len(decision) == 0))
  
  #Si los campos estan vacios, redirecciono a pagina de error.
  if ((boole4)):
    return render (request, 'falloservicio.html')
    
  costo1=int(request.POST['costo'])
  decision=int(request.POST['incluye'])
  
  #Si el servicio incluye algo, verifico lo que se especifico
  #y almaceno en sistema en caso de que se haya validado.
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
  
  #verificar si el servicio ya existe
  lista_servicios = Servicio.objects.filter(name=nombre)
  if (len(lista_servicios) == 0):
    #Almaceno las instancias
    servicio1=Servicio(name=nombre, costo=costo1)
    servicio1.save()
  else:
    return render (request, 'servicioexiste.html')
    
  #Almaceno las instancias de incluidos, en caso de que la validacion
  #sea correcta.
  if (boole):
    servtemp=Servicio.objects.get(name=nombre)
    if (boole1):
      incl1=Incluido_Servicio(servicio=servtemp, tipo=tipo1, cantidad=cantidad1)
      incl1.save()
    if (boole2):
      lista_incluidoserv2 = Incluido_Servicio.objects.filter(servicio=servtemp, tipo=tipo2)
      if (len(lista_incluidoserv2) == 0):
	incl2=Incluido_Servicio(servicio=servtemp, tipo=tipo2, cantidad=cantidad2)
	incl2.save()
      else:
	servicio1.delete()
	return render (request, 'serviciorepetidofalla.html')
    if (boole3):
      lista_incluidoserv3 = Incluido_Servicio.objects.filter(servicio=servtemp, tipo=tipo3)
      if (len(lista_incluidoserv3) == 0):
	incl3=Incluido_Servicio(servicio=servtemp, tipo=tipo3, cantidad=cantidad3)
	incl3.save()
      else:
	servicio1.delete()
	return render (request, 'serviciorepetidofalla.html')
  
  return render (request, 'operacionexitosa.html')
 
 
 
#Da acceso a la pagina de inicio para gestionar productos
def gestion_productos(request):
  return render (request, 'gestionproductos.html')

  
  
#View que se encarga de procesar la solicitud de crear un nuevo producto
def creacion_producto(request):
  nombre=request.POST['nombreproducto']
  idproducto=request.POST['identificador']
  idcliente=request.POST['identificadorcliente']
  nombreplan=request.POST['nombreplan']
  
  #Verficiaciones de campos vacios:
  boole=((len(nombre) <> 0) & (len(idproducto) <> 0) & (len(idcliente) <> 0) & (len(nombreplan) <> 0))
  if (boole):
    clientes=Cliente.objects.filter(identificador=int(idcliente))
    if (len(clientes) == 1):
      #El cliente existe
      planes=Plan.objects.filter(name=nombreplan)
      #Verifico que se este asociando el producto a un plan verdader, de ser
      #asi, almaceno.
      if (len(planes) == 1):
        cliente1=Cliente.objects.get(identificador=int(idcliente))
        plan1=Plan.objects.get(name=nombreplan)
        
        lista_producto = Producto.objects.filter(identificador=int(idproducto))
        if (len(lista_producto) == 0):
	  #El producto no existe
	  producto=Producto(name=nombre, identificador=int(idproducto), cliente=cliente1, plan=plan1, saldo=0)
	  producto.save()
	  productos=Producto.objects.all()
	else:
	  return render (request, 'productoexiste.html')
	  
        return render (request, 'operacionexitosa.html', { 'prods' : productos})
      else:
        return render (request, 'falloproducto.html')
    else:
      return render (request, 'falloproducto.html')
  else:
    return render (request, 'falloproducto.html')
    
    
      
#View que  procesa el request de afiliar un producto a un servicio
def afiliar_servicio(request):
  idproducto=request.POST['idproducto']
  nombreserv=request.POST['nomservicio']
  
  #Verificaciones de campos vacios
  boole= ((len(idproducto) <> 0) & (len(nombreserv) <> 0))
  if (boole):
    productos=Producto.objects.filter(identificador=int(idproducto))
    if (len(productos) == 1):
      #El producto existe
      servs=Servicio.objects.filter(name=nombreserv)
      #Verifico que el servicio al que se desea afiliar realmente existe.
      if (len(servs) == 1):
	#Listo con verificaciones, puedo proceder
	producto1=Producto.objects.get(identificador=int(idproducto))
	servicio1=Servicio.objects.get(name=nombreserv)
	
	lista_adiciona = Adiciona.objects.filter(producto=producto1, servicio=servicio1)
	if (len(lista_adiciona) == 0):
	  adiciona=Adiciona(producto=producto1, servicio=servicio1)
	  adiciona.save()
	else:
	  return render (request, 'adicionaexiste.html')
	return render (request, 'operacionexitosa.html')
      else:
	return render (request, 'falloproductoserv.html')
    else:
      return render (request, 'falloproductoserv.html')
  else:
    return render (request, 'falloproductoserv.html')
  
  
  
#Da acceso a la pagina para insertar consumos al sistema.
def insertar_consumo(request):
  return render (request, 'insercionconsumos.html')

  
  
#Procesa el request/form para agregar un consumo al sistema.
def insercionde_consumo(request):
  idproducto1=request.POST['idproducto']
  mes1=request.POST['mes']
  anio1=request.POST['anio']
  dia1=request.POST['dia']
  hora1=request.POST['hora']
  costo1=request.POST['costo']
  tipo1=request.POST['tipo']
  
  #Verificaciones de campos vacios
  boole= ((len(idproducto1) <> 0) & (len(mes1) <> 0) & (len(anio1) <> 0) & (len(dia1) <> 0)) 
  boole2=  ((len(tipo1) <> 0) & (len(costo1) <> 0) & (len(hora1) <> 0))
  boole= ((boole) & (boole2))
  
  #Si la validacion es correcta, verifico que el producto exista,
  #de ser asi, agrego el consumo y resto el saldo si se trata de un producto
  #prepago.
  if (boole):
    producto=Producto.objects.filter(identificador=int(idproducto1))
    if (len(producto) > 0):
      #El producto existe
      producto1=Producto.objects.get(identificador=int(idproducto1))
      #Resto el saldo, debo restarlo solo si el producto es prepago
      if (producto1.plan.ilimitado == 2):
	producto1.saldo=producto1.saldo-int(costo1)
      lista_consumo = Consumo.objects.filter(producto=producto1, mes=int(mes1), dia=int(dia1),hora=hora1, tipo=tipo1, anio=anio1)
      if (len(lista_consumo) == 0):
	consumo=Consumo(producto=producto1, mes=int(mes1), dia=int(dia1),hora=hora1, tipo=tipo1, anio=anio1, costo=int(costo1))
	consumo.save()
	producto1.save()
      else:
	return render (request, 'consumoexiste.html' )
      return render (request, 'operacionexitosa.html')
    else:
      return render (request, 'falloconsumo.html')
  else:
    return render (request, 'falloconsumo.html')

    
    
#Da acceso a la pagina de inicio para gestionar facturas en el sistema
def gestion_facturas(request):
  return render (request, 'facturas.html')

  
  
#View que maneja el request de facturar a un cliente en particular
def facturar_cliente(request):
  idcliente1=request.POST['idcliente']
  mes1=request.POST['mes']
  anio1=request.POST['anio']
  tipofact1=request.POST['tipofact']
  lprods=[]
  
  #Verficiar campos vacios
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
      lista_factura = Factura.objects.filter(cliente=cliente1, monto=montototal[0], mes=mes1, anio=anio1)
      if (len(lista_factura) == 0):	
	factura.save()
      
      #Retornamos al template la factura emitida y los productos para la que se emitio
      return render (request, 'exitofactura.html', { 'factura' : factura , 'lprods' : lprods })

      
      
#Procesa el request de facturar TODOS los clientes de un tipo (pre-post)
#para un periodo dado.
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
      factura=Factura(cliente=a, monto=montototal[0], mes=mes1, anio=anio1)
      if (montototal[0] <>0):
	factura.save()
	lfacturas.append(factura)
      
  
  return render (request, 'todasfacturas.html', { 'facts': lfacturas })
 
 
 
#View que procesa el request de un cliente de consultar su ultima factura
def consultar_ultfactura(request):
  cedrif=request.POST['cedrif']
  #Verficiar si esta vacio
  
  boole=  ((len(cedrif) <> 0))
  if (boole):
    
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
	      
	#Una vez obtenido esto, retorno dicha factura para ser imprimida en el template
	factura_reciente=cliente.facturas.filter(anio=maxanio, mes=maxmes)
	factura_reciente=factura_reciente[0]
	return render (request, 'facturareciente.html', { 'factura': factura_reciente })
      else:
	pass
    else:
      pass
  else:
    return render (request, 'consultarfalla.html')
 
 
 
#Redireciona a la pagina de inicio para clientes
def inicio_cliente(request):
  return render (request, 'iniciocliente.html')

  
  
#Procesa el request de consultar saldo de sus productos
#de un cliente prepago.
def consultar_saldo(request):
  cedrif=request.POST['cedrif']
  #Verificar si esta vacio
  boole=  ((len(cedrif) <> 0))
  if (boole):
    #Verifico que sea un cliente existente, de ser asi,
    #devuelvo lo necesario para que el template pueda
    #imprimir lo consultado
    clientes=Cliente.objects.filter(identificador=int(cedrif))
    if (len(clientes) > 0):
      cliente=Cliente.objects.get(identificador=int(cedrif))
      productos=cliente.productos.all()
      return render (request, 'consultasaldo.html', { 'productos' : productos })
    else:
      pass
  else:
    return render (request, 'consultarfalla.html')
    
  
  

      
      
    
    