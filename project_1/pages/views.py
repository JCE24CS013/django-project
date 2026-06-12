from django.shortcuts import render

def home(request):
    context = {
        'name': 'Amrith',
        'company': 'ARTCL'
    }
    return render(request, 'pages/home.html', context)

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    context = {
        'email': 'contact@artcl.com',
        'phone': '+91 9999999999'
    }
    return render(request, 'pages/contact.html', context)
