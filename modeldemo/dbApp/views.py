from django.shortcuts import render
from dbApp.models import employee
# Create your views here.
def empDetails(request):

    emp_data=employee.objects.all()
    emp_dict={'emp_list':emp_data}
    for em in emp_data:
        print(em.empNo)
    return render(request,'dbApp/employee.html',context=emp_dict)