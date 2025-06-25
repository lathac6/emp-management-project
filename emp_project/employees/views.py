from django.shortcuts import render,redirect,get_object_or_404
from .models import *
# Create your views here.
def dashborad_viwes(request):
    return render(request,'dashboard.html')

def employee_list_views(request):
    employees=Employee.objects.all()
    context={
        'employees':employees
    }
    return render(request,'employee_list.html',context)

def department_list_views(request):
    departments=Department.objects.all()
    context={
        'departments':departments
    }
    return render(request,'department_list.html',context)

def create_department_view(request):
    if request.method == 'POST':
        name=request.POST.get('dname')
        loc=request.POST.get('dloc')
        Department.objects.create(
            dname=name,
            d_location=loc
        )
        return redirect('department_list')
    return render(request,'create_department.html')

def create_employee_view(request):
    context = {}
    departments = Department.objects.all()
    context['departments'] = departments

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        email=request.POST.get('email')
        address=request.POST.get('address')
        dept_id = request.POST.get('department')

        if not dept_id:
            context['error'] = "Please choose a department"
            return render(request, 'create_employee.html', context)

        try:
            department = Department.objects.get(id=dept_id)
            # Proceed to create Employee (assuming model exists)
            Employee.objects.create(
                ename=name,
                age=age,
                salary=salary,
                email=email,
                address=address,
                dept=department
            )
            return redirect('employee_list')  # Update with your actual URL name
        except Department.DoesNotExist:
            context['error'] = "Selected department does not exist"

    return render(request, 'create_employee.html', context)
def create_employee_profile_view(request,pk):
    employee=get_object_or_404(Employee,id=pk)
    if request.method == 'POST':
        bio=request.POST.get('bio')
        linkedin=request.POST.get('linkedin')
        phone_no=request.POST.get('phone_no')
        image=request.FILES.get('profile_picture')
        resume=request.FILES.get('resume')
        EmployeeProfile.objects.create(employee=employee,
                                       bio=bio,
                                       image=image,
                                       resume=resume,
                                       linkedin=linkedin,
                                       phone_no=phone_no)
        return redirect('employee_list')
    context={
        'employee':employee

    }
    return render(request,'create_employee_profile.html',context )
