from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('ais/<int:ai_id>/', views.ai_detail, name='ai_detail'),
    path('ais/', views.ais, name="ais"),
    path('sources/<int:source_id>/', views.source_detail, name='source_detail'),
    path('sources/', views.sources, name="sources"),
    path('persons/<int:id>/', views.person_detail, name='person_detail'),
    path('persons/', views.persons, name="persons"),
    path('project/links/', views.links, name="links"),
    path('contact/', views.contact, name="contact"),
    path('project/thesis/', views.thesis, name="thesis"),
    path('project/', views.project, name="project"),
    path('project/presentations/', views.presentations, name="presentations"),
    path('imprint/', views.imprint, name="imprint"),
    path('privacy/', views.privacy, name="privacy"),
    # path('series/<int:series_id>/', views.series_detail, name='series_detail'),
    # path('series/', views.series, name="series"),
]