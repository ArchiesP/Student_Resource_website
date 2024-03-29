from django.urls import path
from . import views
urlpatterns = [
    path('', views.second_year, name="second_year"),
    #comp
    path('sy_comp_subjects', views.sy_comp_subjects, name="sy_comp_subject"),
    path('sy_comp/dm', views.sy_comp_dm),
    path('sy_comp/deld', views.sy_comp_deld),
    path('sy_comp/dsa', views.sy_comp_dsa),
    path('sy_comp/coa', views.sy_comp_coa),
    path('sy_comp/oop', views.sy_comp_oop),
    path('sy_comp/em3', views.sy_comp_em3),
    path('sy_comp/cg', views.sy_comp_cg),
    path('sy_comp/ads', views.sy_comp_ads),
    path('sy_comp/mp', views.sy_comp_mp),
    path('sy_comp/ppl', views.sy_comp_ppl),
    #entc
    path('sy_entc_subjects', views.sy_entc_subjects, name="sy_entc_subject"),
    path('sy_entc/cs', views.sy_entc_cs),
    path('sy_entc/dc', views.sy_entc_dc),
    path('sy_entc/ds', views.sy_entc_ds),
    path('sy_entc/eec', views.sy_entc_eec),
    path('sy_entc/em3', views.sy_entc_em3),
    path('sy_entc/exc', views.sy_entc_exc),
    path('sy_entc/oop', views.sy_entc_oop),
    path('sy_entc/pcs', views.sy_entc_pcs),
    path('sy_entc/ss', views.sy_entc_ss),
    #it
    path('sy_it_subjects', views.sy_it_subjects, name="sy_it_subject"),
    path('sy_it/bcn', views.sy_it_bcn),
    path('sy_entc/cg', views.sy_it_cg),
    path('sy_it/dbms', views.sy_it_dbms),
    path('sy_it/dm', views.sy_it_dm),
    path('sy_it/dsa', views.sy_it_dsa),
    path('sy_it/em3', views.sy_it_em3),
    path('sy_it/ldco', views.sy_it_ldco),
    path('sy_it/oop', views.sy_it_oop),
    path('sy_it/pa', views.sy_it_pa),
    path('sy_it/se', views.sy_it_se),
]