from django import forms
from .models import TravelPlan,District

class TravelPlanForm(forms.ModelForm):
    destination = forms.ModelChoiceField(
        queryset=District.objects.all(),
        empty_label="Select Destination",
        widget=forms.Select(attrs={'class': 'form-control'})

    )
    
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})

    
    )
    budget_category = forms.ChoiceField(
        choices=[('Low', 'Low'), ('Mid', 'Mid'), ('High', 'High')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Current destination form field (optional)
    current_destination = forms.ModelChoiceField(
        queryset=District.objects.all(),
        required=False,  # Not required, users can leave it blank
        empty_label="Current Location",
        widget=forms.Select(attrs={'class': 'form-control'})
        
    )




    class Meta:
        model=TravelPlan
        fields = ['destination', 'current_destination', 'start_date', 'end_date', 'budget_category']