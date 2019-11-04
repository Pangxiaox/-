from django.db import models
from django.contrib.auth.models import AbstractUser


class DoctorLogin(AbstractUser):
    docname = models.CharField(max_length=10)
    hosid = models.CharField(max_length=20)
    hosname = models.CharField(max_length=20)


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
    marriage = models.CharField(max_length=2, choices=MARRY_CHOICES)
    p_birthplace = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    medicalhistory_reporter = models.CharField(max_length=10)
    admission_date = models.DateField(null=True, blank=True)
    medicalhistory_recordtime = models.DateTimeField(null=True, blank=True)


class EssentialInformation(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    main_suit = models.TextField(null=True, blank=True)
    medicalhistory_present = models.TextField(null=True, blank=True)
    Y_N_CHOICES = (
        ('有', 'yes'),
        ('无', 'no'),
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
    smoking_hobbies = models.CharField(max_length=1, choices=Y_N_CHOICES)
    drinking_hobbies = models.CharField(max_length=1, choices=Y_N_CHOICES)
    epidemic_water_contact_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    personal_history_remark = models.TextField(null=True, blank=True)
    marital_reproductive_history_remark = models.TextField(null=True, blank=True)
    menopause = models.CharField(max_length=1, choices=Y_N_CHOICES)
    menstrual_history_remark = models.CharField(max_length=1, choices=Y_N_CHOICES)
    diabetes_mellitus_family_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    coronary_heart_disease_family_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    stroke_family_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    tumors_family_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    hypertension_family_history = models.CharField(max_length=1, choices=Y_N_CHOICES)
    family_history_remark = models.TextField(null=True, blank=True)


class PhysicalExamine(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    temperature = models.FloatField()
    pulse = models.IntegerField()
    respiratory_rate = models.IntegerField()  # R（呼吸频率)
    blood_pressure = models.IntegerField()  # Bp（血压）
    routine_info = models.TextField()  # 一般项目
    Y_N_CHOICES = (
        ('有', 'yes'),
        ('无', 'no'),
    )
    yellow_dye = models.CharField(max_length=1, choices=Y_N_CHOICES)
    lymphgland = models.CharField(max_length=1, choices=Y_N_CHOICES)  # 淋巴结肿大
    neck_info = models.TextField()
    face_info = models.TextField()  # 五官


class ChestExamine(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    Y_N_CHOICES = (
        ('有', 'yes'),
        ('无', 'no'),
    )
    chest_contour = models.CharField(max_length=1, choices=Y_N_CHOICES)  # 外形畸形
    respiratory_sounds = models.CharField(max_length=1, choices=Y_N_CHOICES)  # 肺呼吸音
    dryrale = models.CharField(max_length=1, choices=Y_N_CHOICES)  # 干啰音
    wetrale = models.CharField(max_length=1, choices=Y_N_CHOICES)  # 湿啰音
    heart_rate = models.IntegerField()  # 心率
    arrhythmia = models.CharField(max_length=1, choices=Y_N_CHOICES)  # 心律


class StomachExamine(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    Y_N_CHOICES = (
        ('有', 'yes'),
        ('无', 'no'),
    )
    abdomen_soft = models.CharField(max_length=1, choices=Y_N_CHOICES)  # 软
    abdomen_tenderness = models.CharField(max_length=1, choices=Y_N_CHOICES)  # 压痛
    abdomen_rebound_pain = models.CharField(max_length=1, choices=Y_N_CHOICES)  # 反跳痛
    subcostal_liver = models.CharField(max_length=1, choices=Y_N_CHOICES)  # 肝脏肋下触及
    subcostal_spleen = models.CharField(max_length=1, choices=Y_N_CHOICES)  # 脾脏肋下触及
    limb_joint = models.CharField(max_length=1, choices=Y_N_CHOICES)  # 四肢关节
    limb_movement = models.CharField(max_length=1, choices=Y_N_CHOICES)  # 四肢活动
    physiological_reflex = models.CharField(max_length=1, choices=Y_N_CHOICES)  # 生理反射
    pathological_reflex = models.CharField(max_length=1, choices=Y_N_CHOICES)  # 病理反射
    other_info = models.TextField(null=True, blank=True)


class EyeExamine(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    Y_N_CHOICES = (
        ('有', 'yes'),
        ('无', 'no'),
    )
    right_vision = models.FloatField(null=True, blank=True)
    left_vision = models.FloatField(null=True, blank=True)
    right_intraocularpressure = models.FloatField(null=True, blank=True)
    left_intraocularpressure = models.FloatField(null=True, blank=True)
    right_eyelid_edema = models.CharField(max_length=1, choices=Y_N_CHOICES)
    left_eyelid_edema = models.CharField(max_length=1, choices=Y_N_CHOICES)
    right_eyelid_flip = models.CharField(max_length=1, choices=Y_N_CHOICES)
    left_eyelid_flip = models.CharField(max_length=1, choices=Y_N_CHOICES)
    right_other_eyemovement = models.CharField(max_length=1, choices=Y_N_CHOICES)
    left_other_eyemovement = models.CharField(max_length=1, choices=Y_N_CHOICES)
    right_other_protrusion = models.CharField(max_length=1, choices=Y_N_CHOICES)
    left_other_protrusion = models.CharField(max_length=1, choices=Y_N_CHOICES)
    right_lacrimaapparatus_skinredness = models.CharField(max_length=1, choices=Y_N_CHOICES)
    left_lacrimaapparatus_skinredness = models.CharField(max_length=1, choices=Y_N_CHOICES)
    right_lacrimaapparatus_compression = models.CharField(max_length=1, choices=Y_N_CHOICES)
    left_lacrimaapparatus_compression = models.CharField(max_length=1, choices=Y_N_CHOICES)
    right_lacrimaapparatus_passage = models.CharField(max_length=1, choices=Y_N_CHOICES)
    left_lacrimaapparatus_passage = models.CharField(max_length=1, choices=Y_N_CHOICES)
    right_conjunctive = models.CharField(max_length=1, choices=Y_N_CHOICES)
    left_conjunctive = models.CharField(max_length=1, choices=Y_N_CHOICES)
    right_sclera = models.CharField(max_length=1, choices=Y_N_CHOICES)
    left_sclera = models.CharField(max_length=1, choices=Y_N_CHOICES)
    right_corneal_transparency = models.CharField(max_length=1, choices=Y_N_CHOICES)
    left_corneal_transparency = models.CharField(max_length=1, choices=Y_N_CHOICES)
    right_anteriorchamber_central = models.FloatField(null=True, blank=True)
    left_anteriorchamber_central = models.FloatField(null=True, blank=True)
    right_anteriorchamber_surrounded = models.FloatField(null=True, blank=True)
    left_anteriorchamber_surrounded = models.FloatField(null=True, blank=True)
    right_anteriorchamber_waterproof = models.CharField(max_length=1, choices=Y_N_CHOICES)
    left_anteriorchamber_waterproof = models.CharField(max_length=1, choices=Y_N_CHOICES)
    right_iris = models.CharField(max_length=1, choices=Y_N_CHOICES)
    left_iris = models.CharField(max_length=1, choices=Y_N_CHOICES)
    right_pupil_diameter = models.FloatField(null=True, blank=True)
    left_pupil_diameter = models.FloatField(null=True, blank=True)
    right_pupil_lightreflection = models.CharField(max_length=1, choices=Y_N_CHOICES)
    left_pupil_lightreflection = models.CharField(max_length=1, choices=Y_N_CHOICES)
    right_fundusoculi_detailinform = models.TextField(null=True, blank=True)
    left_fundusoculi_detailinform = models.TextField(null=True, blank=True)
    right_lens = models.TextField(null=True, blank=True)
    left_lens = models.TextField(null=True, blank=True)  # 晶状体
    right_vitreum = models.TextField(null=True, blank=True)
    left_vitreum = models.TextField(null=True, blank=True)  # 玻璃体


class DiagnosticReports(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    Y_N_CHOICES = (
        ('有', 'yes'),
        ('无', 'no'),
    )
    seriousDegree = models.IntegerField(max_length=1)
    treatNeed = models.CharField(max_length=1, choices=Y_N_CHOICES)
    diaResult = models.TextField(null=True, blank=True)
    Doctor = models.CharField(max_length=20)
    Director = models.CharField(max_length=20)
    reportTime = models.DateTimeField(null=True, blank=True)


# 下面几个信息与上面部分信息有重复，是否采用上面的字段待确定
class Patient(models.Model):
    id = models.CharField(max_length=15, primary_key=True)  # 病人ID
    pname = models.CharField(max_length=60)  # 病人姓名
    pvillage = models.CharField(max_length=60)  # 病人所在村
    presult = models.CharField(max_length=10)  # 病人诊断结果


class Village(models.Model):
    v_id = models.CharField(max_length=20, primary_key=True)  # 村ID
    vname = models.CharField(max_length=60)
    vdetailaddress = models.CharField(max_length=60)
    vleadingname = models.CharField(max_length=60)
    vleadingtel = models.CharField(max_length=30)
    vorderedtime = models.DateField()
    vmessage = models.TextField()