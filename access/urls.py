from django.urls import path
from access import views

app_name = 'access'

urlpatterns = [
    path('access_list/',views.AccessListView.as_view(),name="access_list"),
    path('<int:pk>/access_detail/',views.AccessDetailView.as_view(),name="access_detail"),
    path('<int:pk>/access_update/',views.AccessUpdateView.as_view(),name="access_update"),
    path('<int:pk>/access_delete',views.AccessDeleteView.as_view(),name="access_delete")
]