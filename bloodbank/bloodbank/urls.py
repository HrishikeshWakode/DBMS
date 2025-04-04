from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def homepage_redirect(request):
    return redirect('add_hospital')
urlpatterns = [
    path('', homepage_redirect),  
    path('admin/', admin.site.urls),
    path('bloodlife/', include('bloodlife.urls')),
]
