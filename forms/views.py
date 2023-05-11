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

def get_user_response(request, pk):
    if request.method == 'POST':
        cd = dict(request.POST)
        del cd['csrfmiddlewaretoken']
        response = {}
        for key, value in cd.items():
            print(key,value[0])
            response.update({
                f"response.{key}.{value[0]}":1
            })
        Form.update_response(pk, response)
        return render(request, 'thankyou.html')
    else:
        try:
            form_data = Form.find(pk)
            return render(request, "get_response.html", {
                'pk':pk,
                'form':form_data
            })
        except: 
            raise Http404("Form Not Found")

def response(request, pk):
    form_data = Form.find(pk)
    return render(request, "responses.html", {
            # 'pk':pk,
            'form':form_data
        })