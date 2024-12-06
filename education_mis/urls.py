from django.urls import path, include
from django.contrib import admin
from school import views  # Import for any specific project-level views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Root URL mapped to the 'home' view
    path('school/', include('school.urls')),  # Include app-level URLs
    #path('', lambda request: HttpResponseRedirect('/school/')),  # Redirect root URL to 'school/'
]
