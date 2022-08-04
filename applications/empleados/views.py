from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import employee
from django.db.models import Q
# Create your views here.


class Home(TemplateView):
    template_name="crud/inicio.html"

class Listar(ListView):
    template_name='crud/crud.html'
    context_object_name='lista'
    
    paginate_by=5
    ordering='name'
    def get_queryset(self):
        palabra_clave=self.request.GET.get("kword",'')
        context_object_name='lista'
        resultados=employee.objects.filter(Q(id__icontains = palabra_clave) | Q(name__icontains = palabra_clave) | Q(last_name__icontains = palabra_clave) |
                Q(email__icontains = palabra_clave) | Q(phone__icontains = palabra_clave)).distinct()
        return resultados



class CrearRegistro(CreateView):
    model = employee
    
    template_name = "crud/agregar.html"
    fields=['name', 'last_name','email','phone']
    success_url='/lista'

class EditarRegistro(UpdateView):
    model = employee
    template_name = "crud/prueba.html"
    fields=['id','name', 'last_name','email','phone']
    success_url='/lista'
   
    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        return super(EditarRegistro, self).form_valid(form)




class EliminarRegistro(DeleteView):
    model = employee
    template_name = "crud/eliminar.html"
    success_url='/lista'







