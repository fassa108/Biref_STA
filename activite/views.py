from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, UpdateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from activite.forms import EntreeForm, EntreeUpdateForm, UserCreationForm

from .models import Entree
# Create your views here.

class EntreeListView(LoginRequiredMixin, ListView):
    model = Entree
    template_name = 'liste_tache.html'
    context_object_name = 'entrees'
    paginate_by = 2

class EntreeDetailView(LoginRequiredMixin, DetailView):
    model = Entree 
    template_name = 'detail_tache.html'
    context_object_name = 'entree'


class EntreeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Entree
    form_class = EntreeUpdateForm
    template_name = 'update_tache.html'
    
    def get_success_url(self):
        return reverse ('detail_entree', kwargs={'pk' : self.object.pk})
    
    def test_func(self):
        entree = self.get_object()
        return self.request.user == entree.user or self.request.user.is_staff
    


class EntreeCreateView(LoginRequiredMixin, CreateView):
    model = Entree
    form_class = EntreeForm
    template_name = 'creation_tache.html'
    def get_success_url(self):
        return reverse ('entree')

    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

        
        

class InscriptionView(UserPassesTestMixin, CreateView) :
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
    

    def test_func(self):    
        return self.request.user.is_superuser
    # def get_success_url(self):
    #     return reverse('detail_article', kwargs={'pk': self.object.article.pk})













# class EntreDeleteView(DeleteView):
#     model = Entree
#     template_name = 'delete_tache.html'
    
#     def get_success_url(self):
#         return reverse ('entree')
    