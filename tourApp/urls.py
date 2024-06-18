from django.urls import path, include
from . import views
from  django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

    path('', views.tourFun, name="tourPage"),
    path('-Detail/<str:Destination_id>', views.tourdetailFun, name="tourDetailPage"),


    

    
    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)