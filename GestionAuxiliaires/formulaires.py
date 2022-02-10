from django.db.models import fields
from django import forms
from django.forms import Textarea

from .models import *


class PersonModF(forms.ModelForm):
    class Meta:
        model = Person
        fields= ['d_naissance']
        widgets = {
            'd_naissance': forms.DateInput(attrs={'class':'datepicker'}),

        }
class RefModF(forms.ModelForm):
    class Meta:
        model = Ref
        fields = '__all__'
class RefModFA(forms.ModelForm):
    class Meta:
        model = Ref
        fields = ('nom','prenom')
class EnfModF(forms.ModelForm):
    class Meta:
        model = Enf
        fields = '__all__'
        exclude = ['cin_Parent']
class AuxEnfModF(forms.ModelForm): #Saisie des enfants a partir de la liste des aux
    class Meta:
        model = Enf
        fields= '__all__'
        exclude = ['cin_Parent']
class ConjModF(forms.ModelForm):
    class Meta:
        model = Conjoint
        fields = '__all__'
        exclude=['cin_Conjoint']
class SitFinModF(forms.ModelForm):
    class Meta:
        model= SitFin
        fields= '__all__'
class Affiche_aux(forms.ModelForm): 
    class Meta:
        model = Ref
        fields = '__all__'

            #CharField(max_length=8)
            #authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
        #widgets = {
            #'nom': Textarea(attrs={'cols': 80, 'rows': 20}),
        #}



from .widgets import BootstrapDateTimePickerInput

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'], 
        widget=BootstrapDateTimePickerInput()
    )
class GradeModF(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'

class PaysModF(forms.ModelForm):
    class Meta:
        model = Pays
        fields = '__all__'


class RegionModF(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'

class PrefectureModF(forms.ModelForm):
    class Meta:
        model = Prefecture
        fields = '__all__'

class CommuneModF(forms.ModelForm):
    class Meta:
        model = Commune
        fields = '__all__'

class QuartierModF(forms.ModelForm):
    class Meta:
        model = Quartier
        fields = '__all__'

class AutreModF(forms.ModelForm):
    class Meta:
        model = Autre
        fields = '__all__'
class SituationModF(forms.ModelForm):
    class Meta:
        model = Situation
        fields = '__all__'
class Taux_AncModF(forms.ModelForm):
    class Meta:
        model = Taux_Anc
        fields = '__all__'
class PeriodeModF(forms.ModelForm):
    class Meta:
        model = Periode
        fields = '__all__'
class TypeModF(forms.ModelForm):
    class Meta:
        model= Type
        fields= '__all__'
class IntervalModF(forms.ModelForm):
    class Meta:
        model= Interval
        fields= '__all__'
class TbModF(forms.ModelForm):
    class Meta:
        model= Tb
        fields= '__all__'
class IrModF(forms.ModelForm):
    class Meta:
        model= Ir
        fields= '__all__'
class ItModF(forms.ModelForm):
    class Meta:
        model= It
        fields= '__all__'
class IfModF(forms.ModelForm):
    class Meta:
        model= If
        fields= '__all__'
class AfModF(forms.ModelForm):
    class Meta:
        model= Af
        fields= '__all__'
class RcarModF(forms.ModelForm):
    class Meta:
        model= Rcar
        fields= '__all__'
class AmoModF(forms.ModelForm):
    class Meta:
        model= Amo
        fields= '__all__'
class SmModF(forms.ModelForm):
    class Meta:
        model= Sm
        fields= '__all__'
class CaadModF(forms.ModelForm):
    class Meta:
        model= Caad
        fields= '__all__'
class IgrModF(forms.ModelForm):
    class Meta:
        model= Igr
        fields= '__all__'
class NetMModF(forms.ModelForm):
    class Meta:
        model= NetM
        fields= '__all__'
class BruteMModF(forms.ModelForm):
    class Meta:
        model= NetM
        fields= '__all__'