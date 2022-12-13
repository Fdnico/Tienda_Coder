from django.shortcuts import render, redirect
from Tienda_Coder.forms import *
from Tienda_Coder.models import *
from django.contrib.auth.decorators import login_required


#--------------------------------------------------- PERIFERICOS ---------------------------------------------------#


def Vista_Perifericos(request):

    perifericos = Perifericos.objects.all()

    return render(request, '', {'listado_perifericos': perifericos})


def Ver_Periferico(request):

    if request.GET['nombre_periferico']:
        nombre = request.GET['nombre_periferico']
        periferico = Perifericos.objects.filter(nombre__icontains = nombre)

    return render(request, '')


def Crear_Periferico(request):

    errores = ''

    if request.method == 'POST':
        form = Perifericos_Form(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            periferico = Perifericos(nombre=data['nombre'], marca=data['marca'], precio=data['precio'])
            periferico.save()
        
        else:
            errores = form.errors

    form = Perifericos_Form()
    contexto = {'form': form, 'errores': errores}

    return render(request, '', contexto)


def Borrar_Periferico(request, id):

    periferico = Perifericos.objects.get(id=id)
    periferico.delete()

    return redirect('')


def Editar_Periferico(request, id):

    periferico = Perifericos.objects.get(id=id)

    if request.method == 'POST':
        form = Perifericos_Form(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            periferico.nombre = data['nombre']
            periferico.marca = data['marca']
            periferico.precio = data['precio']
            periferico.save()

            return redirect('')
        else:
            return render(request, '', {'form': form, 'errores': form.errors})
    else:
        form = Perifericos_Form(initial={'nombre': periferico.nombre, 'marca': periferico.marca, 'precio': periferico.precio})
        return render(request, '', {'form': form, 'errores': ''})


def Buscar_Periferico(request):
    
    return render(request, '')


def Resultado_Buscar_Periferico(request):

    if request.GET['nombre_periferico']:    
        nombre = request.GET['nombre_periferico'] 
        periferico = Perifericos.objects.filter(nombre__icontains = nombre)

        return render(request, '', {'periferico': periferico})

    else:
        rta = 'No enviaste datos!'
        return render(request, '', {'rta': rta})


#--------------------------------------------------- CONSOLAS ---------------------------------------------------#


def Vista_Consolas(request):

    consola = Consolas.objects.all()

    return render(request, '', {'listado_consolas': consola})


def Ver_Consola(request):

    if request.GET['nombre_consola']:
        nombre = request.GET['nombre_consola']
        consola = Consolas.objects.filter(nombre__icontains = nombre)

    return render(request, '')


def Crear_Consola(request):

    errores = ''

    if request.method == 'POST':
        form = Consolas_Form(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            consola = Consolas(nombre=data['nombre'], marca=data['marca'], precio=data['precio'])
            consola.save()
        
        else:
            errores = form.errors

    form = Consolas_Form()
    contexto = {'form': form, 'errores': errores}

    return render(request, '', contexto)


def Borrar_Consola(request, id):

    consola = Consolas.objects.get(id=id)
    consola.delete()

    return redirect('')


def Editar_Consola(request, id):

    consola = Consolas.objects.get(id=id)

    if request.method == 'POST':
        form = Consolas_Form(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            consola.nombre = data['nombre']
            consola.marca = data['marca']
            consola.precio = data['precio']
            consola.save()

            return redirect('')
        else:
            return render(request, '', {'form': form, 'errores': form.errors})
    else:
        form = Consolas_Form(initial={'nombre': consola.nombre, 'marca': consola.marca, 'precio': consola.precio})
        return render(request, '', {'form': form, 'errores': ''})


def Buscar_Consola(request):
    
    return render(request, '')


def Resultado_Buscar_Consola(request):

    if request.GET['nombre_consola']:    
        nombre = request.GET['nombre_consola'] 
        consola = Consolas.objects.filter(nombre__icontains = nombre)

        return render(request, '', {'consola': consola})

    else:
        rta = 'No enviaste datos!'
        return render(request, '', {'rta': rta})
        

#--------------------------------------------------- JUEGOS ---------------------------------------------------#


def Vista_Juegos(request):

    juego = Juegos.objects.all()

    return render(request, '', {'listado_juegos': juego})


def Ver_Juego(request):

    if request.GET['nombre_juego']:
        nombre = request.GET['nombre_juego']
        juego = Juegos.objects.filter(nombre__icontains = nombre)

    return render(request, '')


def Crear_Juego(request):

    errores = ''

    if request.method == 'POST':
        form = Juegos_Form(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            juego = Juegos(nombre=data['nombre'], precio=data['precio'])
            juego.save()
        
        else:
            errores = form.errors

    form = Juegos_Form()
    contexto = {'form': form, 'errores': errores}

    return render(request, '', contexto)


def Borrar_Juego(request, id):

    juego = Juegos.objects.get(id=id)
    juego.delete()

    return redirect('')


def Editar_Juego(request, id):

    juego = Juegos.objects.get(id=id)

    if request.method == 'POST':
        form = Juegos_Form(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            juego.nombre = data['nombre']
            juego.precio = data['precio']
            juego.save()

            return redirect('')
        else:
            return render(request, '', {'form': form, 'errores': form.errors})
    else:
        form = Juegos_Form(initial={'nombre': juego.nombre, 'precio': juego.precio})
        return render(request, '', {'form': form, 'errores': ''})


def Buscar_Juego(request):
    
    return render(request, '')


def Resultado_Buscar_Juego(request):

    if request.GET['nombre_juego']:    
        nombre = request.GET['nombre_juego'] 
        juego = Juegos.objects.filter(nombre__icontains = nombre)

        return render(request, '', {'juego': juego})

    else:
        rta = 'No enviaste datos!'
        return render(request, '', {'rta': rta})