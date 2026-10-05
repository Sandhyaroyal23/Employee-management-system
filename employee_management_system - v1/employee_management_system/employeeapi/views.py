from django.http import HttpResponse
from .models import Employee
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def employee_list_view(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        
        employee_list = []
    
        for employee in employees:
            emp_dict = {
                'name' : employee.name,
                'salary' : employee.salary,
                'email' : employee.email,
                'address' : employee.address,
                'role' : employee.role
            }
            employee_list.append(emp_dict)
    
    
        response_data = json.dumps(employee_list)
    
        return HttpResponse(
            response_data, 
            content_type='application/json',
            status=200
        )


    if request.method == 'POST':
        request_data = request.body
        python_data = json.loads(request_data)

        employee = Employee.objects.create(**python_data)

        data = {
            'message' : 'Employee created successfully',
            'data' : {
                'id' : employee.id,
                'name' : employee.name,
                'salary' : employee.salary,
                'email' : employee.email,
                'address' : employee.address,
                'role' : employee.role
            }
        }

        response_data = json.dumps(data)

        return HttpResponse(
            response_data,
            content_type = 'application/json',
            status = 201
        )

#Outside the if block but inside the function
    error_data = {
        'message' : "Only 'GET' and 'POST' methods are allowed"
    }

    response_data = json.dumps(error_data)

    return HttpResponse(
        response_data,
        content_type = 'application/json',
        status = 405
    )

    
@csrf_exempt
def employee_details_view(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        error_data = {
            'message' : 'Employee ID does not exist'
        }
        response_data = json.dumps(error_data)
        return HttpResponse(
            response_data,
            content_type = 'application/json',
            status=404
        )


    if request.method == 'GET':
        emp_dict = {
            'id' : employee.id,
            'name' : employee.name,
            'salary' : employee.salary,
            'email' : employee.email,
            'address' : employee.address,
            'role' : employee.role
        }

        data = {
            'message' : 'Employee found successfully',
            'data' : emp_dict
        }

        response_data = json.dumps(data)

        return HttpResponse(
            response_data,
            content_type = 'application/json',
            status=200
        )

    if request.method == "PUT":
        request_data = json.loads(request.body)

        field_list = ['name', 'salary', 'email', 'address', 'role']
        missing_fields = []

        for field in field_list:
            if field not in request_data:
                missing_fields.append(field)

        if missing_fields:
            data = {
                'message' : 'Mandatory fields are missing',
                'missing_fields' : missing_fields
            }

            response_data = json.dumps(data)

            return HttpResponse(
                response_data,
                content_type = 'application/json',
                status = 400
            )


        employee.name = request_data['name']
        employee.salary = request_data['salary']
        employee.email = request_data['email']
        employee.address = request_data['address']
        employee.role = request_data['role']
        employee.save()

        data = {
                'message' : 'Employee replaced successfully',
                'data' : {
                    'id' : employee.id,
                    'name' : employee.name,
                    'salary' : employee.salary,
                    'email' : employee.email,
                    'address' : employee.address,
                    'role' : employee.role
                }
            }
    
        response_data = json.dumps(data)
    
        return HttpResponse(
            response_data,
            content_type = 'application/json',
            status = 200
        )

    if request.method == 'PATCH':
        request_data = json.loads(request.body)

        employee.name = request_data.get('name', employee.name)
        employee.salary = request_data.get('salary', employee.salary)
        employee.email = request_data.get('email', employee.email)
        employee.address = request_data.get('address', employee.address)
        employee.role = request_data.get('role', employee.role)

        employee.save()

        data = {
            'message' : 'Employee modified successfully',
            'data' : {
                'id' : employee.id,
                'name' : employee.name,
                'salary' : employee.salary,
                'email' : employee.email,
                'address' : employee.address,
                'role' : employee.role
            }
        }

        response_data = json.dumps(data)

        return HttpResponse(
            response_data,
            content_type = 'application/json',
            status = 200
        )

    if request.method == 'DELETE':
        employee.delete()

        data = {
            'message' : 'Employee deleted successfully',
            'data' : {
                'name' : employee.name,
                'salary' : employee.salary,
                'email' : employee.email,
                'address' : employee.address,
                'role' : employee.role
            }
        }

        response_data = json.dumps(data)

        return HttpResponse(
            response_data,
            content_type = 'application/json',
            status = 200
        )

#Outside the if blocks inside the function
    error_message = {
        'message' : "Only 'GET', 'PUT', 'PATCH' & 'DELETE' methods are allowed"
    }

    response_data = json.dumps(error_message)

    return HttpResponse(response_data, content_type='application/json', status=405)