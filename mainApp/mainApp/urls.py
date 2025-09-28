from django.contrib import admin
from django.urls import include, path
# multilingual support



urlpatterns = (
    
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('references/', include('references.urls')),
    path('jsonEditor/', include('jsonEditor.urls')),
    path('products/', include('products.urls')),
    path('businessAnalytics/', include('businessAnalytics.urls')),
    path('eTransformation/', include('eTransformation.urls')),
    path('hrAndPayroll/', include('hrAndPayroll.urls')),
    path('warehouseWMS/', include('warehouseWMS.urls')),
    path('workflow/', include('workflow.urls')),
    path('consulting/', include('consulting.urls')),
    path('projectManagement/', include('projectManagement.urls')),
    path('serverAndData/', include('serverAndData.urls')),
    path('supportServices/', include('supportServices.urls')),
    path('swDevelopment/', include('swDevelopment.urls')),
    path('warehouseWMS/', include('warehouseWMS.urls')),
    path('workflow/', include('workflow.urls')),
    
)
