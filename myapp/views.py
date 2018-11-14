from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import simplejson as json
from django.core import serializers
# Create your views here.
def index(request):
    student = Students()
    student.name = "faisal"
    student.address = "faisal"
    student.mobile = "faisal"
    student.save()
    return HttpResponse("Hello, world. You're at the polls index.")


#for registering a student
@csrf_exempt 
def registerStudent(request):
    res = {}
    try:
        data = json.loads(request.body)
        name = data['name']
        address = data['address']
        dob = data['dob']
        res['dob'] = dob
        # 
        student = Students()
        student.name = name
        student.address = address
        student.dob = dob
        student.save()
        # 
        res['status'] = "Success"
        res['message'] = "Student details saved"
        res['name'] = name
        return JsonResponse(res)
    except Exception as e:
        res['status'] = "failed"
        res['message'] = "Something went wrong"
        res['error'] = str(e)
        return JsonResponse(res)

@csrf_exempt 
def getAllStudents(request):
    res={}
    try:
        students = serializers.serialize("json",Students.objects.all() )
        # students = list(students)
        res['students'] = json.loads(students)
        res['status'] = "Success"
        return JsonResponse(res)
         
    except Exception as e:
        res['status'] = "failed"
        res['message'] = "Something went wrong"
        res['error'] = str(e)
        return JsonResponse(res)

@csrf_exempt 
def deleteStudent(request):
    res={}
    try:
        data = json.loads(request.body)
        id = data['id']
        student = Students.objects.filter(id=id).delete()
        res['status'] = "success"
        res['message'] = "Student record removed"
        return JsonResponse(res)
    except Exception as e:
        res['status'] = "failed"
        res['message'] = "Something went wrong"
        res['error'] = str(e)
        return JsonResponse(res)



