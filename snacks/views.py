from .models import Snack
from django.views.generic import (ListView
                                 ,DetailView
                                 ,CreateView
                                 ,UpdateView
                                 ,DeleteView
                                 ,TemplateView)  

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'


class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = 'snack_list'

    

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack
    

class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snack
    # fields for the user to control the creation of the object
    fields = ['title', 'purchaser', 'description']
    

class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields = ['title', 'description']
    

class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url = '/'
    
