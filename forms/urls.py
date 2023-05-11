from django.urls import path
from . import views

app_name = 'forms'

urlpatterns = [
    path('', views.home, name='home'),
    path('create',views.create, name='create'),
    path('forms/<str:pk>/edit',views.update_forms, name='update_forms'),
    path('forms/<str:pk>/viewForm',views.get_user_response, name='view_form'),
    path('forms/<str:pk>/responses',views.response, name='responses'),
]