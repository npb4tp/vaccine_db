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
    if not Supplier.objects.all().exists():
        supp1 = Supplier(
            supp_name = "US Government",
            supp_num_doses = "100000"
        )
        supp1.save()
        supp2 = Supplier(
            supp_name = "Pfizer",
            supp_num_doses = "5000000"
        )
        supp2.save()

    if not Patient.objects.all().exists():
        pat1 = Patient(
            patient_fname = "James",
            patient_lname = "Bond",
            patient_dob = "1995-05-11",
            patient_allergies = "Y",
            patient_state = "Virginia",
            patient_zip = "22203",
            patient_city = "Arlington",
            patient_street = "321 N Sesame St",
            patient_phone = "4321112222",
            patient_partially_vacc = "Y",
        )
        pat1.save()
        pat2 = Patient(
            patient_fname = "Barry",
            patient_lname = "Allen",
            patient_dob = "1988-12-12",
            patient_allergies = "N",
            patient_state = "New York",
            patient_zip = "43232",
            patient_city = "Brooklyn",
            patient_street = "1313 Timesquare",
            patient_phone = "1231231233",
            patient_partially_vacc = "N",
        )
        pat2.save()
        pat3 = Patient(
            patient_fname = "Naruto",
            patient_lname = "Uzumaki",
            patient_dob = "2005-05-04",
            patient_allergies = "Y",
            patient_state = "California",
            patient_zip = "99090",
            patient_city = "San Diego",
            patient_street = "921 Hidden Leaf",
            patient_phone = "5551239999",
            patient_partially_vacc = "N",
        )
        pat3.save()
        pat4 = Patient(
            patient_fname = "Michael",
            patient_lname = "Scott",
            patient_dob = "1979-05-11",
            patient_allergies = "Y",
            patient_state = "Pennsylvania",
            patient_zip = "43440",
            patient_city = "Scantron",
            patient_street = "400 Scantron Avenue",
            patient_phone = "7032214876",
            patient_partially_vacc = "Y",
        )
        pat4.save()

    if not Vaccinator.objects.all().exists():
        doc1 = Vaccinator(
            vaccinator_fname = "Bill",
            vaccinator_lname = "Nye",
            vaccinator_occupation = "Scientist",
            vaccinator_phone = "2227034121"
        )
        doc1.save()
        doc2 = Vaccinator(
            vaccinator_fname = "Lil",
            vaccinator_lname = "Uzi",
            vaccinator_occupation = "Pharmacist",
            vaccinator_phone = "3738473111"
        )
        doc2.save()
        doc3 = Vaccinator(
            vaccinator_fname = "Jason",
            vaccinator_lname = "Derulo",
            vaccinator_occupation = "Nurse",
            vaccinator_phone = "4352329988"
        )
        doc3.save()

    supp1 = Supplier.objects.get(pk=1)
    supp2 = Supplier.objects.get(pk=2)

    if not Vaccine.objects.all().exists():
        vac1 = Vaccine(
            vacc_brand = "Pfizer",
            supp_id = supp2
        )
        vac1.save()

        vac2 = Vaccine(
            vacc_brand = "Moderna",
            supp_id = supp1
        )
        vac2.save()

    if not Distributor.objects.all().exists() and Supplier.objects.all().exists():
        dis1 = Distributor(
            supp_id = supp1,
            dist_name = "Walmart",
            dist_phone = "4349731412",
            dist_num_doses = "1000",
            dist_state = "Virginia",
            dist_zip = "22901",
            dist_city = "Charlottesville",
            dist_street = "975 Hilton Heights Rd"
        )
        dis1.save()

        dis2 = Distributor(
            supp_id = supp2,
            dist_name = "CVS",
            dist_phone = "4342444028",
            dist_num_doses = "500",
            dist_state = "Virginia",
            dist_zip = "22903",
            dist_city = "Charlottesville",
            dist_street = "1417 25 University Ave"
        )
        dis2.save()

        dis3 = Distributor(
            supp_id = supp2,
            dist_name = "Rite Aid",
            dist_phone = "5404347341",
            dist_num_doses = "250",
            dist_state = "Virginia",
            dist_zip = "22801",
            dist_city = "Harrisonburg",
            dist_street = "1588 down, S Main St"
        )
        dis3.save()
        

    print("signal works")
