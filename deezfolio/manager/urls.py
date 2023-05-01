from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.manager,name="manager"),
    path("panel",views.panel,name="panel"),
    path("Logout",views.Logout,name="Logout"),
    path("portfolio",views.portfolio,name="portfolio"),
    # for CRUD Operations
    path("addport",views.addport,name="addport"),
    path("editport/<str:pk>",views.editport,name="editport"),
    path("deleteport/<str:pk>",views.deleteport,name="deleteport"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)