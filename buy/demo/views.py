from django.shortcuts import render
from .models import Customer
from .forms import CustomersForm
from django.http import HttpResponse
from datetime import datetime

import csv

def export_csv(request):
    students=Customer.objects.all()
    response=HttpResponse('text/cvs')
    response['Content-Disposition'] = 'attachment; filename=export_csv' + str(datetime.now()) + '.csv'

    write=csv.writer(response)
    write.writerow([ 'id',  'first_name', "last_name", "email", "place", "phone_number", "message"])
    students_fields=students.values_list('id', 'first_name', "last_name", "email", "place", "phone_number", "message")
    for student in students_fields:
        write.writerow(student)
    return response

def customer_form(request):
    #print(Customer.objects.all())
    form=CustomersForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    ctx = {
        "form":form
    }

        # model=Customer() ### new 1
        # model.first_name=request.POST.get("first_name", None)
        # model.last_name=request.POST.get("last_name", None)
        #model.file = request.POST.get("file", None)
        # model.email=request.POST.get("email", None)
        # model.phone_number = request.POST.get("phone_number", None)
        # model.message = request.POST.get("message", None)
        # model.save()
    return render(request, 'form.html', ctx)


def customers_list(request):
    customers=Customer.objects.all()   #### new
    ctx = {
        "customers":customers
    }
    return render(request, 'table.html', ctx)
