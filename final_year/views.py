from django.shortcuts import render

def final_year(request):
    return render(request, "by/branches_by.html")

#comp
def by_comp_subjects(request):
    return render(request, "by/by_comp_subjects.html")
def by_comp_air(request):
    return render(request, "by/by_comp/air.html")
def by_comp_cc(request):
    return render(request, "by/by_comp/cc.html")
def by_comp_da(request):
    return render(request, "by/by_comp/da.html")
def by_comp_dmw(request):
    return render(request, "by/by_comp/dmw.html")
def by_comp_hci(request):
    return render(request, "by/by_comp/hci.html")
def by_comp_hpc(request):
    return render(request, "by/by_comp/hpc.html")
def by_comp_ics(request):
    return render(request, "by/by_comp/ics.html")
def by_comp_ml(request):
    return render(request, "by/by_comp/ml.html")
def by_comp_scoa(request):
    return render(request, "by/by_comp/scoa.html")
def by_comp_stqa(request):
    return render(request, "by/by_comp/stqa.html")

#entc
def by_entc_subjects(request):
    return render(request, "by/by_entc_subjects.html")
def by_entc_bc(request):
    return render(request, "by/by_entc/bc.html")
def by_entc_cns(request):
    return render(request, "by/by_entc/cns.html")
def by_entc_mc(request):
    return render(request, "by/by_entc/mc.html")
def by_entc_rmt(request):
    return render(request, "by/by_entc/rmt.html")
def by_entc_vlsi(request):
    return render(request, "by/by_entc/vlsi.html")

#it
def by_it_subjects(request):
    return render(request, "by/by_it_subjects.html")
def by_it_dcs(request):
    return render(request, "by/by_it/dcs.html")
def by_it_ics(request):
    return render(request, "by/by_it/ics.html")
def by_it_mla(request):
    return render(request, "by/by_it/mla.html")
def by_it_sdm(request):
    return render(request, "by/by_it/sdm.html")
def by_it_uc(request):
    return render(request, "by/by_it/uc.html")

