from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, UpdateView,CreateView
from .forms import UCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from activite.forms import EntreeForm, EntreeUpdateForm, UserCreationForm

from .models import Categorie, Entree
# Create your views here.

class EntreeListView(LoginRequiredMixin, ListView):
    model = Entree
    template_name = 'liste_tache.html'
    context_object_name = 'entrees'
    paginate_by = 4

    def get_queryset(self):
        qs = Entree.objects.filter(user=self.request.user).order_by('-date_creation')
        statut = self.request.GET.get('statut')
        categorie = self.request.GET.get('categorie')
        if statut:
            qs = qs.filter(etat=statut)
        if categorie:
            qs = qs.filter(categorie__id=categorie)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        context['statut_choices'] = Entree.Statut.choices
        context['statut_actif'] = self.request.GET.get('statut', '')
        context['categorie_active'] = self.request.GET.get('categorie', '')
        return context

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


class UserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'liste_users.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_superuser
        
        

class InscriptionView(UserPassesTestMixin, CreateView) :
    form_class = UCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
    

    def test_func(self):    
        return self.request.user.is_superuser
    # def get_success_url(self):
    #     return reverse('detail_article', kwargs={'pk': self.object.article.pk})

class UserEntreeListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model               = Entree
    template_name       = 'liste_tache.html'
    context_object_name = 'entrees'
    paginate_by         = 2

    def test_func(self):
        return self.request.user.is_superuser

    def get_queryset(self):
        return Entree.objects.filter(
            user__pk=self.kwargs['pk']
        ).order_by('-date_creation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        context['statut_choices'] = Entree.Statut.choices
        context['statut_actif'] = self.request.GET.get('statut', '')
        context['categorie_active'] = self.request.GET.get('categorie', '')
        return context











# class EntreDeleteView(DeleteView):
#     model = Entree
#     template_name = 'delete_tache.html'
    
#     def get_success_url(self):
#         return reverse ('entree')
    