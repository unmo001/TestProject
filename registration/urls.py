from django.urls import path

from registration import views

app_name = 'registration'

urlpatterns=[
    path('',views.Login.as_view(),name='login'),
    path('logout/',views.Logout.as_view(),name="logout")
]