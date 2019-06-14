from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Item
from .models import Item1
from .models import Item2


class Item0Form(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("Q1_1", "Q1_2")
        widgets = {
                    "Q1_1": forms.RadioSelect(),
                    "Q1_2": forms.RadioSelect(),
                  }

class Item1Form(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("Q1_1", "Q1_2", "Q1_3", "Q1_4", "Q1_5")
        widgets = {
                    "Q1_1": forms.RadioSelect(),
                    "Q1_2": forms.RadioSelect(),
                    "Q1_3": forms.RadioSelect(),
                    "Q1_4": forms.RadioSelect(),
                    "Q1_5": forms.RadioSelect(),
                  }
class Item2Form(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("Q2_1", "Q2_2", "Q2_3", "Q2_4", "Q2_5")
        widgets = {
                    "Q2_1": forms.RadioSelect(),
                    "Q2_2": forms.RadioSelect(),
                    "Q2_3": forms.RadioSelect(),
                    "Q2_4": forms.RadioSelect(),
                    "Q2_5": forms.RadioSelect(),
                  }
class Item3Form(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("Q3_1", "Q3_2", "Q3_3", "Q3_4", "Q3_5")
        widgets = {
                    "Q3_1": forms.RadioSelect(),
                    "Q3_2": forms.RadioSelect(),
                    "Q3_3": forms.RadioSelect(),
                    "Q3_4": forms.RadioSelect(),
                    "Q3_5": forms.RadioSelect(),
                  }
class Item4Form(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("Q4_1", "Q4_2", "Q4_3", "Q4_4", "Q4_5")
        widgets = {
                    "Q4_1": forms.RadioSelect(),
                    "Q4_2": forms.RadioSelect(),
                    "Q4_3": forms.RadioSelect(),
                    "Q4_4": forms.RadioSelect(),
                    "Q4_5": forms.RadioSelect(),
                  }
class Item5Form(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("Q5_1", "Q5_2", "Q5_3", "Q5_4", "Q5_5")
        widgets = {
                    "Q5_1": forms.RadioSelect(),
                    "Q5_2": forms.RadioSelect(),
                    "Q5_3": forms.RadioSelect(),
                    "Q5_4": forms.RadioSelect(),
                    "Q5_5": forms.RadioSelect(),
                  }
class Item6Form(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("Q6_1", "Q6_2", "Q6_3", "Q6_4", "Q6_5")
        widgets = {
                    "Q6_1": forms.RadioSelect(),
                    "Q6_2": forms.RadioSelect(),
                    "Q6_3": forms.RadioSelect(),
                    "Q6_4": forms.RadioSelect(),
                    "Q6_5": forms.RadioSelect(),
                  }
class Item11Form(forms.ModelForm):
    class Meta:
        model = Item1
        fields = ("Q1_1", "Q1_2", "Q1_3", "Q1_4", "Q1_5")
        widgets = {
                    "Q1_1": forms.RadioSelect(),
                    "Q1_2": forms.RadioSelect(),
                    "Q1_3": forms.RadioSelect(),
                    "Q1_4": forms.RadioSelect(),
                    "Q1_5": forms.RadioSelect(),
                  }
class Item12Form(forms.ModelForm):
    class Meta:
        model = Item1
        fields = ("Q2_1", "Q2_2", "Q2_3", "Q2_4", "Q2_5")
        widgets = {
                    "Q2_1": forms.RadioSelect(),
                    "Q2_2": forms.RadioSelect(),
                    "Q2_3": forms.RadioSelect(),
                    "Q2_4": forms.RadioSelect(),
                    "Q2_5": forms.RadioSelect(),
                  }
class Item13Form(forms.ModelForm):
    class Meta:
        model = Item1
        fields = ("Q3_1", "Q3_2", "Q3_3", "Q3_4", "Q3_5")
        widgets = {
                    "Q3_1": forms.RadioSelect(),
                    "Q3_2": forms.RadioSelect(),
                    "Q3_3": forms.RadioSelect(),
                    "Q3_4": forms.RadioSelect(),
                    "Q3_5": forms.RadioSelect(),
                  }
class Item14Form(forms.ModelForm):
    class Meta:
        model = Item1
        fields = ("Q4_1", "Q4_2", "Q4_3", "Q4_4", "Q4_5")
        widgets = {
                    "Q4_1": forms.RadioSelect(),
                    "Q4_2": forms.RadioSelect(),
                    "Q4_3": forms.RadioSelect(),
                    "Q4_4": forms.RadioSelect(),
                    "Q4_5": forms.RadioSelect(),
                  }
class Item15Form(forms.ModelForm):
    class Meta:
        model = Item1
        fields = ("Q5_1", "Q5_2", "Q5_3", "Q5_4", "Q5_5")
        widgets = {
                    "Q5_1": forms.RadioSelect(),
                    "Q5_2": forms.RadioSelect(),
                    "Q5_3": forms.RadioSelect(),
                    "Q5_4": forms.RadioSelect(),
                    "Q5_5": forms.RadioSelect(),
                  }
class Item16Form(forms.ModelForm):
    class Meta:
        model = Item1
        fields = ("Q6_1", "Q6_2", "Q6_3", "Q6_4", "Q6_5")
        widgets = {
                    "Q6_1": forms.RadioSelect(),
                    "Q6_2": forms.RadioSelect(),
                    "Q6_3": forms.RadioSelect(),
                    "Q6_4": forms.RadioSelect(),
                    "Q6_5": forms.RadioSelect(),
                  }
class Item21Form(forms.ModelForm):
    class Meta:
        model = Item2
        fields = ("Q1_1", "Q1_2", "Q1_3", "Q1_4", "Q1_5")
        widgets = {
                    "Q1_1": forms.RadioSelect(),
                    "Q1_2": forms.RadioSelect(),
                    "Q1_3": forms.RadioSelect(),
                    "Q1_4": forms.RadioSelect(),
                    "Q1_5": forms.RadioSelect(),
                  }
class Item22Form(forms.ModelForm):
    class Meta:
        model = Item2
        fields = ("Q2_1", "Q2_2", "Q2_3", "Q2_4", "Q2_5")
        widgets = {
                    "Q2_1": forms.RadioSelect(),
                    "Q2_2": forms.RadioSelect(),
                    "Q2_3": forms.RadioSelect(),
                    "Q2_4": forms.RadioSelect(),
                    "Q2_5": forms.RadioSelect(),
                  }
class Item23Form(forms.ModelForm):
    class Meta:
        model = Item2
        fields = ("Q3_1", "Q3_2", "Q3_3", "Q3_4", "Q3_5")
        widgets = {
                    "Q3_1": forms.RadioSelect(),
                    "Q3_2": forms.RadioSelect(),
                    "Q3_3": forms.RadioSelect(),
                    "Q3_4": forms.RadioSelect(),
                    "Q3_5": forms.RadioSelect(),
                  }
class Item24Form(forms.ModelForm):
    class Meta:
        model = Item2
        fields = ("Q4_1", "Q4_2", "Q4_3", "Q4_4", "Q4_5")
        widgets = {
                    "Q4_1": forms.RadioSelect(),
                    "Q4_2": forms.RadioSelect(),
                    "Q4_3": forms.RadioSelect(),
                    "Q4_4": forms.RadioSelect(),
                    "Q4_5": forms.RadioSelect(),
                  }
class Item25Form(forms.ModelForm):
    class Meta:
        model = Item2
        fields = ("Q5_1", "Q5_2", "Q5_3", "Q5_4", "Q5_5")
        widgets = {
                    "Q5_1": forms.RadioSelect(),
                    "Q5_2": forms.RadioSelect(),
                    "Q5_3": forms.RadioSelect(),
                    "Q5_4": forms.RadioSelect(),
                    "Q5_5": forms.RadioSelect(),
                  }
class Item26Form(forms.ModelForm):
    class Meta:
        model = Item2
        fields = ("Q6_1", "Q6_2", "Q6_3", "Q6_4", "Q6_5")
        widgets = {
                    "Q6_1": forms.RadioSelect(),
                    "Q6_2": forms.RadioSelect(),
                    "Q6_3": forms.RadioSelect(),
                    "Q6_4": forms.RadioSelect(),
                    "Q6_5": forms.RadioSelect(),
                  }
