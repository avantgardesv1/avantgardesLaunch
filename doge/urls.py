from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("join", views.join, name="join"),
    path("variations", views.variations, name='variations'),
    path("memes", views.memes, name="memes"),
    path("cycle", views.cycle, name="cycle"),
    path("atm", views.atm, name="atm"),
    path('submissions', views.submissions, name="submissions"),
    path('atm_memes', views.atm_memes, name="atm_memes"),
    path('faqs', views.faqs, name="faqs"),
    path("community", views.community, name="community"),



    # This is the API route
    path("metadata/<int:metadata_id>", views.metadata, name="metadata"),
    
]
