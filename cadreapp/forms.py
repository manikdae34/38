from .models import Cadre
from django.forms import ModelForm
    

class CadreForm(ModelForm):
    
    class Meta:
        model = Cadre
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['district'].queryset = models.District.objects.none()

            if 'district' in self.data:
                try:
                    division_id = int(self.data.get('division'))
                    self.fields['district'].queryset = models.District.objects.filter(division_id=division_id).order_by('name')
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['district'].queryset = self.instance.division.district_set.order_by('name')

            self.fields['upazila'].queryset = models.Upazila.objects.none()

            if 'upazila' in self.data:
                try:
                    district_id = int(self.data.get('district'))
                    self.fields['upazila'].queryset = models.Upazila.objects.filter(district_id=district_id).order_by('name')
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['upazila'].queryset = self.instance.district.upazila_set.order_by('name')