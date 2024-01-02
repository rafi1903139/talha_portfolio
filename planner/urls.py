from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('experience/', views.experience, name='experience'),
    path('education/', views.education, name='education'),
    path('extra_curricular/', views.extra_curricular, name='extra_curricular'),
    path('org_affiliation/', views.org_affiliation, name='org_affiliation'),
    path('participation/', views.participation, name='participation'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('reference/', views.reference, name='reference'),
    path('skills/', views.skills, name='skills'),
    path('training/', views.training, name='training'),

    
]



