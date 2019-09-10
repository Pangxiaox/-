from django.db import models


class PersonalInformation(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    SEX_CHOICES = (
        ('男', 'male'),
        ('女', 'female'),
    )
    sex = models.CharField(max_length=2, choices=SEX_CHOICES)
    nation = models.CharField(max_length=10)
    occupation = models.CharField(max_length=10)
    MARRY_CHOICES = (
        ('已婚', 'true'),
        ('未婚', 'false'),
    )
    marriage = models.CharField(max_length=10, choices=MARRY_CHOICES)
    birthplace = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    medicalhistory_reporter = models.CharField(max_length=10)
    admission_date = models.DateField()
    medicalhistory_recordtime = models.DateTimeField()


class EssentialInformation(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    main_suit = models.TextField()
    medicalhistory_present = models.TextField()
    Y_N_CHOICES = (
        ('是', 'yes'),
        ('否', 'no'),
    )
    tuberculosis_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    hepatitis_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    other_infectious_diseases_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    chronic_disease_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    hypertension_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    diabetes_mellitus_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    heart_disease_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    vaccination_allergy_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    surgery_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    past_history_remarks = models.TextField(null=True, blank=True)
    birthplace = models.CharField(max_length=30)
    smoking_hobbies = models.CharField(max_length=1, choices=Y_N_CHOICES)
    drinking_hobbies = models.CharField(max_length=1, choices=Y_N_CHOICES)
    epidemic_water_contact_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    personal_history_remark = models.TextField(null=True, blank=True)
    MARRY_CHOICES = (
        ('已婚', 'true'),
        ('未婚', 'false'),
    )
    marriage = models.CharField(max_length=1, choices=MARRY_CHOICES)
    marital_reproductive_history_remark = models.TextField(null=True, blank=True)
    menopause = models.CharField(max_length=1, choices=Y_N_CHOICES)
    menstrual_history_remark = models.CharField(max_length=1, choices=Y_N_CHOICES)
    diabetes_mellitus_family_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    coronary_heart_disease_family_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    stroke_family_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    tumors_family_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    hypertension_family_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    family_history_remark = models.TextField(null=True, blank=True)
