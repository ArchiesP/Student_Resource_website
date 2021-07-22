from django.shortcuts import render

def third_year(request):
    return render(request, "ty/branches_ty.html")
#comp
def ty_comp_subjects(request):
    return render(request, "ty/ty_comp_subjects.html")
def ty_comp_cn(request):
    return render(request, "ty/ty_comp/cn.html")
def ty_comp_daa(request):
    return render(request, "ty/ty_comp/daa.html")
def ty_comp_dbms(request):
    return render(request, "ty/ty_comp/dbms.html")
def ty_comp_esiot(request):
    return render(request, "ty/ty_comp/esiot.html")
def ty_comp_isee(request):
    return render(request, "ty/ty_comp/isee.html")
def ty_comp_sepm(request):
    return render(request, "ty/ty_comp/sepm.html")
def ty_comp_smd(request):
    return render(request, "ty/ty_comp/smd.html")
def ty_comp_toc(request):
    return render(request, "ty/ty_comp/toc.html")
def ty_comp_wt(request):
    return render(request, "ty/ty_comp/wt.html")
def ty_comp_spos(request):
    return render(request, "ty/ty_comp/spos.html")

#entc
def ty_entc_subjects(request):
    return render(request, "ty/ty_entc_subjects.html")
def ty_entc_ap(request):
    return render(request, "ty/ty_entc/ap.html")
def ty_entc_bm(request):
    return render(request, "ty/ty_entc/bm.html")
def ty_entc_dc(request):
    return render(request, "ty/ty_entc/dc.html")
def ty_entc_dsp(request):
    return render(request, "ty/ty_entc/dsp.html")
def ty_entc_electromagnetics(request):
    return render(request, "ty/ty_entc/electromagnetics.html")
def ty_entc_itcm(request):
    return render(request, "ty/ty_entc/itcm.html")
def ty_entc_mechatronics(request):
    return render(request, "ty/ty_entc/mechatronics.html")
def ty_entc_microcontrollers(request):
    return render(request, "ty/ty_entc/microcontrollers.html")
def ty_entc_pe(request):
    return render(request, "ty/ty_entc/pe.html")
def ty_entc_spos(request):
    return render(request, "ty/ty_entc/spos.html")


#it
def ty_it_subjects(request):
    return render(request, "ty/ty_it_subjects.html")
def ty_it_cc(request):
    return render(request, "ty/ty_it/cc.html")
def ty_it_cn(request):
    return render(request, "ty/ty_it/cn.html")
def ty_it_daa(request):
    return render(request, "ty/ty_it/daa.html")
def ty_it_dbm(request):
    return render(request, "ty/ty_it/dbm.html")
def ty_it_dsbda(request):
    return render(request, "ty/ty_it/dsbda.html")
def ty_it_hci(request):
    return render(request, "ty/ty_it/hci.html")
def ty_it_os(request):
    return render(request, "ty/ty_it/os.html")
def ty_it_sepm(request):
    return render(request, "ty/ty_it/sepm.html")
def ty_it_sp(request):
    return render(request, "ty/ty_it/sp.html")
def ty_it_toc(request):
    return render(request, "ty/ty_it/toc.html")
