from django.urls import path

from . import views

urlpatterns = [
	path('',views.steg_base, name='steg-base'),
	path('welcome/',views.steg_welcome, name='welcome-page'),
	path('audio/',views.steg_audio_input, name='audio-input'),
	path('text/',views.steg_text_input, name='text-input'),
	path('image/',views.steg_image_input, name='image-input')
]