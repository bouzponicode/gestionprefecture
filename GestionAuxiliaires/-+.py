from django.shortcuts import render,redirect

# Create your views here.
#def index(request):
    #return render(request,'GestionAuxiliaires/index.html')

from .formulaires import *
from .models import *
from .filters import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, 'gestionAuxiliaires/index.html')


def home(request):
    persons = Person.objects.all()
    refs = Ref.objects.all()

    # orders = Order.objects.all()
    # t_orders = orders.count()
    # p_orders = orders.filter(status='Pending').count()
    # d_orders = orders.filter(status='Delivered').count()
    # in_orders = orders.filter(status='in progress').count()
    # out_orders = orders.filter(status='out of order').count()
    # context = {'customers': customers,
    #            'orders': orders,
    #            't_orders': t_orders,
    #            'p_orders': p_orders,
    #            'd_orders': d_orders,
    #            'in_orders': in_orders,
    #            'out_orders': out_orders}
    context = {'persons': persons, 'refs': refs}

    return render(request, 'gestionauxiliaires/dashbord.html',context)



def aux_list(request):
    auxs = Ref.objects.all()
    searchFilter =RefFilter(request.GET, queryset=auxs)
    auxs = searchFilter.qs

    paginator = Paginator(auxs, 2)#pagination
    page = request.GET.get('page')#pagination
    try:
        page_auxs = paginator.get_page(page)#pagination
    except  PageNotAnInteger:
        page_auxs = paginator.page(1)
    except  EmptyPage:
        page_auxs = paginator.page(paginator.num_pages)
    return render(request, 'gestionauxiliaires/aux_list.html', {'page': page,'auxs': page_auxs,'myFilter': searchFilter})




def d_aux(request, id):
    aux = Ref.objects.get(pk=id)
    aux.delete()
    return redirect('aux_list')
def person_list(request):
    persons = Person.objects.all()
    searchFilter = PersonFilter(request.GET, queryset=persons)
    persons = searchFilter.qs

    paginator = Paginator(persons, 6)#pagination
    page = request.GET.get('page')#pagination
    try:
        page_persons = paginator.get_page(page)#pagination
    except  PageNotAnInteger:
        page_persons = paginator.page(1)
    except  EmptyPage:
        page_persons = paginator.page(paginator.num_pages)
    return render(request, 'gestionAuxiliaires/person_list.html', {'page': page,'persons': page_persons,'myFilter': searchFilter})
    #return render(request,'gestionauxiliaires/dashbord.html')

def person_form (request,id=0):
    if request.method == "GET":
        if id == 0:
            personForm = PersonModF()
            refForm = RefModF()
            context = {'refForm': refForm}
            #'personForm': personForm,
        else:
            person = Person.objects.get(pk=id)
            personForm = PersonModF(instance=person)

        return render(request,"gestionAuxiliaires/person_Form.html",context)
    else:
        if id == 0:
            personForm = PersonModF(request.POST, request.FILES)
            refForm = RefModF(request.POST, request.FILES)
        else:
            person = Person.objects.get(pk=id)
            personForm = PersonModF(request.POST, request.FILES, instance=person)
        if refForm.is_valid():
            refForm.save()
        return redirect('home')

def ref_form (request,id=0):
    if request.method == "GET":
        if id == 0:
            refForm = RefModF()
        else:
            ref = Ref.objects.get(pk=id)
            refForm = RefModF(instance=ref)

        return render(request, "gestionAuxiliaires/aux_Form.html", {'refForm': refForm})
    else:
        if id == 0:
            refForm = RefModF(request.POST, request.FILES)
        else:
            ref = Ref.objects.get(pk=id)
            refForm = RefModF(request.POST, request.FILES, instance=ref)
        if refForm.is_valid():
            refForm.save()
        return redirect('home')

# Gestion des Enfants

def enf_form (request,id=0):
    if request.method == "GET":
        if id == 0:
            enfForm = EnfModF()
        else:
            enf = Enf.objects.get(pk=id)
            enfForm = EnfModF(instance=enf)

        return render(request, "gestionAuxiliaires/enf_Form.html", {'enfForm': enfForm})
    else:
        if id == 0:
            enfForm = EnfModF(request.POST, request.FILES)
        else:
            enf = Enf.objects.get(pk=id)
            enfForm = EnfModF(request.POST, request.FILES, instance=enf)
        if enfForm.is_valid():
            enfForm.save()
        return redirect('aux_list')

def enf_list(request,cin):
    enfs = Enf.objects.filter(cin_Parent=cin)
    searchFilter =EnfFilter(request.GET, queryset=enfs)
    enfs=searchFilter.qs

    paginator = Paginator(enfs,2)#pagination
    page = request.GET.get('page')#pagination
    try:
        page_enfs = paginator.get_page(page)#pagination
    except  PageNotAnInteger:
        page_enfs = paginator.page(1)
    except  EmptyPage:
        page_enfs = paginator.page(paginator.num_pages)
    return render(request, 'gestionauxiliaires/enf_list.html', {'page': page, 'enfs': page_enfs, 'myFilter': searchFilter})

def d_enf(request,id):
    enf = Enf.objects.get(pk=id)
    enf.delete()
    return redirect('/enf_list')

# Gestion des Conjoints

def conj_list(request, cin):
    conjs = Conjoint.objects.filter(cin_Conjoint=cin)
    searchFilter =ConjFilter(request.GET, queryset=conjs)
    conjs=searchFilter.qs

    paginator = Paginator(conjs, 2)#pagination
    page = request.GET.get('page')#pagination
    try:
        page_conjs = paginator.get_page(page)#pagination
    except  PageNotAnInteger:
        page_conjs = paginator.page(1)
    except  EmptyPage:
        page_conjs = paginator.page(paginator.num_pages)
    return render(request, 'gestionauxiliaires/conj_list.html', {'cin': cin, 'page': page, 'conjs' :page_conjs, 'myFilter': searchFilter})


def conj_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            conjForm = ConjModF()
        else:
            conj = Conjoint.objects.get(pk=id)
            conjForm = ConjModF(instance = conj)

        return render(request, "gestionAuxiliaires/conj_Form.html", {'conjForm':conjForm})
    else:
        if id == 0:
            conjForm = ConjModF(request.POST, request.FILES)
        else:
            conj = Conjoint.objects.get(pk=id)
            conjForm = ConjModF(request.POST, request.FILES, instance=conj)
        if conjForm.is_valid():
           conjForm.save()
        return redirect('aux_list')


def d_conj(request,id):
    conj = Conjoint.objects.get(pk=id)
    conj.delete()
    return redirect('/conj_list')
