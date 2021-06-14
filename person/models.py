from django.db import models

# Create your models here.
class Supplier(models.Model):
    supp_name = models.CharField(max_length=200, null=True)
    supp_num_doses = models.CharField(max_length=200, null=True)

class Distributor(models.Model):
    supp_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    dist_name = models.CharField(max_length=200,null=True)
    dist_phone = models.CharField(max_length=200, null=True)
    dist_num_doses = models.CharField(max_length=200, null=True)
    dist_state = models.CharField(max_length=200, null=True)
    dist_zip = models.CharField(max_length=200, null=True)
    dist_city = models.CharField(max_length=200, null=True)
    dist_street = models.CharField(max_length=200, null=True)

class Patient(models.Model):
    patient_fname = models.CharField(max_length=200, null=True)
    patient_lname = models.CharField(max_length=200, null=True)
    patient_dob = models.DateTimeField(default = '2000-01-01')
    patient_allergies = models.CharField(max_length=1, default="N")
    patient_state = models.CharField(max_length=200, null=True)
    patient_zip = models.CharField(max_length=200, null=True)
    patient_city = models.CharField(max_length=200, null=True)
    patient_street = models.CharField(max_length=200, null=True)
    patient_phone = models.CharField(max_length=200, null=True)
    patient_partially_vacc = models.CharField(max_length=1, default="N")

class Vaccinator(models.Model):
    vaccinator_fname = models.CharField(max_length=200, null=True)
    vaccinator_lname = models.CharField(max_length=200, null=True)
    vaccinator_occupation = models.CharField(max_length=200, null=True)
    vaccinator_phone = models.CharField(max_length=200, null=True)

class Vaccine(models.Model):
    vacc_brand = models.CharField(max_length=200, null=True)
    supp_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)

class Appointment(models.Model):
    app_start = models.DateTimeField(null=True)
    app_end = models.DateTimeField(null=True)
    app_state = models.CharField(max_length=200, null=True)
    app_zip = models.CharField(max_length=200, null=True)
    app_city = models.CharField(max_length=200, null=True)
    app_street = models.CharField(max_length=200, null=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    vaccinator_id = models.ForeignKey(Vaccinator, on_delete=models.CASCADE)
    vaccine_id = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    distributor_id = models.ForeignKey(Distributor, on_delete=models.CASCADE)







