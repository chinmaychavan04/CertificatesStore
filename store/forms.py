from django.db.models import fields
from django import forms
from django.forms import ModelForm
from .models import *


class ProfileForm(forms.ModelForm):

    class Meta:
        model=Collection
        fields='__all__'

