from django.urls import path

from worker_admin import views

app_name = 'worker'

urlpatterns =[
    path('worker_list/',views.WorkerAdminListView.as_view(),name="worker_list"),
    path('worker_detail/',views.WorkerDetailView.as_view(),name="worker_detail"),
    path('<int:pk>/worker_update/',views.WorkerUpdateView.as_view(),name="worker_update"),
    path('<int:pk>/worker_detail/',views.WorkerDetailView.as_view(),name="worker_detail"),
    path('<int:pk>/worker_delete/',views.WorkerDeleteView.as_view(),name="worker_delete"),
]