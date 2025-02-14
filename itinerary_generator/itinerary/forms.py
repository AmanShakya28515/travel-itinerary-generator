from django import forms
from .models import TravelPlan,District

class TravelPlanForm(forms.ModelForm):
    destination = forms.ModelChoiceField(
        queryset=District.objects.all(),
        empty_label="Select Destination",
        widget=forms.Select(attrs={'class': 'form-control'})

    )
    
    startdate = forms.DateField(
        widget=forms.DateInput(attrs='type'='date','class'= 'form-control')
    )




    class Meta:
        model=TravelPlan
        fields = ['destination', 'current_destination', 'start_date', 'end_date', 'budget_category']