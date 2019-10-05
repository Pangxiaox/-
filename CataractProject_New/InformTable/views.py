from django.shortcuts import render, redirect
from InformTable.models import PersonalInformation, EssentialInformation, DoctorLogin, EyeExamine, DiagnosticReports
from django.contrib.auth.models import User
from InformTable.models import Patient, Village
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def postdiagnose(request):
    info = PersonalInformation()
    info2 = EssentialInformation()
    info6 = EyeExamine()
    info8 = DiagnosticReports()

    if request.POST:
        info.id = request.POST.get("id")
        info.name = request.POST.get("name")
        info.age = request.POST.get("age")
        info.sex = request.POST.get("sex")
        info.nation = request.POST.get("nation")
        info.marriage = request.POST.get("marriage")
        info.occupation = request.POST.get("occupation")
        info.p_birthplace = request.POST.get("p_birthplace")
        info.address = request.POST.get("address")
        info.medicalhistory_reporter = request.POST.get("medicalhistory_reporter")
        info.admission_date = request.POST.get("admission_date")
        info.medicalhistory_recordtime = request.POST.get("medicalhistory_recordtime")
        info.save()

        info2.id = request.POST.get("id")
        info2.main_suit = request.POST.get("main_suit")
        info2.medicalhistory_present = request.POST.get("medicalhistory_present")
        info2.tuberculosis_history = request.POST.get("tuberculosis_history")
        info2.hepatitis_history = request.POST.get("hepatitis_history")
        info2.other_infectious_diseases_history = request.POST.get("other_infectious_diseases_history")
        info2.hypertension_history = request.POST.get("hypertension_history")
        info2.diabetes_mellitus_history = request.POST.get("diabetes_mellitus_history")
        info2.chronic_disease_history = request.POST.get("chronic_disease_history")
        info2.heart_disease_history = request.POST.get("heart_disease_history")
        info2.vaccination_allergy_history = request.POST.get("vaccination_allergy_history")
        info2.surgery_history = request.POST.get("surgery_history")
        info2.past_history_remarks = request.POST.get("past_history_remarks")
        info2.e_birthplace = request.POST.get("e_birthplace")
        info2.smoking_hobbies = request.POST.get("smoking_hobbies")
        info2.drinking_hobbies = request.POST.get("drinking_hobbies")
        info2.epidemic_water_contact_history = request.POST.get("epidemic_water_contact_history")
        info2.personal_history_remark = request.POST.get("personal_history_remark")
        info2.marriage_history = request.POST.get("marriage_history")
        info2.marital_reproductive_history_remark = request.POST.get("marital_reproductive_history_remark")
        info2.menopause = request.POST.get("menopause")
        info2.menstrual_history_remark = request.POST.get("menstrual_history_remark")
        info2.diabetes_mellitus_family_history = request.POST.get("diabetes_mellitus_family_history")
        info2.coronary_heart_disease_family_history = request.POST.get("coronary_heart_disease_family_history")
        info2.stroke_family_history = request.POST.get("stroke_family_history")
        info2.tumors_family_history = request.POST.get("tumors_family_history")
        info2.hypertension_family_history = request.POST.get("hypertension_family_history")
        info2.family_history_remark = request.POST.get("family_history_remark")
        info2.save()

        info6.id = request.POST.get("id")
        info6.right_vision = request.POST.get("right_vision")
        info6.left_vision = request.POST.get("left_vision")
        info6.right_intraocularpressure = request.POST.get("right_intraocularpressure")
        info6.left_intraocularpressure = request.POST.get("left_intraocularpressure")
        info6.right_eyelid_edema = request.POST.get("right_eyelid_edema")
        info6.left_eyelid_edema = request.POST.get("left_eyelid_edema")
        info6.right_eyelid_flip = request.POST.get("right_eyelid_flip")
        info6.left_eyelid_flip = request.POST.get("left_eyelid_flip")
        info6.right_other_eyemovement = request.POST.get("right_other_eyemovement")
        info6.left_other_eyemovement = request.POST.get("left_other_eyemovement")
        info6.right_other_protrusion = request.POST.get("right_other_protrusion")
        info6.left_other_protrusion = request.POST.get("left_other_protrusion")
        info6.right_lacrimaapparatus_skinredness = request.POST.get("right_lacrimaapparatus_skinredness")
        info6.left_lacrimaapparatus_skinredness = request.POST.get("left_lacrimaapparatus_skinredness")
        info6.right_lacrimaapparatus_compression = request.POST.get("right_lacrimaapparatus_compression")
        info6.left_lacrimaapparatus_compression = request.POST.get("left_lacrimaapparatus_compression")
        info6.right_lacrimaapparatus_passage = request.POST.get("right_lacrimaapparatus_passage")
        info6.left_lacrimaapparatus_passage = request.POST.get("left_lacrimaapparatus_passage")
        info6.right_conjunctive = request.POST.get("right_conjunctive")
        info6.left_conjunctive = request.POST.get("left_conjunctive")
        info6.right_sclera = request.POST.get("right_sclera")
        info6.left_sclera = request.POST.get("left_sclera")
        info6.right_corneal_transparency = request.POST.get("right_corneal_transparency")
        info6.left_corneal_transparency = request.POST.get("left_corneal_transparency")
        info6.right_anteriorchamber_central = request.POST.get("right_anteriorchamber_central")
        info6.left_anteriorchamber_central = request.POST.get("left_anteriorchamber_central")
        info6.right_anteriorchamber_surrounded = request.POST.get("right_anteriorchamber_surrounded")
        info6.left_anteriorchamber_surrounded = request.POST.get("left_anteriorchamber_surrounded")
        info6.right_anteriorchamber_waterproof = request.POST.get("right_anteriorchamber_waterproof")
        info6.left_anteriorchamber_waterproof = request.POST.get("left_anteriorchamber_waterproof")
        info6.right_iris = request.POST.get("right_iris")
        info6.left_iris = request.POST.get("left_iris")
        info6.right_pupil_diameter = request.POST.get("right_pupil_diameter")
        info6.left_pupil_diameter = request.POST.get("left_pupil_diameter")
        info6.right_pupil_lightreflection = request.POST.get("right_pupil_lightreflection")
        info6.left_pupil_lightreflection = request.POST.get("left_pupil_lightreflection")
        info6.right_fundusoculi_detailinform = request.POST.get("right_fundusoculi_detailinform")
        info6.left_fundusoculi_detailinform = request.POST.get("left_fundusoculi_detailinform")
        info6.right_lens = request.POST.get("right_lens")
        info6.left_lens = request.POST.get("left_lens")
        info6.right_vitreum = request.POST.get("right_vitreum")
        info6.left_vitreum = request.POST.get("left_vitreum")
        info6.save()

        info8.id = request.POST.get("id")
        info8.seriousDegree = request.POST.get("seriousDegree")
        info8.treatNeed = request.POST.get("treatNeed")
        info8.diaResult = request.POST.get("diaResult")
        info8.Doctor = request.POST.get("Doctor")
        info8.Director = request.POST.get("Director")
        info8.reportTime = request.POST.get("reportTime")
        info8.save()

        return redirect("/patientslist")
    return render(request, "DetailInform.html")


# old method
@login_required
def showpatientlist(request):
    patientlist = PersonalInformation.objects.all()
    return render(request, "PatientsList.html", {"p_list": patientlist})


@login_required
def deletediagnose(request, id):
    personal_info_obj = PersonalInformation.objects
    essential_info_obj = EssentialInformation.objects
    eyeexamine_info_obj = EyeExamine.objects
    diagnosticreport_info_obj = DiagnosticReports.objects
    personal_info_obj.filter(id=id).delete()
    essential_info_obj.filter(id=id).delete()
    eyeexamine_info_obj.filter(id=id).delete()
    diagnosticreport_info_obj.filter(id=id).delete()

    return redirect("/patientslist")


@login_required
def editdiagnose(request, id):
    personal_info = PersonalInformation.objects.get(id=id)
    essential_info = EssentialInformation.objects.get(id=id)
    eyeexamine_info = EyeExamine.objects.get(id=id)
    diagnosticreport_info = DiagnosticReports.objects.get(id=id)
    if request.method == "GET":
        return render(request, "EditInform.html", {"personal_info": personal_info, "essential_info": essential_info, "eyeexamine_info": eyeexamine_info, "diagnosticreport_info": diagnosticreport_info})
    else:

        # part 1
        name = request.POST.get("name")
        age = request.POST.get("age")
        sex = request.POST.get("sex")
        nation = request.POST.get("nation")
        marriage = request.POST.get("marriage")
        occupation = request.POST.get("occupation")
        p_birthplace = request.POST.get("p_birthplace")
        address = request.POST.get("address")
        medicalhistory_reporter = request.POST.get("medicalhistory_reporter")

        p_info = PersonalInformation.objects.filter(id=id)  # 返回的是一个对象列表,QuerySet

        p_info.update(age=age)
        p_info.update(name=name)
        p_info.update(sex=sex)
        p_info.update(nation=nation)
        p_info.update(marriage=marriage)
        p_info.update(occupation=occupation)
        p_info.update(p_birthplace=p_birthplace)
        p_info.update(address=address)
        p_info.update(medicalhistory_reporter=medicalhistory_reporter)

        # part 2
        main_suit = request.POST.get("main_suit")
        medicalhistory_present = request.POST.get("medicalhistory_present")
        tuberculosis_history = request.POST.get("tuberculosis_history")
        hepatitis_history = request.POST.get("hepatitis_history")
        other_infectious_diseases_history = request.POST.get("other_infectious_diseases_history")
        hypertension_history = request.POST.get("hypertension_history")
        diabetes_mellitus_history = request.POST.get("diabetes_mellitus_history")
        chronic_disease_history = request.POST.get("chronic_disease_history")
        heart_disease_history = request.POST.get("heart_disease_history")
        vaccination_allergy_history = request.POST.get("vaccination_allergy_history")
        surgery_history = request.POST.get("surgery_history")
        past_history_remarks = request.POST.get("past_history_remarks")
        smoking_hobbies = request.POST.get("smoking_hobbies")
        drinking_hobbies = request.POST.get("drinking_hobbies")
        epidemic_water_contact_history = request.POST.get("epidemic_water_contact_history")
        personal_history_remark = request.POST.get("personal_history_remark")
        marital_reproductive_history_remark = request.POST.get("marital_reproductive_history_remark")
        menopause = request.POST.get("menopause")
        menstrual_history_remark = request.POST.get("menstrual_history_remark")
        diabetes_mellitus_family_history = request.POST.get("diabetes_mellitus_family_history")
        coronary_heart_disease_family_history = request.POST.get("coronary_heart_disease_family_history")
        stroke_family_history = request.POST.get("stroke_family_history")
        tumors_family_history = request.POST.get("tumors_family_history")
        hypertension_family_history = request.POST.get("hypertension_family_history")
        family_history_remark = request.POST.get("family_history_remark")

        e_info = EssentialInformation.objects.filter(id=id)

        e_info.update(main_suit=main_suit)
        e_info.update(medicalhistory_present=medicalhistory_present)
        e_info.update(tuberculosis_history=tuberculosis_history)
        e_info.update(hepatitis_history=hepatitis_history)
        e_info.update(other_infectious_diseases_history=other_infectious_diseases_history)
        e_info.update(hypertension_history=hypertension_history)
        e_info.update(diabetes_mellitus_history=diabetes_mellitus_history)
        e_info.update(chronic_disease_history=chronic_disease_history)
        e_info.update(heart_disease_history=heart_disease_history)
        e_info.update(vaccination_allergy_history=vaccination_allergy_history)
        e_info.update(surgery_history=surgery_history)
        e_info.update(past_history_remarks=past_history_remarks)
        e_info.update(smoking_hobbies=smoking_hobbies)
        e_info.update(drinking_hobbies=drinking_hobbies)
        e_info.update(epidemic_water_contact_history=epidemic_water_contact_history)
        e_info.update(personal_history_remark=personal_history_remark)
        e_info.update(marital_reproductive_history_remark=marital_reproductive_history_remark)
        e_info.update(menopause=menopause)
        e_info.update(menstrual_history_remark=menstrual_history_remark)
        e_info.update(diabetes_mellitus_family_history=diabetes_mellitus_family_history)
        e_info.update(coronary_heart_disease_family_history=coronary_heart_disease_family_history)
        e_info.update(stroke_family_history=stroke_family_history)
        e_info.update(tumors_family_history=tumors_family_history)
        e_info.update(hypertension_family_history=hypertension_family_history)
        e_info.update(family_history_remark=family_history_remark)

        # part 6
        right_vision = request.POST.get("right_vision")
        left_vision = request.POST.get("left_vision")
        right_intraocularpressure = request.POST.get("right_intraocularpressure")
        left_intraocularpressure = request.POST.get("left_intraocularpressure")
        right_eyelid_edema = request.POST.get("right_eyelid_edema")
        left_eyelid_edema = request.POST.get("left_eyelid_edema")
        right_eyelid_flip = request.POST.get("right_eyelid_flip")
        left_eyelid_flip = request.POST.get("left_eyelid_flip")
        right_other_eyemovement = request.POST.get("right_other_eyemovement")
        left_other_eyemovement = request.POST.get("left_other_eyemovement")
        right_other_protrusion = request.POST.get("right_other_protrusion")
        left_other_protrusion = request.POST.get("left_other_protrusion")
        right_lacrimaapparatus_skinredness = request.POST.get("right_lacrimaapparatus_skinredness")
        left_lacrimaapparatus_skinredness = request.POST.get("left_lacrimaapparatus_skinredness")
        right_lacrimaapparatus_compression = request.POST.get("right_lacrimaapparatus_compression")
        left_lacrimaapparatus_compression = request.POST.get("left_lacrimaapparatus_compression")
        right_lacrimaapparatus_passage = request.POST.get("right_lacrimaapparatus_passage")
        left_lacrimaapparatus_passage = request.POST.get("left_lacrimaapparatus_passage")
        right_conjunctive = request.POST.get("right_conjunctive")
        left_conjunctive = request.POST.get("left_conjunctive")
        right_sclera = request.POST.get("right_sclera")
        left_sclera = request.POST.get("left_sclera")
        right_corneal_transparency = request.POST.get("right_corneal_transparency")
        left_corneal_transparency = request.POST.get("left_corneal_transparency")
        right_anteriorchamber_central = request.POST.get("right_anteriorchamber_central")
        left_anteriorchamber_central = request.POST.get("left_anteriorchamber_central")
        right_anteriorchamber_surrounded = request.POST.get("right_anteriorchamber_surrounded")
        left_anteriorchamber_surrounded = request.POST.get("left_anteriorchamber_surrounded")
        right_anteriorchamber_waterproof = request.POST.get("right_anteriorchamber_waterproof")
        left_anteriorchamber_waterproof = request.POST.get("left_anteriorchamber_waterproof")
        right_iris = request.POST.get("right_iris")
        left_iris = request.POST.get("left_iris")
        right_pupil_diameter = request.POST.get("right_pupil_diameter")
        left_pupil_diameter = request.POST.get("left_pupil_diameter")
        right_pupil_lightreflection = request.POST.get("right_pupil_lightreflection")
        left_pupil_lightreflection = request.POST.get("left_pupil_lightreflection")
        right_fundusoculi_detailinform = request.POST.get("right_fundusoculi_detailinform")
        left_fundusoculi_detailinform = request.POST.get("left_fundusoculi_detailinform")
        right_lens = request.POST.get("right_lens")
        left_lens = request.POST.get("left_lens")
        right_vitreum = request.POST.get("right_vitreum")
        left_vitreum = request.POST.get("left_vitreum")

        eye_info = EyeExamine.objects.filter(id=id)

        eye_info.update(right_vision=right_vision)
        eye_info.update(left_vision=left_vision)
        eye_info.update(right_intraocularpressure=right_intraocularpressure)
        eye_info.update(left_intraocularpressure=left_intraocularpressure)
        eye_info.update(right_eyelid_edema=right_eyelid_edema)
        eye_info.update(left_eyelid_edema=left_eyelid_edema)
        eye_info.update(right_eyelid_flip=right_eyelid_flip)
        eye_info.update(left_eyelid_flip=left_eyelid_flip)
        eye_info.update(right_other_eyemovement=right_other_eyemovement)
        eye_info.update(left_other_eyemovement=left_other_eyemovement)
        eye_info.update(right_other_protrusion=right_other_protrusion)
        eye_info.update(left_other_protrusion=left_other_protrusion)
        eye_info.update(right_lacrimaapparatus_skinredness=right_lacrimaapparatus_skinredness)
        eye_info.update(left_lacrimaapparatus_skinredness=left_lacrimaapparatus_skinredness)
        eye_info.update(right_lacrimaapparatus_compression=right_lacrimaapparatus_compression)
        eye_info.update(left_lacrimaapparatus_compression=left_lacrimaapparatus_compression)
        eye_info.update(right_lacrimaapparatus_passage=right_lacrimaapparatus_passage)
        eye_info.update(left_lacrimaapparatus_passage=left_lacrimaapparatus_passage)
        eye_info.update(right_conjunctive=right_conjunctive)
        eye_info.update(left_conjunctive=left_conjunctive)
        eye_info.update(right_sclera=right_sclera)
        eye_info.update(left_sclera=left_sclera)
        eye_info.update(right_corneal_transparency=right_corneal_transparency)
        eye_info.update(left_corneal_transparency=left_corneal_transparency)
        eye_info.update(right_anteriorchamber_central=right_anteriorchamber_central)
        eye_info.update(left_anteriorchamber_central=left_anteriorchamber_central)
        eye_info.update(right_anteriorchamber_surrounded=right_anteriorchamber_surrounded)
        eye_info.update(left_anteriorchamber_surrounded=left_anteriorchamber_surrounded)
        eye_info.update(right_anteriorchamber_waterproof=right_anteriorchamber_waterproof)
        eye_info.update(left_anteriorchamber_waterproof=left_anteriorchamber_waterproof)
        eye_info.update(right_iris=right_iris)
        eye_info.update(left_iris=left_iris)
        eye_info.update(right_pupil_diameter=right_pupil_diameter)
        eye_info.update(left_pupil_diameter=left_pupil_diameter)
        eye_info.update(right_pupil_lightreflection=right_pupil_lightreflection)
        eye_info.update(left_pupil_lightreflection=left_pupil_lightreflection)
        eye_info.update(right_fundusoculi_detailinform=right_fundusoculi_detailinform)
        eye_info.update(left_fundusoculi_detailinform=left_fundusoculi_detailinform)
        eye_info.update(right_lens=right_lens)
        eye_info.update(left_lens=left_lens)
        eye_info.update(right_vitreum=right_vitreum)
        eye_info.update(left_vitreum=left_vitreum)

        # part 8
        seriousDegree = request.POST.get("seriousDegree")
        treatNeed = request.POST.get("treatNeed")
        diaResult = request.POST.get("diaResult")
        Doctor = request.POST.get("Doctor")
        Director = request.POST.get("Director")
        reportTime = request.POST.get("reportTime")

        diareport_info = DiagnosticReports.objects.filter(id=id)

        diareport_info.update(seriousDegree=seriousDegree)
        diareport_info.update(treatNeed=treatNeed)
        diareport_info.update(diaResult=diaResult)
        diareport_info.update(Doctor=Doctor)
        diareport_info.update(Director=Director)
        diareport_info.update(reportTime=reportTime)

        return redirect('/patientslist')


# 到时不为医生提供这一功能，由我们分配账号密码，医生可自行修改密码
def doctorsignup(request):
    state = ""
    if request.method == 'POST':
        username = request.POST.get('docid', '') # 相当于django自带user验证的username
        hosid = request.POST.get('hosid', '')
        hosname = request.POST.get('hosname', '')
        password = request.POST.get('docpwd', '') # 相当于django自带user验证的password
        docname = request.POST.get('docname', '')
        repeat_password = request.POST.get('repeat_docpwd', '')

        if DoctorLogin.objects.filter(username=username):
            state = '用户已存在'
        else:
            new_user = DoctorLogin.objects.create_user(username=username, password=password, hosid=hosid, hosname=hosname, docname=docname)
            new_user.save()

            return redirect('/doctorlogin/')

    return render(request, 'DoctorSignUp.html', {'state': state, 'user': None})


def doctorlogin(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get('docid')
        password = request.POST.get('docpwd')
        user = authenticate(username=username, password=password) # 其他字段对这个没影响
        if user is not None:
            login(request, user)
            return redirect('/showPatients/')
        else:
            message = "用户名或密码错误,请重新输入"
    return render(request, "DoctorLogin.html", {"message": message})


@login_required
def doctorlogout(request):
    logout(request)
    return redirect('/doctorlogin/')


@login_required
def showPatients(request):
    print(request.user.username)
    if request.method == 'GET':
        print("ok")
        all_patients = Patient.objects.all().order_by('id')

    return render(request, 'ManagePatientsInform.html', {'all_patients': all_patients, "user": request.user.username})


@login_required
def showVillages(request):
    print(request.user.username)
    if request.method == 'GET':
        print("ok")
        all_villages = Village.objects.all().order_by('v_id')

    return render(request, 'ManageVillageInform.html', {'all_villages': all_villages, "user": request.user.username})


@login_required
def set_password(request):
    user = request.user
    state = ''
    if request.method == 'POST':
        username = request.POST.get('docid', '')
        old_password = request.POST.get('docpwd', '')
        new_password = request.POST.get('new_docpwd', '')
        repeat_password = request.POST.get('repeat_docpwd', '')
        if user.check_password(old_password):
            if not new_password:
                state = '请输入新密码'
            elif new_password != repeat_password:
                state = '两次输入的密码不一致'
            else:
                newuser = DoctorLogin.objects.get(username=username)
                newuser.set_password(new_password)
                newuser.save()
                return redirect("/doctorlogin/")
        else:
            state = '旧密码错误'
    content = {
        'user': user,
        'state': state,
    }
    return render(request, 'DoctorSetPwd.html', content)
