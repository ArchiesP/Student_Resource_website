from django.urls import path
from . import views
urlpatterns = [
    path('', views.third_year, name="third_year"),
    #comp
    path('ty_comp_subjects', views.ty_comp_subjects, name="ty_comp_subject"),
    path('ty_comp/cn', views.ty_comp_cn),
    path('ty_comp/daa', views.ty_comp_daa),
    path('ty_comp/dbms', views.ty_comp_dbms),
    path('ty_comp/esiot', views.ty_comp_esiot),
    path('ty_comp/isee', views.ty_comp_isee),
    path('ty_comp/sepm', views.ty_comp_sepm),
    path('ty_comp/smd', views.ty_comp_smd),
    path('ty_comp/toc', views.ty_comp_toc),
    path('ty_comp/wt', views.ty_comp_wt),
    path('ty_comp/spos', views.ty_comp_spos),
    #entc
    path('ty_entc_subjects', views.ty_entc_subjects, name="ty_entc_subject"),
    path('ty_entc/ap', views.ty_entc_ap),
    path('ty_entc/bm', views.ty_entc_bm),
    path('ty_entc/dc', views.ty_entc_dc),
    path('ty_entc/dsp', views.ty_entc_dsp),
    path('ty_entc/electromagnetics', views.ty_entc_electromagnetics),
    path('ty_entc/itcm', views.ty_entc_itcm),
    path('ty_entc/mechatronics', views.ty_entc_mechatronics),
    path('ty_entc/microcontrollers', views.ty_entc_microcontrollers),
    path('ty_entc/spos', views.ty_entc_spos),
    path('ty_entc/pe', views.ty_entc_pe),
    #it
    path('ty_it_subjects', views.ty_it_subjects, name="ty_it_subject"),
    path('ty_it/cc', views.ty_it_cc),
    path('ty_it/cn', views.ty_it_cn),
    path('ty_it/daa', views.ty_it_daa),
    path('ty_it/dbm', views.ty_it_dbm),
    path('ty_it/dsbda', views.ty_it_dsbda),
    path('ty_it/hci', views.ty_it_hci),
    path('ty_it/os', views.ty_it_os),
    path('ty_it/sepm', views.ty_it_sepm),
    path('ty_it/sp', views.ty_it_sp),
    path('ty_it/toc', views.ty_it_toc),
]