from django.shortcuts import render, redirect
from .models import Image, Usuario
from .forms import RegistroForm

def index(request):
    images = Image.objects.all() # Busca todas as imagens no banco de dados
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('archcode/index2.html')
    else:
        form = RegistroForm()
    context={
        "page_title":"Portal BSI",
        "images": images, # Passa as imagens para o template
        "form": form
    }
    return render(request,'archcode/index.html',context)

""" def index(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('archcode/index2.html')  # Altere conforme necessário
    else:
        form = RegistroForm()

    images = Image.objects.all()  # Busca todas as imagens no banco de dados
    context = {
        "page_title": "Portal BSI",
        "images": images,  # Passa as imagens para o template
        "form": form  # Adiciona o formulário ao contexto
    }
    return render(request, 'archcode/index.html', context) """
    
  

def index_2(request):
    context={
        "page_title":"Home 2"
    }
    return render(request,'archcode/index-2.html',context)

def index_3(request):
    context={
        "page_title":"Home 3"
    }
    return render(request,'archcode/index-3.html',context)

def about_us(request):
    context={
        "page_title":"About Us"
    }
    return render(request,'archcode/about-us.html',context)

def team(request):
    context={
        "page_title":"Team"
    }
    return render(request,'archcode/team.html',context)

def portfolio(request):
    context={
        "page_title":"Portfolio"
    }
    return render(request,'archcode/portfolio.html',context)

def portfolio_details(request):
    context={
        "page_title":"Portfolio Details"
    }
    return render(request,'archcode/portfolio-details.html',context)

def services_details(request):
    context={
        "page_title":"Services Details"
    }
    return render(request,'archcode/services-details.html',context)

def services(request):
    context={
        "page_title":"Services"
    }
    return render(request,'archcode/services.html',context)

def blog_grid(request):
    context={
        "page_title":"Blog Grid"
    }
    return render(request,'archcode/blog-grid.html',context)

def blog_large_left_sidebar(request):
    context={
        "page_title":"Large Left Sidebar"
    }
    return render(request,'archcode/blog-large-left-sidebar.html',context) 

def blog_list_left_sidebar(request):
    context={
        "page_title":"List Left Sidebar"
    }
    return render(request,'archcode/blog-list-left-sidebar.html',context)

def blog_details(request):
    context={
        "page_title":"Blog Details"
    }
    return render(request,'archcode/blog-details.html',context)

def contact_us(request):
    context={
        "page_title":"Contact Us"
    }
    return render(request,'archcode/contact-us.html',context)

def coming_soon(request):
    context={
        "page_title":"Coming Soon"
    }
    return render(request,'archcode/coming-soon.html',context)

def under_construct(request):
    context={
        "page_title":"Under Construct"
    }
    return render(request,'archcode/under-construct.html',context)

def error_404(request):
    context={
        "page_title":"Error 404"
    }
    return render(request,'404.html',context)





    

