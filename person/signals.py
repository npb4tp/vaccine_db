from person.models import Appointment, Supplier, Distributor, Patient, Vaccinator, Vaccine
from django.dispatch import receiver
from django.db.backends.signals import connection_created
from sys import argv

@receiver(connection_created)
def populate_database(sender, **kwargs):
    """Only works with empty database. 
        To clear database run the command "python manage.py flush" 
        This also deletes the superuser so you'll have to create a new one to 
        log into the admin page. """
    
    #check if there are suppliers
    if not Patient.objects.all().exists():
        pat1 = Patient(
            patient_fname = "Dummy",
            patient_lname = "Patient",
            patient_dob = "2000-01-01",
            patient_allergies = "N",
            patient_state = "Virginia",
            patient_zip = "00000",
            patient_city = "Charlottesville",
            patient_street = "321 N Sesame St",
            patient_phone = "4321112222",
            patient_partially_vacc = "N",
        )
        pat1.save()
    print("signal works")
