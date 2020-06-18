from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length = 100, unique=True)
    rate_increase = models.DecimalField(decimal_places=2, max_digits=2)
    def __str__(self):
        return self.company_name
    

class Shipment(models.Model):
    user_name = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    tracking_number = models.IntegerField()
    total_price = models.FloatField()
    shipment_date = models.DateTimeField()    
    company_name = models.ForeignKey(Company, to_field="user", on_delete=models.CASCADE, related_name="companyname")
    service_level = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    ref_1 = models.CharField(max_length=20)
    ref_2 = models.CharField(max_length=20)
    weight = models.IntegerField()
    def __str__(self):
        return str(self.company_name) + ": " + str(self.tracking_number)   
    
    

