from django.db import models

# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class District(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Upazila(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Cadre(models.Model):
    full_Name_EN = models.CharField(max_length=100)
    full_Name_BN = models.CharField(max_length=100)
    nick_Name = models.CharField(max_length=60)
    fathers_Name = models.CharField(max_length=100)
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    email = models.EmailField(max_length=255, unique=True)
    mobile_Number = models.CharField(max_length=11, unique=True)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    upazila = models.ForeignKey(Upazila, on_delete=models.SET_NULL, null=True)
    post_Code = models.PositiveSmallIntegerField()
    date_of_Birth = models.DateField()
    national_ID = models.IntegerField(unique=True)
    religion_choice = (
        ('Islam', 'Islam'),
        ('Hinduism', 'Hinduism'),
        ('Christianity', 'Christianity'),
        ('Buddhism', 'Buddhism'),
        ('Other', 'Other')
    )
    religion = models.CharField(max_length=45, choices=religion_choice)
    blood_group_choice = (
        ('A+', 'A+'),
        ('O+', 'O+'),
        ('B+', 'B+'),
        ('AB+', 'AB+'),
        ('A-', 'A-'),
        ('O-', 'O-'),
        ('B-', 'B-'),
        ('AB-', 'AB-')
    )
    blood_Group = models.CharField(choices=blood_group_choice, max_length=5)
    marital_status_choice = (
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
        ('Separated', 'Separated'),
        ('Divorced', 'Divorced'),
        ('Single', 'Single')
    )
    marital_Status = models.CharField(choices=marital_status_choice, max_length=10)
    bCS_Registration_No = models.PositiveSmallIntegerField()
    Merit_Position = models.PositiveSmallIntegerField(blank=True)
    posting_choice = (
        ('DAE HQ', 'DAE HQ'),
        ('Agriculture Training Institute (ATI)', 'Agriculture Training Institute (ATI)'),
        ('Horticulture Centre', 'Horticulture Centre'),
        ('Plant Quarantine Station', 'Plant Quarantine Stations'),
        ('National Agriculture Training Academy (NATA)', 'National Agriculture Training Academy (NATA)'),
        ('Agriculture Information Service (AIS)', 'Agriculture Information Service (AIS)'),
        ('Seed Certification Agency (SCA)', 'Seed Certification Agency (SCA)'),
        ('Other', 'Other')
    )
    desire_Posting_Place = models.CharField(choices=posting_choice, max_length=300)
    passing_year_choice = (
        ('1999', '1999'),
        ('2000', '2000'),
        ('2001', '2001'),
        ('2002', '2002'),
        ('2003', '2003'),
        ('2004', '2004'),
        ('2005', '2005'),
        ('2007', '2007'),
        ('2008', '2008'),
        ('2009', '2009'),
        ('2010', '2010'),
        ('2011', '2011'),
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
    )
    hSC_Passing_Year = models.IntegerField(choices=passing_year_choice)
    college_Name = models.CharField(max_length=200)
    graduation_Year = models.IntegerField(choices=passing_year_choice)
    university_choice = (
        ('Bangladesh Agricultural University', 'Bangladesh Agricultural University'),
        ('Hajee Mohammad Danesh Science and Technology University', 'Hajee Mohammad Danesh Science and Technology University'),
        ('Khulna University', 'Khulna University'),
        ('Noakhali Science and Technology University', 'Noakhali Science and Technology University'),
        ('Patuakhali Science & Technology University', 'Patuakhali Science & Technology University'),
        ('University of Rajshahi', 'University of Rajshahi'),
        ('Sher-e-Bangla Agricultural University', 'Sher-e-Bangla Agricultural University'),
        ('Sylhet Agricultural University', 'Sylhet Agricultural University'),
        ('Others', 'Others'),
    )
    university_Name = models.CharField(choices=university_choice, max_length=100)
    masters_Degree_if_any = models.CharField(max_length=255, blank=True)
    university_or_Institute = models.CharField(choices=university_choice, max_length=100, blank=True)
    previous_Job_if_any = models.CharField(max_length=255, blank=True)
    picture = models.ImageField(upload_to='images/', blank=True)


    def __str__(self):
        return self.nick_Name