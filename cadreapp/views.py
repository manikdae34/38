from django.shortcuts import render, redirect
from .models import Cadre, Division, District, Upazila
from .forms import CadreForm

# Create your views here.
def load_district(request):
    division_id = request.GET.get('division')
    district = District.objects.filter(division_id=division_id).order_by('name')

    district_id = request.GET.get('district')
    upazila = Upazila.objects.filter(district_id=district_id).order_by('name')
    context = {
        'district': district,
        'upazila': upazila
    }
    return render(request, 'district_dropdown_list_options.html', context)

    
def Index(request):
    form = CadreForm()

    if request.method == 'POST':
        form = CadreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
         'form': form
     }
    return render(request, 'registration_form.html', context)