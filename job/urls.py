from django.urls import path
from . import views

from . import api

app_name = 'job'



urlpatterns = [
     
     path('' , views.job_list , name='job_list'),
     path('add/' , views.add_job , name='add_job'),
     path('<slug:slug>/' , views.job_details , name='job_details'),


     # api 
     path('api/jobs', api.joblistapi , name='joblistapi'),
     path('api/jobs/<int:id>/', api.job_details_api , name='job_details_api'),

     # class 

     path('api/v2/jobs', api.JobListView.as_view() , name='job_details_api'),
     path('api/v2/jobs/<int:id>/', api.JobDetailsApi.as_view() , name='job_details_api'),
]