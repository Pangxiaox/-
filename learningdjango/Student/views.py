from Student.models import StudentInfo
from django.shortcuts import render, redirect


def show(request):
    studentlist = StudentInfo.objects.all()
    return render(request, "studentinfo.html", {"s_list": studentlist})


def post(request):
    stu = StudentInfo()
    if request.POST:
        stu.name = request.POST.get('inputname')
        stu.sex = request.POST.get('inputsex')
        stu.credit = request.POST.get('inputcredit')
        stu.save()
        return redirect("/studentinfo/")
    return render(request, "post.html")


def detailinfo(request):
    stuname = request.GET.get('inputname')
    return render(request, "detailInfo.html", {"s_name": stuname})


