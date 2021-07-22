from django.shortcuts import render
def home(request):
    return render(request, 'home/index.html', {})

def first_year(request):
    return render(request, 'fy/first_year.html', {})

def fy_bee(request):
    return render(request, 'fy/bee.html', {})

def fy_books(request):
    return render(request, 'first year/fy_books.html', {})

def fy_assignments(request):
    return render(request, 'first year/fy_assignments.html', {})

def second_year(request):
    return render(request, 'branches.html', {})

def sy_comp(request):
    return render(request, 'second year/sy_comp.html', {})

def sy_comp_notes(request):
    return render(request, 'second year/sy_comp_notes.html', {})

def sy_comp_assignments(request):
    return render(request, 'second year/sy_comp_assignments.html', {})

def sy_comp_books(request):
    return render(request, 'second year/sy_comp_books.html', {})

def sy_it(request):
    return render(request, 'second year/sy_it.html', {})

def sy_it_notes(request):
    return render(request, 'second year/sy_it_notes.html', {})

def sy_it_assignments(request):
    return render(request, 'second year/sy_it_assignments.html', {})

def sy_it_books(request):
    return render(request, 'second year/sy_it_books.html', {})

def sy_entc(request):
    return render(request, 'second year/sy_entc.html', {})

def sy_entc_notes(request):
    return render(request, 'second year/sy_entc_notes.html', {})

def sy_entc_assignments(request):
    return render(request, 'second year/sy_entc_assignments.html', {})

def sy_entc_books(request):
    return render(request, 'second year/sy_entc_books.html', {})

def third_year(request):
    return render(request, 'ty/branches_ty.html', {})

def ty_comp(request):
    return render(request, 'third year/ty_comp.html', {})

def ty_comp_notes(request):
    return render(request, 'third year/ty_comp_notes.html', {})

def ty_comp_assignments(request):
    return render(request, 'third year/ty_comp_assignments.html', {})

def ty_comp_books(request):
    return render(request, 'third year/ty_comp_books.html', {})

def ty_it(request):
    return render(request, 'third year/ty_it.html', {})

def ty_it_notes(request):
    return render(request, 'third year/ty_it_notes.html', {})

def ty_it_assignments(request):
    return render(request, 'third year/ty_it_assignments.html', {})

def ty_it_books(request):
    return render(request, 'third year/ty_it_books.html', {})

def ty_entc(request):
    return render(request, 'third year/ty_entc.html', {})

def ty_entc_notes(request):
    return render(request, 'third year/ty_entc_notes.html', {})

def ty_entc_assignments(request):
    return render(request, 'third year/ty_entc_assignments.html', {})

def ty_entc_books(request):
    return render(request, 'third year/ty_entc_books.html', {})

def fourth_year(request):
    return render(request, 'by/branches_by.html', {})

def ly_comp(request):
    return render(request, 'Last year/ly_comp.html', {})

def ly_comp_notes(request):
    return render(request, 'Last year/ly_comp_notes.html', {})

def ly_comp_assignments(request):
    return render(request, 'Last year/ly_comp_assignments.html', {})

def ly_comp_books(request):
    return render(request, 'Last year/ly_comp_books.html', {})

def ly_it(request):
    return render(request, 'Last year/ly_it.html', {})

def ly_it_notes(request):
    return render(request, 'Last year/ly_it_notes.html', {})

def ly_it_assignments(request):
    return render(request, 'Last year/ly_it_assignments.html', {})

def ly_it_books(request):
    return render(request, 'Last year/ly_it_books.html', {})

def ly_entc(request):
    return render(request, 'Last year/ly_entc.html', {})

def ly_entc_notes(request):
    return render(request, 'Last year/ly_entc_notes.html', {})

def ly_entc_assignments(request):
    return render(request, 'Last year/ly_entc_assignments.html', {})

def ly_entc_books(request):
    return render(request, 'Last year/ly_entc_books.html', {})

def useful_links(request):
    return render(request, 'useful_links.html', {})
