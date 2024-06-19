from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
    cpd_mnth_id = models.CharField(max_length=100)  # Assuming ID can be large, hence max_length=100
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1) # Check if this is necessary 'on_delete=models.CASCADE'
    cpd_dt = models.DateField()  # Assuming this is a date
    cluster_name_adjusted = models.CharField(max_length=100)  # Adjust max_length as needed
    mrch_catg_cd = models.CharField(max_length=10)  # Assuming this is a category code, adjust max_length as needed
    mrch_catg_rlup_nm = models.CharField(max_length=100)  # Adjust max_lngth as needed
    merchant = models.CharField(max_length=100)  # Adjust max_length as needed
    cp_flag = models.BooleanField()  # Assuming flag values are boolean
    domestic_flag = models.BooleanField()  # Assuming flag values are boolean
    intraregion_flag = models.BooleanField()  # Assuming flag values are boolean
    interregion_flag = models.BooleanField()  # Assuming flag values are boolean
    city_name = models.CharField(max_length=100, null=True, blank=True)  # City name can be empty, hence null=True, blank=True
    country_code = models.CharField(max_length=10)  # Adjust max_length as needed
    spend = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming spend is a decimal value

    def __str__(self):
        return f"{self.cpd_mnth_id} - {self.merchant}"
