from django.urls import path

from report import views

app_name = 'report'

urlpatterns = [
    path('report_list/',views.ReportListView.as_view(),name="report_list"),
    path('report_draft/',views.ReportDraftListView.as_view(),name="report_draft"),
    path('<int:pk>/report_draft_update/',views.ReportDraftUpdateView.as_view(),name='report_draft_update'),
    path('<int:pk>/report_detail/',views.ReportDetailView.as_view(),name="report_detail"),
    path('<int:pk>/report_update/',views.ReportUpdateView.as_view(),name="report_update"),
    path('<int:pk>/report_delete',views.ReportDeleteView.as_view(),name="report_delete"),
    path('report_form/',views.ReportCreateView.as_view(),name="report_form")

]