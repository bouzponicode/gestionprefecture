import django_filters
from .models import *

class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = Person
        #fields ='__all__'
        #exclude=['photo']
        fields=['nom']

class RefFilter(django_filters.FilterSet):
    class Meta:
        model = Ref
        fields=['nom']

class EnfFilter(django_filters.FilterSet):
    class Meta:
        model = Enf
        fields=['nom']
class ConjFilter(django_filters.FilterSet):
    class Meta:
        model = Conjoint
        fields=['nom']


