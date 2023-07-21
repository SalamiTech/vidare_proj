from django.shortcuts import render
from django.http import HttpResponse
from myapp.functions import handle_uploaded_file
from myapp.forms import StudentForm
from myapp.models import Student   # Update the import statement

def index(request):  
    if request.method == 'POST':  
        form = StudentForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()
            return HttpResponse("File uploaded successfully")  
    else:  
        form = StudentForm() 
    return render(request, "index.html", {'form': form})

def dashboard(request):
    students = Student.objects.all() 
    return render(request, "dashboard.html", {'students': students})
