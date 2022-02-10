import imp
from locale import format_string
from django.shortcuts import get_object_or_404, render,redirect

# Create your views here.
#def index(request):
#return render(request,'GestionAuxiliaires/index.html')

from .formulaires import *
from .models import *
from .filters import *
from django.forms import inlineformset_factory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.template.loader import render_to_string

def index(request):
    return render(request, 'gestionAuxiliaires/index.html')

def admin(request):
    return render(request, 'gestionAuxiliaires/administration.html')

def gestion(request):
    return render(request, 'gestionAuxiliaires/gestion.html')

def edition(request):
    return render(request, 'gestionAuxiliaires/edition.html')


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


def l_aux(request):
    items = Ref.objects.all()
    item_eff= items.count()
    searchFilter =RefFilter(request.GET, queryset=items)
    items = searchFilter.qs

    paginator = Paginator(items, 10)#pagination - 10 est le nombre d'enregitrements par page
    page = request.GET.get('page')#pagination
    try:
        page_items = paginator.get_page(page)#pagination
    except  PageNotAnInteger:
        page_items = paginator.page(1)
    except  EmptyPage:
        page_items = paginator.page(paginator.num_pages)
    context= {'page': page, 'items': page_items,'myFilter': searchFilter,'item_eff': item_eff

    }
    return render(request, 'gestionauxiliaires/l_aux.html', context)  

def aux_list(request):
    items = Ref.objects.all()
    item_eff= items.count()
    searchFilter =RefFilter(request.GET, queryset=items)
    items = searchFilter.qs

    paginator = Paginator(items, 10)#pagination - 10 est le nombre d'enregitrements par page
    page = request.GET.get('page')#pagination
    try:
        page_items = paginator.get_page(page)#pagination
    except  PageNotAnInteger:
        page_items = paginator.page(1)
    except  EmptyPage:
        page_items = paginator.page(paginator.num_pages)
    context= {'page': page, 'items': page_items,'myFilter': searchFilter,'item_eff': item_eff

    }
    return render(request, 'gestionauxiliaires/l_aux.html', context)


def a_l_aux(request):
    items = Ref.objects.all()
    item_eff= items.count()
    searchFilter =RefFilter(request.GET, queryset=items)
    items = searchFilter.qs

    paginator = Paginator(items, 100)#pagination - 10 est le nombre d'enregitrements par page
    page = request.GET.get('page')#pagination
    try:
        page_items = paginator.get_page(page)#pagination
    except  PageNotAnInteger:
        page_items = paginator.page(1)
    except  EmptyPage:
        page_items = paginator.page(paginator.num_pages)
    context= {'page': page, 'items': page_items,'myFilter': searchFilter,'item_eff': item_eff
    }
    return render(request, 'gestionauxiliaires/a_l_aux.html', context)
def d_aux(request, id):
    items = Ref.objects.get(pk=id)
    items.delete()
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
def persone_form (request,id=0):
    if request.method == "GET":
        if id == 0:
            form= DateForm()            
            context = {'form': form}            
        else:
            person = Person.objects.get(pk=id)
            form = DateForm(instance=person)
        return render(request,"gestionAuxiliaires/dpicker_test_form.html",context)
def person_form (request,id=0):
    if request.method == "GET":
        if id == 0:           
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


# Fonction utilisée avec JS
def aux_save(request,form,template_name):
    data = dict()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            #items = Ref.objects.all()
            items= Ref.objects.order_by('-id')
            item_eff= items.count()
            context= {
            'items':items,'item_eff': item_eff
            }
            data['a_l_aux']= render_to_string('gestionauxiliaires/a_l_aux_2.html', context)
        else:
            data['form_is_valid'] = False       
    context= {
        'form': form
    }
    data['html_form']= render_to_string(template_name, context, request = request)
    return JsonResponse(data)
def aux_create(request):
    if request.method == "POST":
        form = RefModF(request.POST)
    else:
        form = RefModF()
    return aux_save(request,form,'gestionAuxiliaires/aux_create.html')
def aux_update(request,id):
    item= get_object_or_404(Ref,id=id)
    if request.method == "POST":
        form = RefModF(request.POST,instance=item)
    else:
        form = RefModF(instance=item)
    return aux_save(request,form,'gestionAuxiliaires/aux_update.html')
def aux_delete(request,id):
    data = dict()
    item= get_object_or_404(Ref,id=id)
    
    if request.method == "POST":
        item.delete()
        data['form_is_valid'] = True
        items= Ref.objects.order_by('-id')
        item_eff= items.count()
        context= {'items':items,'item_eff': item_eff}
        data['a_l_aux']= render_to_string('gestionauxiliaires/a_l_aux_2.html', context)
    else:      
        context= {'item': item}
        data['html_form']= render_to_string('gestionauxiliaires/aux_delete.html', context, request = request)
    return JsonResponse(data)        



def s_aux (request,id=0):
    if request.method == "GET":
        if id == 0:
            form = RefModF()
        else:
            item = Ref.objects.get(pk=id)
            form = RefModF(instance=item)
        items= Ref.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_aux.html", context)
    else:
        if id == 0:
            form = RefModF(request.POST, request.FILES)
        else:
            ref = Ref.objects.get(pk=id)
            form = RefModF(request.POST, request.FILES, instance=ref)
        if form.is_valid():
            form.save()
    items= Ref.objects.all()
    context= {'items': items, 'form': form}
    return render(request, "gestionAuxiliaires/s_aux.html", context)
def affiche_aux_form (request,id=0):
    if request.method == "GET":
        aux = Ref.objects.get(pk=id)
    return render(request, "gestionAuxiliaires/affiche_aux.html", {'aux' : aux})
# Gestion des Enfants
def s_enf (request,id=0,cin=""):
    if request.method == "GET":
        if id == 0:
            form = EnfModF()
        else:
            item = Enf.objects.get(pk=id)
            form = EnfModF(instance=item)
            cin=item.cin_Parent
        items= Enf.objects.filter(cin_Parent=cin)
        context= {'items': items, 'form': form,'cin':cin}
        return render(request, "gestionAuxiliaires/s_enf.html", context)
    else:
        if id == 0:
            form = EnfModF(request.POST, request.FILES)
        else:
            item = Enf.objects.get(pk=id)
            cin= item.cin_Parent
            form = EnfModF(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form = form.save(commit= False)
            form.cin_Parent = cin
            form.save()
            id=0
            form = EnfModF()
        #else:
            #form = EnfModF(request.POST, request.FILES)       
    items= Enf.objects.filter(cin_Parent=cin)
    id=0
    context= {'items': items, 'form': form}
    return redirect('l_aux')
def l_enf(request):
    items= Enf.objects.all()
    paginator = Paginator(items,10)#pagination
    page = request.GET.get('page')#pagination
    try:
        page_items = paginator.get_page(page)#pagination
    except  PageNotAnInteger:
        page_items = paginator.page(1)
    except  EmptyPage:
        page_items = paginator.page(paginator.num_pages)
    return render(request, 'gestionauxiliaires/l_enf.html', {'page': page, 'items': page_items})

def enf_list(request,cin):
    enfs = Enf.objects.filter(cin_Parent=cin)
    searchFilter =EnfFilter(request.GET, queryset=enfs)
    enfs=searchFilter.qs

    paginator = Paginator(enfs,10)#pagination
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
    return redirect('/s_enf')

# Gestion des Conjoints
def l_conj(request):
    items= Conjoint.objects.all()
    paginator = Paginator(items,10)#pagination
    page = request.GET.get('page')#pagination
    try:
        page_items = paginator.get_page(page)#pagination
    except  PageNotAnInteger:
        page_items = paginator.page(1)
    except  EmptyPage:
        page_items = paginator.page(paginator.num_pages)
    return render(request, 'gestionauxiliaires/l_conj.html', {'page': page, 'items': page_items})

def conj_list(request, cin):
    conjs = Conjoint.objects.filter(cin_Conjoint=cin)
    searchFilter =ConjFilter(request.GET, queryset=conjs)
    conjs=searchFilter.qs
    paginator = Paginator(conjs, 10)#pagination
    page = request.GET.get('page')#pagination
    try:
        page_conjs = paginator.get_page(page)#pagination
    except  PageNotAnInteger:
        page_conjs = paginator.page(1)
    except  EmptyPage:
        page_conjs = paginator.page(paginator.num_pages)
    context={'cin': cin, 'page': page, 'conjs' :page_conjs, 'myFilter': searchFilter}    
    return render(request, 'gestionauxiliaires/conj_list.html',context )

def s_conj (request,id=0,cin=""):
    if request.method == "GET":
        if id == 0:
            form = ConjModF()
        else:
            item = Conjoint.objects.get(pk=id)
            form = ConjModF(instance=item)
            cin=item.cin_Conjoint
        items= Conjoint.objects.filter(cin_Conjoint=cin)
        context= {'items': items, 'form': form,'cin':cin}
        return render(request, "gestionAuxiliaires/s_conj.html", context)
    else:
        if id == 0:
            form = ConjModF(request.POST, request.FILES)
        else:
            item = Conjoint.objects.get(pk=id)
            cin= item.cin_Conjoint
            form = ConjModF(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form = form.save(commit= False)
            form.cin_Conjoint = cin
            form.save()
            id=0
            form = ConjModF()
        else:
            form = ConjModF(request.POST, request.FILES)       
    items= Conjoint.objects.filter(cin_Conjoint=cin)
    id=0
    context= {'items': items, 'form': form}
    return redirect('l_aux')

def s_conjj(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ConjModF()
        else:
            queryset = Conjoint.objects.get(pk= id) 
            form = ConjModF(instance= queryset)
        cin=queryset.cin_Parent
        items= Conjoint.objects.filter(cin_Conjoint=cin)
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_conj.html", context)
    else:
        if id == 0:
            form = ConjModF(request.POST, request.FILES)
        else:
            queryset = Conjoint.objects.get(pk=id)
            form = ConjModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
    items= Conjoint.objects.all()
    context= {'items': items, 'form': form}
    return render(request, "gestionAuxiliaires/s_conj.html", context)

# def conj_form(request, id):
#     ConjFormSet= inlineformset_factory(Ref, Conjoint, fields=('cin', 'nom'))
#     aux= Person.objects.get(pk=id)
#
#     conjFormSet = ConjFormSet(instance=aux)
#     return render(request, "gestionAuxiliaires/conj_Form.html", {'conjFormSet':conjFormSet})
#     conjFormSet = ConjFormSet(request.POST, instance=aux)
#     if conjFormSet.is_valid():
#         conjFormSet.save()
#         return redirect('aux_list')


def d_conj(request,id):
    conj = Conjoint.objects.get(pk=id)
    conj.delete()
    return redirect('/l_conj')
#Situation financière
def s_sit_fin (request,id= 0):
    if request.method == "GET":
        if id == 0:
            form = SitFinModF()
        else:
            queryset = SitFin.objects.get(pk= id)
            form = SitFinModF(instance= queryset)
        items= SitFin.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_sit_fin.html", context)
    else:
        if id == 0:
            form = SitFinModF(request.POST, request.FILES)
        else:
            queryset = SitFin.objects.get(pk=id)
            form = SitFinModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
    items= SitFin.objects.all()
    context= {'items': items, 'form': form}
    return render(request, "gestionAuxiliaires/s_sit_fin.html", context)

#Grades
def grade_form (request,id=0):
    if request.method == "GET":
        if id == 0:
            form = GradeModF()
        else:
            queryset = Grade.objects.get(pk=id)
            form = GradeModF(instance=queryset)
        items= Grade.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/grade_Form.html", context)
    else:
        if id == 0:
            form = GradeModF(request.POST, request.FILES)
        else:
            queryset = Grade.objects.get(pk=id)
            form = GradeModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
        items= Grade.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/grade_Form.html", context)

#pays
def pays_form (request,id=0):
    if request.method == "GET":
        if id == 0:
            form = PaysModF()
        else:
            queryset = Pays.objects.get(pk=id)
            form = PaysModF(instance=queryset)
        items= Pays.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/pays_Form.html", context)
    
    else:
        if id == 0:
            form = PaysModF(request.POST, request.FILES)
        else:
            queryset = Pays.objects.get(pk=id)
            form = PaysModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
        items= Pays.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/pays_Form.html", context)
        #return redirect('s_region')
#Region
def region_form (request,id=0):
    if request.method == "GET":
        if id == 0:
            form = RegionModF()
        else:
            queryset = Region.objects.get(pk=id)
            form = RegionModF(instance=queryset)
        items= Region.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/region_Form.html", context)
    else:
        if id == 0:
            form = RegionModF(request.POST, request.FILES)
        else:
            queryset = Region.objects.get(pk=id)
            form = RegionModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
        items= Region.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/region_Form.html", context)
        #return redirect('s_prefecture')

#Prefecture
def prefecture_form (request,id=0):
    if request.method == "GET":
        if id == 0:
            form = PrefectureModF()
        else:
            queryset = Prefecture.objects.get(pk=id)
            form = PrefectureModF(instance=queryset)
        items= Prefecture.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/prefecture_Form.html", context)
    else:
        if id == 0:
            form = PrefectureModF(request.POST, request.FILES)
        else:
            queryset = Prefecture.objects.get(pk=id)
            form = PrefectureModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
        items= Prefecture.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/prefecture_Form.html", context)

#Commune
def commune_form (request,id=0):
    if request.method == "GET":
        if id == 0:
            form = CommuneModF()
        else:
            queryset = Commune.objects.get(pk=id)
            form = CommuneModF(instance=queryset)
        items= Commune.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/commune_Form.html", context)    
        
    else:
        if id == 0:
            form = CommuneModF(request.POST, request.FILES)
        else:
            queryset = Commune.objects.get(pk=id)
            form = CommuneModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
        items= Commune.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/commune_Form.html", context)

#Quartier
def quartier_form (request,id=0):
    if request.method == "GET":
        if id == 0:
            form = QuartierModF()
        else:
            queryset = Quartier.objects.get(pk=id)
            form = QuartierModF(instance=queryset)
        items= Quartier.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/quartier_Form.html", context)
    else:
        if id == 0:
            form = QuartierModF(request.POST, request.FILES)
        else:
            queryset = Quartier.objects.get(pk=id)
            form = QuartierModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
        items= Quartier.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/quartier_Form.html", context)

#Autre
def autre_form (request,id=0):
    if request.method == "GET":
        if id == 0:
            form = AutreModF()
        else:
            queryset = Autre.objects.get(pk=id)
            form = AutreModF(instance=queryset)
        items= Autre.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/autre_Form.html", context)
    else:
        if id == 0:
            form = AutreModF(request.POST, request.FILES)
        else:
            queryset = Autre.objects.get(pk=id)
            form = AutreModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
        items= Autre.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/autre_Form.html", context)

#Situation
def situation_form (request,id=0):
    if request.method == "GET":
        if id == 0:
            form = SituationModF()
        else:
            queryset = Situation.objects.get(pk=id)
            form = SituationModF(instance=queryset)
        items= Situation.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/situation_Form.html", context)
    else:
        if id == 0:
            form = SituationModF(request.POST, request.FILES)
        else:
            queryset = Situation.objects.get(pk=id)
            form = SituationModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
        items= Situation.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/situation_Form.html", context)
#Taux d'ancieneté
def taux_anc_form (request,id=0):
    if request.method == "GET":
        if id == 0:
            form = Taux_AncModF()
        else:
            queryset = Taux_Anc.objects.get(pk=id)
            form = Taux_AncModF(instance=queryset)
        items= Taux_Anc.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/taux_anc_Form.html", context)
    else:
        if id == 0:
            form = Taux_AncModF(request.POST, request.FILES)
        else:
            queryset = Taux_Anc.objects.get(pk=id)
            form = Taux_AncModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
        items= Taux_Anc.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/taux_anc_Form.html", context)
#Gestion des Periodes
def s_periode (request,id=0):
    if request.method == "GET":
        if id == 0:
            form = PeriodeModF()
        else:
            queryset = Periode.objects.get(pk=id)
            form = PeriodeModF(instance=queryset)
        items= Periode.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_periode.html", context)
    else:
        if id == 0:
            form = PeriodeModF(request.POST, request.FILES)
        else:
            queryset = Periode.objects.get(pk=id)
            form = PeriodeModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
        items= Periode.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_periode.html", context)
#Saisie des types
def s_type (request,id=0):
    if request.method == "GET":
        if id == 0:
            form = TypeModF()
        else:
            queryset = Type.objects.get(pk=id)
            form = TypeModF(instance=queryset)
        items= Type.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_type.html", context)
    else:
        if id == 0:
            form = TypeModF(request.POST, request.FILES)
        else:
            queryset = Type.objects.get(pk=id)
            form = TypeModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            form = TypeModF()
        items= Type.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_type.html", context)    
#Saisie des Intervales
def s_interval (request,id=0):
    if request.method == "GET":
        if id == 0:
            form = IntervalModF()
        else:
            queryset = Interval.objects.get(pk=id)
            form = IntervalModF(instance=queryset)
        items= Interval.objects.all()
        context= {'items': items, 'form': form}
        for item in items:
                print(item.id) 
        return render(request, "gestionAuxiliaires/s_interval.html", context)
    else:
        if id == 0:
            form = IntervalModF(request.POST, request.FILES)
        else:
            queryset = Interval.objects.get(pk=id)
            form = IntervalModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            form = IntervalModF()
        items= Interval.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_interval.html", context)    

#Traitment de base
def s_tb (request,id= 0):
    if request.method == "GET":
        if id == 0:
            form = TbModF()
        else:
            queryset = Tb.objects.get(pk= id)
            form = TbModF(instance= queryset)
        items= Tb.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_tb.html", context)
    else:
        if id == 0:
            form = TbModF(request.POST, request.FILES)
        else:
            queryset = Tb.objects.get(pk=id)
            form = TbModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
    items= Tb.objects.all()
    form = TbModF()
    context= {'items': items, 'form': form}
    return render(request, "gestionAuxiliaires/s_tb.html", context)
#Indemnité de representation
def s_ir (request,id= 0):
    if request.method == "GET":
        if id == 0:
            form = IrModF()
        else:
            queryset = Ir.objects.get(pk= id)
            form = IrModF(instance= queryset)
        items= Ir.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_ir.html", context)
    else:
        if id == 0:
            form = IrModF(request.POST, request.FILES)
        else:
            queryset = Ir.objects.get(pk=id)
            form = IrModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
    items= Ir.objects.all()
    form = IrModF()
    context= {'items': items, 'form': form}
    return render(request, "gestionAuxiliaires/s_ir.html", context)
#Indemnité de tournée
def s_it (request,id= 0):
    if request.method == "GET":
        if id == 0:
            form = ItModF()
        else:
            queryset = It.objects.get(pk= id)
            form = ItModF(instance= queryset)
        items= It.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_it.html", context)
    else:
        if id == 0:
            form = ItModF(request.POST, request.FILES)
        else:
            queryset = It.objects.get(pk=id)
            form = ItModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
    items= It.objects.all()
    form = ItModF()
    context= {'items': items, 'form': form}
    return render(request, "gestionAuxiliaires/s_it.html", context)
#Indemnité de fonction
def s_if (request,id= 0):
    if request.method == "GET":
        if id == 0:
            form = IfModF()
        else:
            queryset = If.objects.get(pk= id)
            form = IfModF(instance= queryset)
        items= If.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_if.html", context)
    else:
        if id == 0:
            form = IfModF(request.POST, request.FILES)
        else:
            queryset = If.objects.get(pk=id)
            form = IfModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
    items= If.objects.all()
    form = IfModF()
    context= {'items': items, 'form': form}
    return render(request, "gestionAuxiliaires/s_if.html", context)

#Allocations Familiales
def s_af (request,id= 0):
    if request.method == "GET":
        if id == 0:
            form = AfModF()
        else:
            queryset = Af.objects.get(pk= id)
            form = AfModF(instance= queryset)
        items= Af.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_af.html", context)
    else:
        if id == 0:
            form = AfModF(request.POST, request.FILES)
        else:
            queryset = Af.objects.get(pk=id)
            form = AfModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
    items= Af.objects.all()
    form = AfModF()
    context= {'items': items, 'form': form}
    return render(request, "gestionAuxiliaires/s_af.html", context)
    #RCAR
def s_rcar (request,id= 0):
    if request.method == "GET":
        if id == 0:
            form = RcarModF()
        else:
            queryset = Rcar.objects.get(pk= id)
            form = RcarModF(instance= queryset)
        items= Rcar.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_rcar.html", context)
    else:
        if id == 0:
            form = RcarModF(request.POST, request.FILES)
        else:
            queryset = Rcar.objects.get(pk=id)
            form = RcarModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
    items= Rcar.objects.all()
    form = RcarModF()
    context= {'items': items, 'form': form}
    return render(request, "gestionAuxiliaires/s_rcar.html", context)
    #AMO
def s_amo (request,id= 0):
    if request.method == "GET":
        if id == 0:
            form = AmoModF()
        else:
            queryset = Amo.objects.get(pk= id)
            form = AmoModF(instance= queryset)
        items= Amo.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_amo.html", context)
    else:
        if id == 0:
            form = AmoModF(request.POST, request.FILES)
        else:
            queryset = Amo.objects.get(pk=id)
            form = AmoModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
    items= Amo.objects.all()
    form = AmoModF()
    context= {'items': items, 'form': form}
    return render(request, "gestionAuxiliaires/s_amo.html", context)
    #SM
def s_sm (request,id= 0):
    if request.method == "GET":
        if id == 0:
            form = SmModF()
        else:
            queryset = Sm.objects.get(pk= id)
            form = SmModF(instance= queryset)
        items= Sm.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_sm.html", context)
    else:
        if id == 0:
            form = SmModF(request.POST, request.FILES)
        else:
            queryset = Sm.objects.get(pk=id)
            form = SmModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
    items= Sm.objects.all()
    form = SmModF()
    context= {'items': items, 'form': form}
    return render(request, "gestionAuxiliaires/s_sm.html", context)
#CAAD
def s_caad (request,id= 0):
    if request.method == "GET":
        if id == 0:
            form = CaadModF()
        else:
            queryset = Caad.objects.get(pk= id)
            form = CaadModF(instance= queryset)
        items= Caad.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_caad.html", context)
    else:
        if id == 0:
            form = CaadModF(request.POST, request.FILES)
        else:
            queryset = Caad.objects.get(pk=id)
            form = CaadModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
    items= Caad.objects.all()
    form = CaadModF()
    context= {'items': items, 'form': form}
    return render(request, "gestionAuxiliaires/s_caad.html", context)
#IGR
def s_igr (request,id= 0):
    if request.method == "GET":
        if id == 0:
            form = IgrModF()
        else:
            queryset = Igr.objects.get(pk= id)
            form = IgrModF(instance= queryset)
        items= Igr.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_igr.html", context)
    else:
        if id == 0:
            form = IgrModF(request.POST, request.FILES)
        else:
            queryset = Igr.objects.get(pk=id)
            form = IgrModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
    items= Igr.objects.all()
    form = IgrModF()
    context= {'items': items, 'form': form}
    return render(request, "gestionAuxiliaires/s_igr.html", context)
#NETM
def s_netm (request,id= 0):
    if request.method == "GET":
        if id == 0:
            form = NetMModF()
        else:
            queryset = NetM.objects.get(pk= id)
            form = NetMModF(instance= queryset)
        items= NetM.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_netm.html", context)
    else:
        if id == 0:
            form = NetMModF(request.POST, request.FILES)
        else:
            queryset = NetM.objects.get(pk=id)
            form = NetMModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
    items= NetM.objects.all()
    form = NetMModF()
    context= {'items': items, 'form': form}
    return render(request, "gestionAuxiliaires/s_netm.html", context)
#BRUTEM
def s_brutem (request,id= 0):
    if request.method == "GET":
        if id == 0:
            form = BruteMModF()
        else:
            queryset = BruteM.objects.get(pk= id)
            form = BruteMModF(instance= queryset)
        items= BruteM.objects.all()
        context= {'items': items, 'form': form}
        return render(request, "gestionAuxiliaires/s_brutem.html", context)
    else:
        if id == 0:
            form = BruteMModF(request.POST, request.FILES)
        else:
            queryset = BruteM.objects.get(pk=id)
            form = BruteMModF(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
    items= BruteM.objects.all()
    form = BruteMModF()
    context= {'items': items, 'form': form}
    return render(request, "gestionAuxiliaires/s_brutem.html", context)