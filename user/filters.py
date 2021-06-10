import django_filters
from django.forms import forms

from .models import *

class FormationFilter(django_filters.FilterSet):
    titer= django_filters.CharFilter('titer',lookup_expr='icontains')
    categ= django_filters.CharFilter('categ',lookup_expr='icontains')

    class Meta:
        model = Formation
        fields = ['titer','categ','etat']
