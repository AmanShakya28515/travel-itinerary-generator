from django.shortcuts import render, redirect
from .forms import TravelPlanForm

def create_travel_plan(request):
    if request.method == "POST":
        form = TravelPlanForm(request.POST)
        
        if form.is_valid():
            travel_plan = form.save(commit=False)  # Don't save yet, we need to assign the user
            travel_plan.user = request.user  # Assign the logged-in user to this travel plan
            travel_plan.save()  # Save the travel plan to the database
            
            return redirect('generate_itinerary', plan_id=travel_plan.id)  
    else:
        form = TravelPlanForm()  
    
    return render(request, 'create_travel_plan.html', {'form': form})


