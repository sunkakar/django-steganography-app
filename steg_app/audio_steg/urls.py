from django.urls import path
from . import views
from .views import HistoryListView, StegTextView
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('',views.steg_base, name='steg-base'),
	path('about/',views.about, name='about'),
	path('welcome/',views.steg_welcome, name='welcome-page'),
	path('audio/',views.steg_audio_input, name='audio-input'),
	path('text/',login_required(StegTextView.as_view()), name='text-input'),
	path('image/',views.steg_image_input, name='image-input'),
	path('history/',login_required(HistoryListView.as_view()), name='steg-history'),
	path('encrypted/',views.encryptresult, name='steg-encrypted'),	
]