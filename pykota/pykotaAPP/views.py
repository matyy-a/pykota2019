from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth.models import User
from .filters import userpquotaFilter

@login_required
def index (request):
	return render (request, 'pykota/index.html')

@login_required
def impresora_lista (request):
	impresoras = printers.objects.all
	if request.method == "POST":
		form = printersForm(request.POST)
		if form.is_valid():
			impresora = form.save(commit=False)
			impresora.save()
			messages.success(request,'Impresora añadida correctamente')
			return redirect('impresora_lista',)
	else:
		form = printersForm()
	return render (request, 'pykota/impresora_lista.html', {'impresoras': impresoras, 'form': form})

@login_required
def impresora_editar(request, pk):
	impresora = get_object_or_404(printers, pk=pk)
	if request.method == "POST":
		form = printersForm(request.POST, instance=impresora)
		if form.is_valid():
			impresora = form.save(commit=False)
			impresora.save()
			return redirect('impresora_lista')
	else:
		form = printersForm(instance=impresora)
	return render(request, 'pykota/impresora_editar.html', {'form': form})

@login_required
def impresora_borrar (request, pk):
	impresora = get_object_or_404(printers, pk=pk)
	messages.info(request,'Se ha eliminado correctamente')
	impresora.delete()
	return redirect ('impresora_lista')

@login_required
def grupo_lista (request):
	grupos = groups.objects.all
	if request.method == "POST":
		form = groupsForm(request.POST)
		if form.is_valid():
			grupo = form.save(commit=False)
			grupo.save()
			messages.success(request,'Grupo añadido correctamente')
			return redirect('grupo_lista',)
	else:
		form = groupsForm()
	return render (request, 'pykota/grupo_lista.html', {'grupos': grupos, 'form': form})

@login_required
def grupo_editar(request, pk):
	grupo = get_object_or_404(groups, pk=pk)
	if request.method == "POST":
		form = groupsForm(request.POST, instance=grupo)
		if form.is_valid():
			grupo = form.save(commit=False)
			grupo.save()
			return redirect('grupo_lista')
	else:
		form = groupsForm(instance=grupo)
	return render(request, 'pykota/grupo_editar.html', {'form': form})

@login_required
def grupo_borrar (request, pk):
	grupo = get_object_or_404(groups, pk=pk)
	messages.info(request,'Se ha eliminado correctamente')
	grupo.delete()
	return redirect ('grupo_lista')


@login_required
def grupousuario_lista (request):
	grupousuarios = groupsmembers.objects.all
	if request.method == "POST":
		form = groupsmembersForm(request.POST)
		if form.is_valid():
			grupousuario = form.save(commit=False)
			grupousuario.save()
			messages.success(request,'Se ha asignado correctamente')
			return redirect('grupo-usuario_lista',)
	else:
		form = groupsmembersForm()
	return render (request, 'pykota/grupo-usuario_lista.html', {'grupousuarios': grupousuarios, 'form': form})

@login_required
def grupousuario_editar(request, pk):
	grupousuario = get_object_or_404(groupsmembers, pk=pk)
	if request.method == "POST":
		form = groupsmembersForm(request.POST, instance=grupousuario)
		if form.is_valid():
			grupousuario = form.save(commit=False)
			grupousuario.save()
			return redirect('grupousuario_lista')
	else:
		form = groupsmembersForm(instance=grupousuario)
	return render(request, 'pykota/grupo-usuario_editar.html', {'form': form})

@login_required
def grupousuario_borrar (request, pk):
	grupousuario = get_object_or_404(groupsmembers, pk=pk)
	messages.info(request,'Se ha eliminado correctamente')
	grupousuario.delete()
	return redirect ('grupousuario_lista')


@login_required
def usuario_lista (request):
	usuarios = users.objects.all
	if request.method == "POST":
		form = usersForm(request.POST)
		if form.is_valid():
			usuarios = form.save(commit=False)
			usuarios.save()
			form.save_m2m()
			messages.success(request,'Usuario añadido correctamente')
			return redirect('usuario_lista',)
	else:
		form = usersForm()

	return render (request, 'pykota/usuario_lista.html', {'usuarios': usuarios, 'form': form})


@login_required
def usuario_editar (request, pk):
	usuario = get_object_or_404(users, pk=pk)
	if request.method == "POST":
		form = usersForm(request.POST, instance=usuario)
		if form.is_valid():
			usuarios = form.save(commit=False)
			usuarios.save()
			form.save_m2m()
			return redirect('usuario_lista',)
	else:
		form = usersForm(instance=usuario)

	return render (request, 'pykota/usuario_editar.html', {'form': form})

@login_required
def usuario_borrar (request, pk):
	usuario = get_object_or_404(users, pk=pk)
	messages.info(request,'El usuario se ha eliminado correctamente')
	usuario.delete()
	return redirect('usuario_lista')

@login_required
def asignarcuota_lista (request):
	f = userpquotaFilter(request.GET, queryset=userpquota.objects.all())
	if request.method == "POST":
		form = userpquotaForm(request.POST)
		if form.is_valid():
			asignarcuota = form.save(commit=False)
			asignarcuota.save()
			messages.success(request,'Se ha asignado correctamente')
			return redirect('asignarcuota_lista',)
	else:
		form = userpquotaForm()
	return render (request, 'pykota/asignarcuota_lista.html', {'filter': f, 'form': form})

@login_required
def asignarcuota_editar(request, pk):
	asignarcuota = get_object_or_404(userpquota, pk=pk)
	if request.method == "POST":
		form = userpquotaForm(request.POST, instance=asignarcuota)
		if form.is_valid():
			asignarcuota = form.save(commit=False)
			asignarcuota.save()
			return redirect('asignarcuota_lista')
	else:
		form = userpquotaForm(instance=asignarcuota)
	return render(request, 'pykota/asignarcuota_editar.html', {'form': form})

@login_required
def asignarcuota_borrar (request, pk):
	asignarcuota = get_object_or_404(userpquota, pk=pk)
	messages.info(request,'Se ha eliminado correctamente')
	asignarcuota.delete()
	return redirect ('asignarcuota_lista')