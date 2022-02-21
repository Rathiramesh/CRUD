from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields=('fullname','Mob_number','position','Emp_code')
        labels={'fullname':'FullName','Emp_code':'Employee_Code','Mob_number':'Mobile_Number','position':'Position', }
