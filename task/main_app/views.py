from django.shortcuts import render, redirect
from django.urls import reverse
# import from db
from .models import Client , Customers
from django.views.generic.edit import CreateView , UpdateView , DeleteView 
# from .forms import CustomerForm


# Create your views here.
def home(request):
    return render(request,'home.html')

def clients_index(request):
    clients = Client.objects.all() 
    return render(request , 'clients/index.html' , {'clients': clients})

def clients_details(request , client_id):
    print(client_id)
    client = Client.objects.get(id=client_id)
    customers = Customers.objects.filter(client_id = client_id)
    print(customers)
    return render(request, 'clients/details.html' , {'client': client, 'customers': customers})


# CBV's - Client
class ClientCreate(CreateView):
    model= Client
    fields= '__all__'
    success_url = '/clients/'

# CBV's - Customers

def customers_details(request , customer_id):
    customer = Customers.objects.get(id=customer_id)
    return render(request, 'clients/details.html' , {'customer': customer})


class CustomerCreate(CreateView):
    model= Customers
    fields= ['username','description','path','action','error']
    success_url = '/clients/'

    def form_valid(self, form):
        print("id ====", self.kwargs.get('client_id'))
        form.instance.client_id = self.kwargs.get('client_id')
        # allows the CreateView form_valid method to do its normal work.
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('details', kwargs={'client_id': self.kwargs.get('client_id')})



class CustomerUpdate(UpdateView):
    model = Customers
    fields= ['username','description','path','action' ,'error']
    success_url = '/clients/'

   

class CustomerDelete(DeleteView):
    model = Customers
    success_url = '/clients/'


