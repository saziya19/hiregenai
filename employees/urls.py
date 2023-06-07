from django.urls import path
from django.urls import re_path
#from .views import download_file
from .import views

urlpatterns = [
    path('',views.main,name='main'),
    path('jobseeker',views.jobseeker,name='jobsee'),
    path('resume',views.resume,name='resum'),
    path('filtered_files',views.filtered_files,name='filtered_files'),
    # path('download_file/<str:filename>/', views.download_file, name='download_file'),
    # path('download_file/<str:filename>/', views.download_file, name='download_file'),
     path('download_file/<str:filename>/',views.download_file, name='download_file'),
    #  path('search1',views.search1,name='search'),
     path('search_resumes/', views.search_resumes, name='search_resumes'),
    # path('download_file/<str:filename>/', download_file, name='download_file'),
]
    # re_path(r'^download_file/(?P<path>.+)/$', download_file, name='download_file'),

    # path('job_search/', views.job_search, name='job_search'),
   

    
    
