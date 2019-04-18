from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required



# Views

def steg_base(request):
    return render(request,'audio_steg/base.html')

def steg_welcome(request):
    return render(request, 'audio_steg/welcome.html')

@login_required
def steg_audio_input(request):
    return render(request, 'audio_steg/audio_input.html')

@login_required
def steg_text_input(request):
    return render(request, 'audio_steg/text_input.html')

@login_required
def steg_image_input(request):
    return render(request, 'audio_steg/image_input.html')

@login_required
def history(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'audio_steg/history.html', context)
