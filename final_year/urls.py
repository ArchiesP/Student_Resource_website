from django.urls import path
from . import views
urlpatterns = [
    path('', views.final_year, name="final_year"),
    #comp
    path('by_comp_subjects', views.by_comp_subjects, name="by_comp_subject"),
    path('by_comp/air', views.by_comp_air),
    path('by_comp/cc', views.by_comp_cc),
    path('by_comp/da', views.by_comp_da),
    path('by_comp/dmw', views.by_comp_dmw),
    path('by_comp/hci', views.by_comp_hci),
    path('by_comp/hpc', views.by_comp_hpc),
    path('by_comp/ics', views.by_comp_ics),
    path('by_comp/ml', views.by_comp_ml),
    path('by_comp/scoa', views.by_comp_scoa),
    path('by_comp/stqa', views.by_comp_stqa),
    #entc
    path('by_entc_subjects', views.by_entc_subjects, name="by_entc_subject"),
    path('by_entc/bc', views.by_entc_bc),
    path('by_entc/cns', views.by_entc_cns),
    path('by_entc/mc', views.by_entc_mc),
    path('by_entc/rmt', views.by_entc_rmt),
    path('by_entc/vlsi', views.by_entc_vlsi),

    #it
    path('by_it_subjects', views.by_it_subjects, name="by_it_subject"),
    path('by_it/dcs', views.by_it_dcs),
    path('by_it/ics', views.by_it_ics),
    path('by_it/mla', views.by_it_mla),
    path('by_it/sdm', views.by_it_sdm),
    path('by_it/uc', views.by_it_uc),
]
