from django.shortcuts import render

# Create your views here.

def renderTemplate(request):
    myDict = {"name":"Eugene"}
    return render(request, 'templatesApp/firstTemplate.html', context=myDict)

def renderEmployee(request):
    myDict={"id": 12345, "name": "Eugene", "sal": 140000}
    return render(request,'templatesApp/employeeTemplate.html', myDict)
