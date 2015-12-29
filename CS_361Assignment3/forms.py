from django import forms

class TeacherForm(forms.Form):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    office_details=forms.CharField(max_length=50)
    phone=forms.CharField(max_length=20)
    email=forms.EmailField()


class StudentForm(forms.Form):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    email=forms.EmailField()


class CourseForm(forms.Form):
    name=forms.CharField(max_length=30)
    code=forms.CharField(max_length=15)
    classroom=forms.CharField(max_length=30)
    times=forms.TimeField()

class EnrollForm(forms.Form):
    student_name=forms.CharField(max_length=30)
    course_name=forms.CharField(max_length=30)

