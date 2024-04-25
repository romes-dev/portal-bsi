from django.urls import path ,include
from archcode import archcode_views
from django.conf.urls.static import static
from django.conf import settings


app_name='archcode'
urlpatterns = [
    
    path('',archcode_views.index,name="index"),
    path('index/',archcode_views.index,name="index"),
    path('index-2/',archcode_views.index_2,name="index-2"),
    path('index-3/',archcode_views.index_3,name="index-3"),

    path('about-us/',archcode_views.about_us,name="about-us"),
    path('team/',archcode_views.team,name="team"),

    path('portfolio/',archcode_views.portfolio,name="portfolio"),
    path('portfolio-details/',archcode_views.portfolio_details,name="portfolio-details"),

    path('services/',archcode_views.services,name="services"),
    path('services-details/',archcode_views.services_details,name="services-details"),

    path('blog-grid/',archcode_views.blog_grid,name="blog-grid"),
    path('blog-large-left-sidebar/',archcode_views.blog_large_left_sidebar,name="blog-large-left-sidebar"),
    path('blog-list-left-sidebar/',archcode_views.blog_list_left_sidebar,name="blog-list-left-sidebar"),
    path('blog-details/',archcode_views.blog_details,name="blog-details"),
    
    path('contact-us/',archcode_views.contact_us,name="contact-us"),
    path('coming-soon/',archcode_views.coming_soon,name="coming-soon"),
    path('under-construct/',archcode_views.under_construct,name="under-construct"),
    path('error-404/',archcode_views.error_404,name="error-404"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)