from django.contrib import admin
from django.urls import path, include
from projects import views
from landing import views as landing_views

urlpatterns = [
    path('', include('landing.urls')),
    path('about/', landing_views.about),
    path('project/activate/<slug:handle>/', views.activate_project_view),
    path('project/deactivate/<slug:handle>/', views.activate_project_view),
    path('admin/', admin.site.urls),
]
