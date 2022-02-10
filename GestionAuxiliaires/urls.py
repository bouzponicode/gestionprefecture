"""GestionPrefecture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('dashboard', views.home, name='home'),
    path('', views.index, name='index'),
    path('admin', views.admin, name='admin'),
    path('gestion', views.gestion, name='gestion'),
    path('edition', views.edition, name='edition'),
#Gestion des Auxiliaires
    path('person_test', views.persone_form, name='persone_form'),
    path('person_create', views.person_form, name='person_form'),  # La page auth_form.html
    path('a_l_aux/aux_create/', views.aux_create, name='aux_create'),
    path('a_l_aux/update/<int:id>/',views.aux_update,name='aux_update'),
    path('a_l_aux/delete/<int:id>/',views.aux_delete,name='aux_delete'),
    path('a_l_aux/', views.a_l_aux, name='a_l_aux'),
    path('s_aux', views.s_aux, name='s_aux'),  # La page auth_form.html
    path('s_aux/<int:id>', views.s_aux, name='s_aux'),
    path('aux_affiche/<int:id>', views.affiche_aux_form, name='affiche_aux_form'),  # La page auth_form.html
    path('aux_list/', views.aux_list, name='aux_list'),
    path('l_aux/', views.l_aux, name='l_aux'),
    path('<int:id>/', views.s_aux, name='e_aux'),
    path('s_aux', views.s_aux, name='s_aux'),  # La page auth_form.html
    path('d_aux/<int:id>', views.d_aux, name='d_aux'),
    #Gestion des Enfants
    path('s_enf', views.s_enf, name='s_enf'),  # La page enf_form.html
    #path('s_enf/<int:id>', views.s_enf, name='s_enf'),
    path('s_enf/<str:cin>', views.s_enf, name='s_enf'),
    #path('s_aux_enf/<str:cin>', views.s_aux_enf, name='s_aux_enf'),
    path('s_enf/<int:id>/', views.s_enf, name='e_enf'),
    #path('s_aux_enf/<int:id>', views.s_enf, name='e_enf'),
    #path('e_enf/<int:id>', views.s_enf, name='s_enf'),
    path('l_enf/', views.l_enf, name='l_enf'),
    path('l_enf/<str:cin>', views.l_enf, name='l_enf'),
    path('enf_list/<str:cin>', views.enf_list, name='enf_list'),
    path('d_enf/<int:id>', views.d_enf, name='d_enf'),
    #Gestion des Conjoints
    path('s_conj', views.s_conj, name='s_conj'),  # La page s_conj.html
    path('s_conj/<int:id>/', views.s_conj, name='e_conj'),
    path('s_conj/<str:cin>/', views.s_conj, name='s_conj'),
    path('l_conj/', views.l_conj, name='l_conj'),
    path('l_conj/<str:cin>', views.l_conj, name='l_conj'),
    path('conj_list/<str:cin>', views.conj_list, name='conj_list'),
    path('d_conj/<int:id>', views.d_conj, name='d_conj'),
    #Saisie des grades
    path('s_grade',views.grade_form,name= 's_grade'),
    path('s_grade/<int:id>',views.grade_form,name= 's_grade'),
    #Saisie des pays
    path('s_pays',views.pays_form,name= 's_pays'),
    path('s_pays/<int:id>',views.pays_form,name= 's_pays'),
    #Saisie des regions
    path('s_region/<int:id>',views.region_form,name= 's_region'),
    path('s_region',views.region_form,name= 's_region'),
    #Saisie des prefectures
    path('s_prefecture',views.prefecture_form,name= 's_prefecture'),
    path('s_prefecture/<int:id>',views.prefecture_form,name= 's_prefecture'),
    #Saisie des communes
    path('s_commune/<int:id>',views.commune_form,name= 's_commune'),
    path('s_commune',views.commune_form,name= 's_commune'),
    #Saisie des quartiers
    path('s_quartier/<int:id>',views.quartier_form,name= 's_quartier'),
    path('s_quartier',views.quartier_form,name= 's_quartier'),
    #Saisie des autres
    path('s_autre',views.autre_form,name= 's_autre'),
    path('s_autre/<int:id>',views.autre_form,name= 's_autre'),
    #Saisie des Situations
    path('s_situation',views.situation_form,name= 's_situation'),
    path('s_situation/<int:id>',views.situation_form,name= 's_situation'),
    #Saisie des Situations financières
    path('s_sit_fin',views.s_sit_fin,name= 's_sit_fin'),
    path('s_sit_fin/<int:id>',views.s_sit_fin,name= 's_sit_fin'),
    #Saisie des Taux d'Ancieneté
    path('s_taux_anc',views.taux_anc_form,name= 's_taux_anc'),
    path('s_taux_anc/<int:id>',views.taux_anc_form,name= 's_taux_anc'),
    #Saisie des Periodes
    path('s_periode',views.s_periode,name= 's_periode'),
    path('s_periode/<int:id>',views.s_periode,name= 's_periode'),
    #Saisie des Intrvales
    path('s_interval',views.s_interval,name= 's_interval'),
    path('s_interval/<int:id>',views.s_interval,name= 's_interval'),
    #Saisie des types
    path('s_type',views.s_type,name= 's_type'),
    path('s_type/<int:id>',views.s_type,name= 's_type'),
    #Traitement de base
    path('s_tb',views.s_tb,name= 's_tb'),
    path('s_tb/<int:id>',views.s_tb,name= 's_tb'),
    #Indemnité de representation
    path('s_ir',views.s_ir,name= 's_ir'),
    path('s_ir/<int:id>',views.s_ir,name= 's_ir'),
    #Indemnité de tournée
    path('s_it',views.s_it,name= 's_it'),
    path('s_it/<int:id>',views.s_it,name= 's_it'),
    #Indemnité de fonction
    path('s_if',views.s_if,name= 's_if'),
    path('s_if/<int:id>',views.s_if,name= 's_if'),
    #Allocations Familiales
    path('s_af',views.s_af,name= 's_af'),
    path('s_af/<int:id>',views.s_af,name= 's_af'),
    #RCAR
    path('s_rcar',views.s_rcar,name= 's_rcar'),
    path('s_rcar/<int:id>',views.s_rcar,name= 's_rcar'),
    #AMO
    path('s_amo',views.s_amo,name= 's_amo'),
    path('s_amo/<int:id>',views.s_amo,name= 's_amo'),
    #SM
    path('s_sm',views.s_sm,name= 's_sm'),
    path('s_sm/<int:id>',views.s_sm,name= 's_sm'),
    #CAAD
    path('s_caad',views.s_caad,name= 's_caad'),
    path('s_caad/<int:id>',views.s_caad,name= 's_caad'),
    #IGR
    path('s_igr',views.s_igr,name= 's_igr'),
    path('s_igr/<int:id>',views.s_igr,name= 's_igr'),
    #NetM
    path('s_netm',views.s_netm,name= 's_netm'),
    path('s_netm/<int:id>',views.s_netm,name= 's_netm'),
    #BruteM
    path('s_brutem',views.s_brutem,name= 's_brutem'),
    path('s_brutem/<int:id>',views.s_brutem,name= 's_brutem'),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




#
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('s_auth', views.auth_form, name='s_auth'),  # La page auth_form.html
#     path('<int:id>/', views.auth_form, name='e_authors'),
#     path('d_authors/<int:id>', views.d_authors, name='d_authors'),
#     path('list/', views.auth_list, name='auth_list'),
#     path('s_oeuv', views.oeuv_form, name='s_oeuv'),  # La page oeuv_form.html
#     path('list_Oeuvres/', views.oeuv_list, name='oeuv_list'),
#     path('oeuvre_e/<int:id>/', views.oeuv_form, name='e_oeuvres'),
#     path('d_oeuvres/<int:id>', views.d_oeuvres, name='d_oeuvres'),
#     path('oeuvres_a/<str:pk>' ,views.a_oeuv, name="a_oeuv"),
# ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




