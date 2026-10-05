from django.shortcuts import render,redirect
from.models import Student

def display_student_view(request):
    students=Student.objects.all()
    
    context={
        'students' : students
    }
    return render(request,'display_student.html',context)
def create_student_view(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        rollno=request.POST.get('rollno')
        marks=request.POST.get('marks')
        course=request.POST.get('course') 
        address=request.POST.get('address')
        
        Student.objects.create(name=name,rollno=rollno,marks=marks,course=course,address=address)
        return redirect('display') 
    return render(request,'student-form.html')   

def update_student_view(request,student_id):
    context={
        'operation':'update student',
        'title':'update student',
    }
          
    try:
        student=Student.objects.get(id=student_id)
        context['student']=student
      
    
    except Student.DoesNotExist:
        context['errors']='404 :student not found '
        
    if request.method == 'POST':
        name=request.POST.get('name')
        rollno=request.POST.get('rollno')
        marks=request.POST.get('marks')
        address=request.POST.get('address')
        course=request.POST.get('course') 
        
        student.name=name
        student.rollno=rollno
        student.marks=marks
        student.address=address
        student.course=course
        
        student.save()
        return redirect('display')
    
    return render(request,'student-form.html',context)

def delete_student_view(request,student_id):
    context=dict()
    
    try:
        student=Student.objects.get(id=student_id)
        context['student']=student
    except Student.DoesNotExist:
        context['errors']='404: student not found'
    if request.method=='POST':
        student.delete()
        return redirect('display')
    return render(request,'delete-student.html',context)        
          