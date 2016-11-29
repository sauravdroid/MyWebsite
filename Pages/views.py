from django.shortcuts import render


def home_page(request):
    return render(request, 'Pages/homepage.html', {})


def about_me_page(request):
    return render(request,'Pages/about-me.html',{})

def projects_page(request):
    return render(request,'Pages/project-list.html',{})