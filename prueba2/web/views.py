from django.shortcuts import render

# Create your views here.
from .forms import CustonUserFrom
from web.models import producto
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import login,authenticate
from django.shortcuts import redirect

#rest_framework
from rest_framework import viewsets
from .serializers import productoSerializers



def Principal (request):
    print('ok,estamos en la vista mostrar alumnos')
    lista = producto.objects.filter(destacado =1)
    context={'listado':lista}
    return render(request,'web/Principal.html',context)
def Notebook (request):
    print('ok,estamos en la vista mostrar notebook')
    lista = producto.objects.filter(tipo ='n')
    context={'listado':lista}
    return render(request,'web/Notebook.html',context)

def celulares (request):
    print('ok,estamos en la vista mostrar celulares')
    lista = producto.objects.filter(tipo ='c')
    context = {'listado': lista}
    return render(request, 'web/celulares.html', context)
def Formulario (request):
    print("vista Formulario")
    context={}
    return render(request,'web/Formulario.html',context)

# INICIO DE METODOS SOLO PARA EL ADMIN
@login_required
@permission_required('core.add_producto')
def agregar_p (request):
    print("vista Formulario")
    context={}
    return render(request,'web/Agregar_producto.html',context)
@login_required
@permission_required('core.add_producto')
def agregar_produc (request):
    print("hola  estoy en agregar producto...")
    if request.method == 'POST':
        mi_marca = request.POST['marca']
        mi_codigo = request.POST['codigo']
        mi_modelo = request.POST['modelo']
        mi_descripcion = request.POST['descripcion']
        mi_precio = request.POST['precio']
        mi_Foto_producto_d = request.FILES['Foto_producto_d']
        mi_activo = request.POST['activo']
        mi_tipo = request.POST['tipo']
        mi_destacado = request.POST['destacado']

        if mi_codigo != "":
            try:
                Producto = producto()

                Producto.codigo = mi_codigo
                Producto.marca = mi_marca
                Producto.modelo = mi_modelo
                Producto.descripcion = mi_descripcion
                Producto.precio = mi_precio
                Producto.Foto_producto_d = mi_Foto_producto_d
                Producto.activo = mi_activo
                Producto.tipo = mi_tipo
                Producto.destacado = mi_destacado

                Producto.save()

                return render(request, 'web/Confir_crud/p_agregardo.html', {})

            except Producto.DoesNotExist:
                return render(request, 'web/error/error_204.html', {})
        else:
            return render(request, 'web/error/error_201.html', {})
    else:
        return render(request, 'web/error/error_203.html', {})
@login_required
@permission_required('core.add_producto')
def eliminar_p (request):
    print("vista eliminar_p")
    context={}
    return render(request,'web/eliminar_producto.html',context)
@login_required
@permission_required('core.add_producto')
def eliminar_porducto(request):
    print('-----------------------------------')
    print("hola  estoy en eliminar_por_rut...")
    print('-----------------------------------')
    if request.method == 'POST':
       mi_codigo = request.POST['codigo']

       if mi_codigo != "":
           try:
               Producto = producto()
               Producto = producto.objects.get(codigo = mi_codigo)
               if Producto is not None:
                   print("producto=", Producto)
                   Producto.delete()
                   return render(request, 'web/Confir_crud/p_eliminado.html',)
               else:
                   return render(request, 'web/error/error_204.html',{})
           except Producto.DoesNotExist:
               return render(request, 'web/error/error_202.html', {})
       else:
           return render(request, 'web/error/error_201.html', {})
    else:
        return render(request, 'web/error/error_203.html', {})
@login_required
@permission_required('core.add_producto')
def listado_producto (request):
    print('ok,')
    lista = producto.objects.all()
    context = {'listado': lista}
    return render(request, 'web/listar_p.html', context)
@login_required
@permission_required('core.add_producto')
def editar(request):
    print('----------------------------')
    print('ok,estamos en la vista editar')
    context={}
    return render(request,'web/buscar_Editar_p.html',context)

@login_required
@permission_required('core.add_producto')
def buscar_para_editar(request):
    print("hola  estoy en buscar_para_editar...")
    if request.method == 'POST':
       mi_codigo = request.POST['codigo']

       if mi_codigo != "":
           try:
               Producto = producto()
               Producto= producto.objects.get(codigo = mi_codigo)
               if Producto is not None:
                   print("producto=", Producto)
                   context={'producto':Producto}
                   return render(request, 'web/editar_producto.html', context)
               else:
                   return render(request, 'web/error/error_202.html',{})
           except Producto.DoesNotExist:
               return render(request, 'web/error/error_202.html', {})
       else:
           return render(request, 'web/error/error_201.html', {})
    else:
        return render(request, 'web/error/error_203.html', {})
@login_required
@permission_required('core.add_producto')
def actualizar_producto(request):
        print("hola  estoy en actualizar_alumno...")
        if request.method == 'POST':

            mi_id_producto_d = request.POST['id_producto_d']
            mi_marca = request.POST['marca']
            mi_codigo = request.POST['codigo']
            mi_modelo = request.POST['modelo']
            mi_descripcion = request.POST['descripcion']
            mi_precio = request.POST['precio']
            mi_Foto_producto_d = request.FILES['Foto_producto_d']
            mi_activo = request.POST['activo']
            mi_tipo = request.POST['tipo']
            mi_destacado = request.POST['destacado']

            if mi_codigo != "":
                try:
                    Producto = producto()

                    Producto.id_producto_d = mi_id_producto_d
                    Producto.codigo = mi_codigo
                    Producto.marca = mi_marca
                    Producto.modelo = mi_modelo
                    Producto.descripcion = mi_descripcion
                    Producto.precio = mi_precio
                    Producto.Foto_producto_d = mi_Foto_producto_d
                    Producto.activo = mi_activo
                    Producto.tipo = mi_tipo
                    Producto.destacado = mi_destacado

                    Producto.save()

                    return render(request, 'web/Confir_crud/p_actualizado.html', {})

                except Producto.DoesNotExist:
                    return render(request, 'web/error/error_204.html', {})
            else:
                return render(request, 'web/error/error_201.html', {})
        else:
            return render(request, 'web/error/error_203.html', {})


#registro de usuario 
def registro_usuario(request):
    data = {
        'form':CustonUserFrom()
    }
     
    if request.method == 'POST':
        Formulario = CustonUserFrom(request.POST)
        if Formulario.is_valid():
            Formulario.save()
            #autenticar al usuario y redirigirlo al inicio
            username = Formulario.cleaned_data['username']
            password = Formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='Principal')

    return render(request,'registration/registrar.html', data)

class productoViewset(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = productoSerializers