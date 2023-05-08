from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from .utils import Form

# Create your views here.
Form = Form()

def get_uuid():
    return 'user'

def home(request):
    return render(request, 'home.html')

def create(request):
    pk = Form.create()
    return HttpResponseRedirect(reverse_lazy('forms:update_forms', args=[pk]))

def update_forms(request, pk):
    return render(request, 'update.html')