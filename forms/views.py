from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import Http404, JsonResponse
from .utils import Form
import json

# Create your views here.
Form = Form()

def get_uuid():
    return 'user'

def home(request):
    forms = Form.findall()
    return render(request, 'home.html', {
        'forms':forms
    })

def create(request):
    pk = Form.create()
    return HttpResponseRedirect(reverse_lazy('forms:update_forms', args=[pk]))

def update_forms(request, pk):
    if request.method == 'POST':
        form_data = json.loads(request.body)
        Form.update(pk, form_data)
        return JsonResponse ({
            'saved':'ok'
        })
    try:
        form_data = Form.find(pk)
        return render(request, 'update.html',{
            'pk':pk,
            'form':form_data
        })
    except Exception as e:
        print(e)
        raise Http404('Form not found')

