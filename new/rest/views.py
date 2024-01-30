
from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest.models import *
from rest.serializers import demo_serializer
from rest_framework.response  import Response
from rest_framework.decorators import api_view
from rest_framework import status
import csv

from django.http import FileResponse
from reportlab.pdfgen import canvas

def home(request):
    return render(request,'home.html')
@api_view(['GET','POST'])
def Demo_Serializer(request):
    if request.method =='GET':
        Pro = Product.objects.all()
        x = demo_serializer(Pro,many=True)
        return Response(x.data)
    if request.method=='POST':
        pro=demo_serializer(data=request.data)
        if pro.is_valid():
            pro.save()
        return Response(pro.data)
@api_view(['GET','PUT','DELETE'])
def list_product(request,pk):
    if request.method =='GET':
        x=Product.objects.get(id=pk)
        Y=demo_serializer(x)
        return Response(Y.data)
    if request.method=='PUT':
        x=Product.objects.get(id=pk)
        Y=demo_serializer(x,data=request.data)
        if Y.is_valid():
            Y.save()
            return Response(Y.data)
    if request.method=='DELETE':
        x=Product.objects.get(id=pk)
        x.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


def exportcsv(request):
    z = Product.objects.all()
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="products.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['ID','product_name','product_price'])
    x = z.values_list('id','product_name','product_price')
    for y in x:
        writer.writerow(y)
    return response


def generate_pdf(request):
    response = FileResponse(generate_pdf_file(), 
                            as_attachment=True, 
                            filename='product_catalog.pdf')
    return response
 
 
def generate_pdf_file():
    from io import BytesIO
 
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
 
    # Create a PDF document
    x = Product.objects.all()
    p.drawString(100, 750, "Product Catalog")
 
    y = 700
    for z in x:
        p.drawString(100, y, f"Name: {z.product_name}")
        p.drawString(100, y - 20, f"Price: {z.product_price}")
       
        y -= 60
 
    p.showPage()
    p.save()
 
    buffer.seek(0)
    return buffer

    

    
