from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pict/', include('pict.urls')),
    path('pict/first_year/', include('first_year.urls')),
    path('pict/second_year/', include('second_year.urls')),
    path('pict/third_year/', include('third_year.urls')),
    path('pict/final_year/', include('final_year.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),

]
