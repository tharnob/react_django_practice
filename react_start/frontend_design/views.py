from django.shortcuts import render

# Create your views here.

def design(request):
    return render(request, 'design/index.html', {})

def react_template(request):
    return render(request, 'frontend_design/react_template.html', {})
