from django import forms

class ShipmentForm(forms.Form):
    date = forms.DateTimeField(label="Date (mm/dd/yyyy)", required=True)
    tracking_number = forms.IntegerField(label="Tracking Number", min_value=1)
    total_price = forms.FloatField(label="Total Price", min_value=.01)
    service_level = forms.CharField(max_length=50, label="Service Level")
    destination = forms.CharField(max_length=50, label="Destination")
    ref_1 = forms.CharField(max_length=20, label="Ref 1")
    ref_2 = forms.CharField(max_length=20, label="Ref 2")
    weight = forms.FloatField(label="Weight", min_value=.01)
    def clean_date(self):
        data = self.cleaned_data['date']        
        return data
    def clean_tracking_number(self):
        data = self.cleaned_data['tracking_number']        
        return data
    def clean_total_price(self):
        data = self.cleaned_data['total_price']        
        return data
    def clean_service_level(self):
        data = self.cleaned_data['service_level']        
        return data
    def clean_destination(self):
        data = self.cleaned_data['destination']        
        return data
    def clean_ref_1(self):
        data = self.cleaned_data['ref_1']        
        return data
    def clean_ref_2(self):
        data = self.cleaned_data['ref_2']        
        return data
    def clean_weight(self):
        data = self.cleaned_data['weight']        
        return data
   
 


