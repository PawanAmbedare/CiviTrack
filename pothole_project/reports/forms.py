from django import forms
from .models import PotholeReport

class PotholeReportForm(forms.ModelForm):
    class Meta:
        model = PotholeReport
        fields = ['title', 'description', 'image', 'severity', 'latitude', 'longitude']
        widgets = {
            'description': forms.Textarea(attrs={'rows':4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        base_class = 'form-control'
        for fname, field in self.fields.items():
            # apply form-control class to all non-file inputs
            if isinstance(field.widget, forms.FileInput):
                field.widget.attrs.update({'class': 'file-input'})
            else:
                field.widget.attrs.update({'class': base_class})
        # hide latitude/longitude visually (they are still inputs)
        self.fields['latitude'].widget.attrs.update({'type': 'hidden', 'id': 'id_latitude'})
        self.fields['longitude'].widget.attrs.update({'type': 'hidden', 'id': 'id_longitude'})

    def clean(self):
        cleaned = super().clean()
        lat = cleaned.get('latitude')
        lng = cleaned.get('longitude')
        if (lat is None) ^ (lng is None):
            raise forms.ValidationError('Please select a location on the map (both latitude and longitude).')
        if lat is not None:
            if not (-90 <= float(lat) <= 90):
                self.add_error('latitude','Latitude must be between -90 and 90')
        if lng is not None:
            if not (-180 <= float(lng) <= 180):
                self.add_error('longitude','Longitude must be between -180 and 180')
        return cleaned
