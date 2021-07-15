from django.urls import path

from report import views

app_name = 'report'

urlpatterns = [
    path('report_list/',views.ReportListView.as_view(),name="report_list"),
    path('<int:pk>/report_detail',views.ReportDetailView.as_view(),name="report_detail"),
    path('<int:pk>/report_update',views.ReportDetailView.as_view(),name="report_update"),
]