from django.shortcuts import render

def second_year(request):
    return render(request, "sy/branches_sy.html")
#comp
def sy_comp_subjects(request):
    return render(request, "sy/sy_comp_subjects.html")
def sy_comp_dm(request):
    return render(request, "sy/sy_comp/dm.html")
def sy_comp_deld(request):
    return render(request, "sy/sy_comp/deld.html")
def sy_comp_dsa(request):
    return render(request, "sy/sy_comp/dsa.html")
def sy_comp_coa(request):
    return render(request, "sy/sy_comp/coa.html")
def sy_comp_oop(request):
    return render(request, "sy/sy_comp/oop.html")
def sy_comp_em3(request):
    return render(request, "sy/sy_comp/em3.html")
def sy_comp_cg(request):
    return render(request, "sy/sy_comp/cg.html")
def sy_comp_ads(request):
    return render(request, "sy/sy_comp/ads.html")
def sy_comp_mp(request):
    return render(request, "sy/sy_comp/mp.html")
def sy_comp_ppl(request):
    return render(request, "sy/sy_comp/ppl.html")

#entc
def sy_entc_subjects(request):
    return render(request, "sy/sy_entc_subjects.html")
def sy_entc_cs(request):
    return render(request, "sy/sy_entc/cs.html")
def sy_entc_dc(request):
    return render(request, "sy/sy_entc/dc.html")
def sy_entc_ds(request):
    return render(request, "sy/sy_entc/ds.html")
def sy_entc_em3(request):
    return render(request, "sy/sy_entc/em3.html")
def sy_entc_eec(request):
    return render(request, "sy/sy_entc/eec.html")
def sy_entc_exc(request):
    return render(request, "sy/sy_entc/exc.html")
def sy_entc_oop(request):
    return render(request, "sy/sy_entc/oop.html")
def sy_entc_pcs(request):
    return render(request, "sy/sy_entc/pcs.html")
def sy_entc_ss(request):
    return render(request, "sy/sy_entc/ss.html")


#it
def sy_it_subjects(request):
    return render(request, "sy/sy_it_subjects.html")
def sy_it_bcn(request):
    return render(request, "sy/sy_it/bcn.html")
def sy_it_cg(request):
    return render(request, "sy/sy_it/cg.html")
def sy_it_dbms(request):
    return render(request, "sy/sy_it/dbms.html")
def sy_it_dm(request):
    return render(request, "sy/sy_it/dm.html")
def sy_it_dsa(request):
    return render(request, "sy/sy_it/dsa.html")
def sy_it_em3(request):
    return render(request, "sy/sy_it/em3.html")
def sy_it_ldco(request):
    return render(request, "sy/sy_it/ldco.html")
def sy_it_oop(request):
    return render(request, "sy/sy_it/oop.html")
def sy_it_pa(request):
    return render(request, "sy/sy_it/pa.html")
def sy_it_se(request):
    return render(request, "sy/sy_it/se.html")
