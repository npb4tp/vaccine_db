from django.db import models

# Create your models here.
class Supplier(models.Model):
    supp_name = models.CharField(max_length=200, default="None")
    supp_num_doses = models.CharField(max_length=200, default="None")

class Distributor(models.Model):
    supp_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    dist_name = models.CharField(max_length=200, default="None")
    dist_phone = models.CharField(max_length=200, default="None")
    dist_num_doses = models.CharField(max_length=200, default="None")
    dist_state = models.CharField(max_length=200, default="None")
    dist_zip = models.CharField(max_length=200, default="None")
    dist_city = models.CharField(max_length=200, default="None")
    dist_street = models.CharField(max_length=200, default="None")

class Patient(models.Model):
    patient_fname = models.CharField(max_length=200, default="None")
    patient_lname = models.CharField(max_length=200, default="None")
    patient_dob = models.DateTimeField(default = '2000-01-01')
    patient_allergies = models.CharField(max_length=1, default="N")
    patient_state = models.CharField(max_length=200, default="None")
    patient_zip = models.CharField(max_length=200, default="None")
    patient_city = models.CharField(max_length=200, default="None")
    patient_street = models.CharField(max_length=200, default="None")
    patient_phone = models.CharField(max_length=200, default="None")
    patient_partially_vacc = models.CharField(max_length=1, default="N")

class Vaccinator(models.Model):
    vaccinator_fname = models.CharField(max_length=200, default="None")
    vaccinator_lname = models.CharField(max_length=200, default="None")
    vaccinator_occupation = models.CharField(max_length=200, default="None")
    vaccinator_phone = models.CharField(max_length=200, default="None") 

class Vaccine(models.Model):
    vacc_brand = models.CharField(max_length=200, default="None")
    supp_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)  

class Appointment(models.Model):
    app_start = models.DateTimeField(null=True)
    app_end = models.DateTimeField(null=True)
    app_state = models.CharField(max_length=200, default="None")
    app_zip = models.CharField(max_length=200, default="None")
    app_city = models.CharField(max_length=200, default="None")
    app_street = models.CharField(max_length=200, default="None")
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    vaccinator_id = models.ForeignKey(Vaccinator, on_delete=models.CASCADE)
    vaccine_id = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    distributor_id = models.ForeignKey(Distributor, on_delete=models.CASCADE)







