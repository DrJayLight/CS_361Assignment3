from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from forms import *
from models import *
from django.shortcuts import RequestContext

def add_teacher(request):
    if request.method=='POST':
        form=TeacherForm(request.POST)
        if form.is_valid():
            t=Teacher(first_name=form.cleaned_data['first_name'],
                      last_name=form.cleaned_data['last_name'],
                      office_details=form.cleaned_data['office_details'],
                      phone=form.cleaned_data['phone'],
                      email=form.cleaned_data['email'])
            t.save()
            return HttpResponseRedirect('/all-teachers/')
    else:
        form=TeacherForm()
    return render_to_response('add_teacher.html',{'form':form},RequestContext(request))

def add_student(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            s=Student(first_name=form.cleaned_data['first_name'],
                      last_name=form.cleaned_data['last_name'],
                      email=form.cleaned_data['email'])
            s.save()
            return HttpResponseRedirect('/all-students/')
    else:
        form=StudentForm()
    return render_to_response('add_student.html',{'form':form},RequestContext(request))


def add_course(request):
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            t=Teacher(first_name="Non",last_name="Non",office_details="Non",phone="Non",
                    email="Non@Non.com")
            t.save()
            c=Course(name=form.cleaned_data['name'],
                      code=form.cleaned_data['code'],
                      classroom=form.cleaned_data['classroom'],
                      times=form.cleaned_data['times'],
                      teacher=t)
            c.save()
            return HttpResponseRedirect('/all-courses/')
    else:
        form=CourseForm()
    return render_to_response('add_course.html',{'form':form},RequestContext(request))

def all_teachers(request):
    return render_to_response('all_teachers.html',
                              {'teacher_list':Teacher.objects.all()})

def all_students(request):
    return render_to_response('all_students.html',
                              {'student_list':Student.objects.all()})

def all_courses(request):
    return render_to_response('all_courses.html',
                              {'course_list':Course.objects.all()})

def enroll_student(request):
    if request.method=='POST':
        form=EnrollForm(request.POST)
        if form.is_valid():
            s_name=form.cleaned_data['student_name']
            student=Student.objects.filter(first_name=s_name)
            coursename=form.cleaned_data['course_name']
            Course.objects.filter(name=coursename)

            return HttpResponseRedirect('/all-enrolledstudents/')
    else:
        form=EnrollForm()
    return render_to_response('enroll_students.html',{'form':form},RequestContext(request))

