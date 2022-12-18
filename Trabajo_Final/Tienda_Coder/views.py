from django.shortcuts import render, redirect
from Tienda_Coder.forms import *
from Tienda_Coder.models import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate





def acerca_de(request):
    if request.user.is_authenticated:
        if Avatar.objects.filter(user= request.user.id).order_by('-id'):
            imagen_model = Avatar.objects.filter(user= request.user.id).order_by('-id')[0]
            imagen_url = imagen_model.imagen.url
        else:
            imagen_url = ''
    else:
        imagen_url = '' 
    return render(request, 'Tienda_Coder/acerca_de.html', {'imagen_url': imagen_url})


def index(request):
    if request.user.is_authenticated:
        if Avatar.objects.filter(user= request.user.id).order_by('-id'):
            imagen_model = Avatar.objects.filter(user= request.user.id).order_by('-id')[0]
            imagen_url = imagen_model.imagen.url
        else:
            imagen_url = ''
    else:
        imagen_url = '' 
    return render(request, 'Tienda_Coder/index.html', {'imagen_url': imagen_url})


#--------------------------------------------------- PRODUCTOS ---------------------------------------------------#


def Resultado_Buscar_Producto(request):

    if request.GET['item']:
            
        producto = Perifericos.objects.filter(nombre__icontains = request.GET['item'])
        producto2 = Perifericos.objects.filter(marca__icontains = request.GET['item'])
        producto3 = Consolas.objects.filter(nombre__icontains = request.GET['item'])
        producto4 = Consolas.objects.filter(marca__icontains = request.GET['item'])
        producto5 = Juegos.objects.filter(nombre__icontains = request.GET['item'])

        if producto:    
            return render(request, 'Tienda_Coder/resultado_buscar_producto.html', {'producto': producto})
        elif producto2:
            producto = Perifericos.objects.filter(marca__icontains = request.GET['item'])
            return render(request, 'Tienda_Coder/resultado_buscar_producto.html', {'producto': producto})
        elif producto3:
            producto = Consolas.objects.filter(nombre__icontains = request.GET['item'])
            return render(request, 'Tienda_Coder/resultado_buscar_producto.html', {'producto': producto})
        elif producto4:
            producto = Consolas.objects.filter(marca__icontains = request.GET['item'])
            return render(request, 'Tienda_Coder/resultado_buscar_producto.html', {'producto': producto})
        elif producto5:
            producto = Juegos.objects.filter(nombre__icontains = request.GET['item'])
            return render(request, 'Tienda_Coder/resultado_buscar_producto.html', {'producto': producto})
        

    else:
        rta = 'No enviaste datos'
        return render(request, 'Tienda_Coder/resultado_buscar_producto.html', {'rta': rta})
        

#--------------------------------------------------- PERIFERICOS ---------------------------------------------------#


def Vista_Perifericos(request):

    perifericos = Perifericos.objects.all()

    for obj in Perifericos.objects.all():
        imagen = obj.imagen
        
    return render(request, 'Tienda_Coder/perifericos.html', {'listado_perifericos': perifericos, 'imagen': imagen})


def Ver_Periferico(request):

    if request.GET['nombre_periferico']:
        nombre = request.GET['nombre_periferico']
        periferico = Perifericos.objects.filter(nombre__icontains = nombre)

    return render(request, 'Tienda_Coder/periferico_ver.html')


@user_passes_test (lambda u: u.is_superuser)
def Crear_Periferico(request):

    if request.method == 'POST':
        form = Perifericos_Form(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            periferico = Perifericos(nombre=data['nombre'], marca=data['marca'], precio=data['precio'], imagen=data['imagen'])
            periferico.save()

            return redirect('perifericos')
        else:
            return render(request, 'Tienda_Coder/periferico_crear.html', {'form': form, 'errors': form.errors })

    form = Perifericos_Form()

    return render(request, 'Tienda_Coder/periferico_crear.html', {'form': form})


def Borrar_Periferico(request, id):

    periferico = Perifericos.objects.get(id=id)
    periferico.delete()

    return redirect('perifericos')


def Editar_Periferico(request, id):

    periferico = Perifericos.objects.get(id=id)

    if request.method == 'POST':
        form = Perifericos_Form(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            periferico.nombre = data['nombre']
            periferico.marca = data['marca']
            periferico.precio = data['precio']
            periferico.imagen = data['imagen']
            periferico.save()

            return redirect('perifericos')
        else:
            return render(request, 'Tienda_Coder/periferico_editar.html', {'form': form, 'errores': form.errors})
    else:
        form = Perifericos_Form(initial={'nombre': periferico.nombre, 'marca': periferico.marca, 'precio': periferico.precio, 'imagen': periferico.imagen})
        return render(request, 'Tienda_Coder/periferico_editar.html', {'form': form, 'errores': ''})


def Buscar_Periferico(request):
    
    return render(request, 'Tienda_Coder/periferico_buscar.html')


def Resultado_Buscar_Periferico(request):

    if request.GET['nombre_periferico']:    
        nombre = request.GET['nombre_periferico'] 
        periferico = Perifericos.objects.filter(nombre__icontains = nombre)

        return render(request, 'Tienda_Coder/periferico_resultado_buscar.html', {'periferico': periferico})

    else:
        rta = 'No enviaste datos!'
        return render(request, 'Tienda_Coder/periferico_resultado_buscar.html', {'rta': rta})


#--------------------------------------------------- CONSOLAS ---------------------------------------------------#


def Vista_Consolas(request):

    consolas = Consolas.objects.all()
    
    for obj in Consolas.objects.all():
        imagen = obj.imagen
        
    return render(request, 'Tienda_Coder/consolas.html', {'listado_consolas': consolas, 'imagen': imagen})


def Ver_Consola(request):

    if request.GET['nombre_consola']:
        nombre = request.GET['nombre_consola']
        consola = Consolas.objects.filter(nombre__icontains = nombre)

    return render(request, 'Tienda_Coder/consola_ver.html')


def Crear_Consola(request):

    if request.method == 'POST':
        form = Consolas_Form(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            consola = Consolas(nombre=data['nombre'], marca=data['marca'], precio=data['precio'], imagen=data['imagen'])
            consola.save()

            return redirect('consolas')
        else:
            return render(request, 'Tienda_Coder/consola_crear.html', {'form': form, 'errors': form.errors })

    form = Consolas_Form()

    return render(request, 'Tienda_Coder/consola_crear.html', {'form': form})


def Borrar_Consola(request, id):

    consola = Consolas.objects.get(id=id)
    consola.delete()

    return redirect('consolas')


def Editar_Consola(request, id):

    consola = Consolas.objects.get(id=id)

    if request.method == 'POST':
        form = Consolas_Form(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            consola.nombre = data['nombre']
            consola.marca = data['marca']
            consola.precio = data['precio']
            consola.imagen = data['imagen']
            consola.save()

            return redirect('consolas')
        else:
            return render(request, 'Tienda_Coder/consola_editar.html', {'form': form, 'errores': form.errors})
    else:
        form = Consolas_Form(initial={'nombre': consola.nombre, 'marca': consola.marca, 'precio': consola.precio, 'imagen': consola.imagen})
        return render(request, 'Tienda_Coder/consola_editar.html', {'form': form, 'errores': ''})


def Buscar_Consola(request):
    
    return render(request, 'Tienda_Coder/consola_buscar.html')


def Resultado_Buscar_Consola(request):

    if request.GET['nombre_consola']:    
        nombre = request.GET['nombre_consola'] 
        consola = Consolas.objects.filter(nombre__icontains = nombre)

        return render(request, 'Tienda_Coder/consola_resultado_buscar.html', {'consola': consola})

    else:
        rta = 'No enviaste datos!'
        return render(request, 'Tienda_Coder/consola_resultado_buscar.html', {'rta': rta})
        

#--------------------------------------------------- JUEGOS ---------------------------------------------------#


def Vista_Juegos(request):

    juegos = Juegos.objects.all()

    if juegos:
        for obj in Juegos.objects.all():
            imagen = obj.imagen
        
        contexto = {'listado_juegos': juegos, 'imagen': imagen}
    else:
        contexto = {'listado_juegos': juegos}
        
    return render(request, 'Tienda_Coder/juegos.html', contexto)


def Ver_Juego(request):

    if request.GET['nombre_juego']:
        nombre = request.GET['nombre_juego']
        juego = Juegos.objects.filter(nombre__icontains = nombre)

    return render(request, 'Tienda_Coder/juego_ver.html')


def Crear_Juego(request):

    if request.method == 'POST':
        form = Juegos_Form(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            juego = Juegos(nombre=data['nombre'], precio=data['precio'], imagen=data['imagen'])
            juego.save()

            return redirect('juegos')
        else:
            return render(request, 'Tienda_Coder/juego_crear.html', {'form': form, 'errors': form.errors })

    form = Juegos_Form()

    return render(request, 'Tienda_Coder/juego_crear.html', {'form': form})


def Borrar_Juego(request, id):

    juego = Juegos.objects.get(id=id)
    juego.delete()

    return redirect('juegos')


def Editar_Juego(request, id):

    juego = Juegos.objects.get(id=id)

    if request.method == 'POST':
        form = Juegos_Form(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            juego.nombre = data['nombre']
            juego.precio = data['precio']
            juego.imagen = data['imagen']
            juego.save()

            return redirect('juegos')
        else:
            return render(request, 'Tienda_Coder/juego_editar.html', {'form': form, 'errores': form.errors})
    else:
        form = Juegos_Form(initial={'nombre': juego.nombre, 'precio': juego.precio, 'imagen': juego.imagen})
        return render(request, 'Tienda_Coder/juego_editar.html', {'form': form, 'errores': ''})


def Buscar_Juego(request):
    
    return render(request, 'Tienda_Coder/juego_buscar.html')


def Resultado_Buscar_Juego(request):

    if request.GET['nombre_juego']:    
        nombre = request.GET['nombre_juego'] 
        juego = Juegos.objects.filter(nombre__icontains = nombre)

        return render(request, 'Tienda_Coder/juego_resultado_buscar.html', {'juego': juego})

    else:
        rta = 'No enviaste datos!'
        return render(request, 'Tienda_Coder/juego_resultado_buscar.html', {'rta': rta})

#--------------------------------------------------- USUARIOS ---------------------------------------------------#


def Iniciar_Sesion(request):

    errors = ''
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(username=data['username'], password=data['password'])

            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                return render(request, 'Tienda_Coder/login.html', {'form': form, 'errors': 'Credenciales Invalidas'})
        
        else:
            return render(request, 'Tienda_Coder/login.html', {'form': form, 'errors': form.errors})

    form = AuthenticationForm()
    return render(request, 'Tienda_Coder/login.html', {'form': form})


def Registrar_Usuario(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('inicio')
        else:
            return render(request, 'Tienda_Coder/register.html', {'form': form, 'errors': form.errors})

    form = UserRegisterForm()
    return render(request, 'Tienda_Coder/register.html', {'form': form})


def Editar_Perfil(request):

    usuario = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data

            usuario.email = data['email']
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']

            usuario.save()
            return redirect('inicio')
        else:
            return render(request, 'Tienda_Coder/editar_perfil.html', {'form': form, 'errors': form.errors})
    
    else:
        form = UserEditForm(initial = {'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
        
    return render(request, 'Tienda_Coder/editar_perfil.html', {'form': form})


def Agregar_Avatar(request):
    
    if request.method == 'POST':
        form = AvatarForm(request.POST, files=request.FILES)
        print(request.FILES, request.POST)
        if form.is_valid():
            data = form.cleaned_data

            usuario = request.user

            avatar = Avatar(user=usuario, imagen=data['imagen'])
            avatar.save()

            return redirect('inicio')
        else:
            return render(request, 'Tienda_Coder/agregar_avatar.html', {'form': form, 'errors': form.errors })
    form = AvatarForm()

    return render(request, 'Tienda_Coder/agregar_avatar.html', {'form': form})



def Vista_Comentarios(request):

    comentario = Comentarios.objects.all()

    return render(request, 'Tienda_Coder/index.html', {'listado_comentarios': comentario})


def Comentario(request):

    usuario = request.user.username

    if Avatar.objects.filter(user= request.user.id).order_by('-id'):
        imagen_model = Avatar.objects.filter(user= request.user.id).order_by('-id')[0]
        imagen_url = imagen_model.imagen.url
    else:
        imagen_url = ''

    if request.method == 'POST':
        form = Comentar_Form(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            comentario = Comentarios(comentario=data['comentario'], usuario=usuario, imagen=imagen_url)
            comentario.save()

    form = Comentar_Form()

    return render(request, 'Tienda_Coder/comentar.html', {'form': form})

    
def mostrar_perfil(request):
    if request.user.is_authenticated:
        if Avatar.objects.filter(user= request.user.id).order_by('-id'):
            imagen_model = Avatar.objects.filter(user= request.user.id).order_by('-id')[0]
            imagen_url = imagen_model.imagen.url
        else:
            imagen_url = ''
    else:
        imagen_url = '' 
    return render(request, 'Tienda_Coder/Perfil.html', {'imagen_url': imagen_url})