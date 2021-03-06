from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .forms import * 

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('change_password/', PasswordChangeView.as_view(template_name='change_password.html',form_class=PasswordChangingForm, success_url=reverse_lazy('password_success')), name='password_change'),
    path('password_success/', PasswordChangeDoneView.as_view(template_name='password_success.html'), name='password_success'),
    path('logout/', views.logoutPage, name='logout'),
    path('', views.index, name='index'),
    path('créer_dwsr/', views.create_dwsr, name='create_dwsr'),
    path('liste_des_dwsr/', views.liste_des_dwsr, name='liste_des_dwsr'),
    path('create_dwsr_user/<int:id>/', views.create_dwsr_user, name='create_dwsr_user'),
    path('liste_des_session/', views.liste_session, name='liste_session'),
    path('create_candidat/', views.create_candidat, name='create_candidat'),
    path('liste_des_candidat/', views.liste_des_candidat, name='liste_des_candidat'),
    path('update_candidat/<int:id>', views.update_candidat, name='update_candidat'),
    path('delete_candidat/<int:id>', views.delete_candidat, name='delete_candidat'),
    path('inscrir_dans_session/<int:id>/', views.inscrir_dans_session, name='inscrir_dans_session'),
    path('suprimmer_le_dossier_du_dwsr/<int:id>', views.delete_dwsr, name='delete_dwsr'),
    path('MAJ_du_dossier_du_dwsr/<int:id>', views.update_dwsr, name='update_dwsr'),
    path('liste_des_utilisateur/', views.liste_des_user, name='liste_des_user'),
    path('profile_candidat/<int:id>', views.profile_candidat, name='profile_candidat'),
    path('create_candidat_user/<int:id>', views.create_candidat_user, name='create_candidat_user'),
    path('saisir_résultat/<int:id>', views.saisir_résultat, name='saisir_résultat'),
    path('delete_user/<int:id>', views.delete_user, name='delete_user'),
    path('update_user/<int:id>', views.update_user, name='update_user'),
    path('créer_centre_examen/', views.create_centre, name='create_centre'),
    path('liste_des_centre_examens/', views.liste_centre_examens, name='liste_centre_examens'),
    path('create_centre_user/<int:id>', views.create_centre_user, name='create_centre_user'),
    path('update_centre/<int:id>', views.update_centre, name='update_centre'),
    path('delete_centre/<int:id>', views.delete_centre, name='delete_centre'),
    path('create_auto_ecole/', views.create_auto_ecole, name='create_auto_ecole'),
    path('liste_auto_ecole/', views.liste_auto_ecole ,name='liste_auto_ecole'),
    path('update_auto_ecole/<int:id>', views.update_auto_ecole, name='update_auto_ecole'),
    path('delete_auto_ecole/<int:id>', views.delete_auto_ecole, name='delete_auto_ecole'),
    path('create_examinateur/', views.create_examinateur, name='create_examinateur'),
    path('liste_examinateur/', views.liste_examinateur, name='liste_examinateur'),
    path('update_examinateur/<int:id>', views.update_examinateur, name='update_examinateur'),
    path('delete_examinateur/<int:id>', views.delete_examinateur, name='delete_examinateur'),
    path('calendrier_des_session/', views.session_calendar, name='session_calendar'),
]