from django.urls import path
from .views import customer_form, customers_list, export_csv


urlpatterns=[
    path('', customer_form, name='customer_form'),
    path('school_buy/', export_csv, name="export_csv"),
    path('school/', customers_list, name='customers_list')
]