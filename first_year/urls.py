from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_year, name="first_year"),
    # BEE
    path('bee_units/', views.fy_bee, name="fy_bee"),
    path('bee_units/bee_unit1', views.fy_bee1, name="fy_bee1"),
    path('bee_units/bee_unit2', views.fy_bee2, name="fy_bee2"),
    path('bee_units/bee_unit3', views.fy_bee3, name="fy_bee3"),
    path('bee_units/bee_unit4', views.fy_bee4, name="fy_bee4"),
    path('bee_units/bee_unit5', views.fy_bee5, name="fy_bee5"),
    path('bee_units/bee_unit6', views.fy_bee6, name="fy_bee6"),
    # BXE
    path('bxe_units/', views.fy_bxe, name="fy_bxe"),
    path('bxe_units/bxe_unit1', views.fy_bxe1, name="fy_bxe1"),
    path('bxe_units/bxe_unit2', views.fy_bxe2, name="fy_bxe2"),
    path('bxe_units/bxe_unit3', views.fy_bxe3, name="fy_bxe3"),
    path('bxe_units/bxe_unit4', views.fy_bxe4, name="fy_bxe4"),
    path('bxe_units/bxe_unit5', views.fy_bxe5, name="fy_bxe5"),
    path('bxe_units/bxe_unit6', views.fy_bxe6, name="fy_bxe6"),
    # Engineering Chemistry
    path('ec_units/', views.fy_ec, name="fy_ec"),
    path('ec_units/ec_unit1', views.fy_ec1, name="fy_ec1"),
    path('ec_units/ec_unit2', views.fy_ec2, name="fy_ec2"),
    path('ec_units/ec_unit3', views.fy_ec3, name="fy_ec3"),
    path('ec_units/ec_unit4', views.fy_ec4, name="fy_ec4"),
    path('ec_units/ec_unit5', views.fy_ec5, name="fy_ec5"),
    path('ec_units/ec_unit6', views.fy_ec6, name="fy_ec6"),
    # Engineering Graphics
    path('eg_units/', views.fy_eg, name="fy_eg"),
    path('eg_units/eg_unit1', views.fy_eg1, name="fy_eg1"),
    path('eg_units/eg_unit2', views.fy_eg2, name="fy_eg2"),
    path('eg_units/eg_unit3', views.fy_eg3, name="fy_eg3"),
    path('eg_units/eg_unit4', views.fy_eg4, name="fy_eg4"),
    path('eg_units/eg_unit5', views.fy_eg5, name="fy_eg5"),
    path('eg_units/eg_unit6', views.fy_eg6, name="fy_eg6"),
    # Engineering Mechanics
    path('em_units/', views.fy_em, name="fy_em"),
    path('em_units/em_unit1', views.fy_em1, name="fy_em1"),
    path('em_units/em_unit2', views.fy_em2, name="fy_em2"),
    path('em_units/em_unit3', views.fy_em3, name="fy_em3"),
    path('em_units/em_unit4', views.fy_em4, name="fy_em4"),
    path('em_units/em_unit5', views.fy_em5, name="fy_em5"),
    path('em_units/em_unit6', views.fy_em6, name="fy_em6"),
    # Engineering Mathematics 1
    path('em1_units/', views.fy_em_1, name="fy_em1"),
    path('em1_units/em1_unit1', views.fy_em1_1, name="fy_em1_1"),
    path('em1_units/em1_unit2', views.fy_em1_2, name="fy_em1_2"),
    path('em1_units/em1_unit3', views.fy_em1_3, name="fy_em1_3"),
    path('em1_units/em1_unit4', views.fy_em1_4, name="fy_em1_4"),
    path('em1_units/em1_unit5', views.fy_em1_5, name="fy_em1_5"),
    path('em1_units/em1_unit6', views.fy_em1_6, name="fy_em1_6"),
    # Engineering Mathematics 2
    path('em2_units/', views.fy_em_2, name="fy_em2"),
    path('em2_units/em2_unit1', views.fy_em2_1, name="fy_em2_1"),
    path('em2_units/em2_unit2', views.fy_em2_2, name="fy_em2_2"),
    path('em2_units/em2_unit3', views.fy_em2_3, name="fy_em2_3"),
    path('em2_units/em2_unit4', views.fy_em2_4, name="fy_em2_4"),
    path('em2_units/em2_unit5', views.fy_em2_5, name="fy_em2_5"),
    path('em2_units/em2_unit6', views.fy_em2_6, name="fy_em2_6"),
    # Engineering Physics
    path('ep_units/', views.fy_ep, name="fy_ep"),
    path('ep_units/ep_unit1', views.fy_ep1, name="fy_ep1"),
    path('ep_units/ep_unit2', views.fy_ep2, name="fy_ep2"),
    path('ep_units/ep_unit3', views.fy_ep3, name="fy_ep3"),
    path('ep_units/ep_unit4', views.fy_ep4, name="fy_ep4"),
    path('ep_units/ep_unit5', views.fy_ep5, name="fy_ep5"),
    path('ep_units/ep_unit6', views.fy_ep6, name="fy_ep6"),
    # PPS
    path('pps_units/', views.fy_pps, name="fy_pps"),
    path('pps_units/pps_unit1', views.fy_pps1, name="fy_pps1"),
    path('pps_units/pps_unit2', views.fy_pps2, name="fy_pps2"),
    path('pps_units/pps_unit3', views.fy_pps3, name="fy_pps3"),
    path('pps_units/pps_unit4', views.fy_pps4, name="fy_pps4"),
    path('pps_units/pps_unit5', views.fy_pps5, name="fy_pps5"),
    path('pps_units/pps_unit6', views.fy_pps6, name="fy_pps6"),
    # Systems in Mechanical Engineering
    path('sme_units/', views.fy_sme, name="fy_sme"),
    path('sme_units/sme_unit1', views.fy_sme1, name="fy_sme1"),
    path('sme_units/sme_unit2', views.fy_sme2, name="fy_sme2"),
    path('sme_units/sme_unit3', views.fy_sme3, name="fy_sme3"),
    path('sme_units/sme_unit4', views.fy_sme4, name="fy_sme4"),
    path('sme_units/sme_unit5', views.fy_sme5, name="fy_sme5"),
    path('sme_units/sme_unit6', views.fy_sme6, name="fy_sme6"),


]
