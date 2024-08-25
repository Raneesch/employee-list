from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from employees.models import Emploee




# Create your views here.


def employee_details(requests,pk):
#    try:
#        employee = Emploee.objects.get(pk = pk)
#        print(employee)
#    except:
#        raise Http404
    employee=get_object_or_404(Emploee, pk = pk)
    # print(employee)
    context = {
        'employee' : employee
    }
    return render(requests,'employee_detail.html',context)
    