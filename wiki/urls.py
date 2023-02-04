from django.urls import path
from .import views

urlpatterns = [
    path('get/',views.getWIKI),
    path('post/',views.postWIKI),
    path('put/<int:pk>/',views.putWIKI),
    path('put/<int:pk>/',views.deleteWIKI),
]
