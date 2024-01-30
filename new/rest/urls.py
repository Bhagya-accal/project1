
from django.urls import path
from . import views
from.views import *
urlpatterns = [
    path('home/', views.home,name='home'),
    path('demo/',views.Demo_Serializer),
    path('update/<str:pk>/',views.list_product),
    path('exportcsv/', views.exportcsv,name='exportcsv'),
    path('generate_pdf/',views.generate_pdf,name='pdf')
]