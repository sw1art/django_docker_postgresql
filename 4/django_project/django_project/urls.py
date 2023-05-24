from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),
    # user manager
    path('accounts/', include('django.contrib.auth.urls')),
    # local applications
    path('', include('pages.urls'))
]
