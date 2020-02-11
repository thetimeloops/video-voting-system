from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.login1,name="login1"),
    path('index',views.index,name="index"),
    path('indexx/<str:id_name>',views.indexx,name="indexx")
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
