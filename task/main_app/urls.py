from django.urls import path
from . import views



urlpatterns = [
    # home
    path('', views.home , name='home'),
    # clients
    path('clients/' , views.clients_index , name='index'),
    path('clients/<int:client_id>', views.clients_details , name='details'),
    path('clients/add/' , views.ClientCreate.as_view(), name='clients_create'), 
    # customers
    path('customers/<int:client_id>', views.customers_details , name='customers_details'),
    path('customers/add/<int:client_id>' , views.CustomerCreate.as_view(), name='customers_create'), 
    path('customers/<int:pk>/update' , views.CustomerUpdate.as_view(), name='customers_update'), 
    path('customers/<int:pk>/delete' , views.CustomerDelete.as_view(), name='customers_delete'),
    # path('clients/<int:client_id>/add_customer' , views.add_customer , name='add_customer'),




]