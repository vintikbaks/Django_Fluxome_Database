from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'queries'
urlpatterns = [
	path('', views.index, name="index"),
	path('<int:flux_id>/', views.detail, name="detail"),
	path('<int:flux_id>/', views.detail2, name="detail2"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)