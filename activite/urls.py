from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from activite.views import EntreeListView, EntreeDetailView, EntreeUpdateView, EntreeCreateView, InscriptionView, UserEntreeListView, UserListView


urlpatterns = [
    path("", EntreeListView.as_view(), name="entree"),
    path("entree/<int:pk>/detail", EntreeDetailView.as_view(), name="detail_entree"),
    path("entree/<int:pk>/modifier", EntreeUpdateView.as_view(), name="modifier_entree"),
    path("creer_entree", EntreeCreateView.as_view(), name="creer_entree"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('inscription/', InscriptionView.as_view(), name='inscription'),
    path('users/', UserListView.as_view(), name='liste_users'),
    path('users/<int:pk>/entrees/', UserEntreeListView.as_view(), name='user_entrees'),
]