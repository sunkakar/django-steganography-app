from django.shortcuts import render, redirect
from .models import Post
from .forms import TextForm, ImageForm, AudioForm
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from .text_encrypt import text_encrypt, text_decrypt
from .audio_encrypt import audio_encrypt, music, audio_decrypt


# Views

def steg_base(request):
    return render(request,'audio_steg/base.html')

def steg_welcome(request):
    return render(request, 'audio_steg/welcome.html')



class StegAudioView(TemplateView):
    template_name = 'audio_steg/audio_input.html'

    def get(self,request):
        form = AudioForm()
        return render(request, self.template_name,{'form':form})

    def post(self,request):
        form = AudioForm(request.POST)
        
        if form.is_valid():
            #form.save()
            Type = form.cleaned_data.get('stegtype')
            HiddenText = form.cleaned_data.get('hiddentext')
            choice_field = form.cleaned_data.get('choice_field')
            
            result = 'Invalid Form Input. Try Again!'
            if choice_field == '1':    
                result1 = audio_encrypt(HiddenText)
                result2 = music(HiddenText)
                result = {'octalval':result1, 'notes':result2}

            elif choice_field == '2':
                result1 = audio_decrypt(HiddenText)
                result = {'notes':result1}
                print(result1)
        args = {'form': form, 'result':result, 'choice':choice_field}
        return render(request, self.template_name, args)



class StegTextView(TemplateView):
    template_name = 'audio_steg/text_input.html'

    def get(self,request):
        form = TextForm()
        return render(request, self.template_name,{'form':form})

    def post(self,request):
        form = TextForm(request.POST)
        
        if form.is_valid():
            #form.save()
            Type = form.cleaned_data.get('stegtype')
            PlainText = form.cleaned_data.get('plaintext')
            HiddenText = form.cleaned_data.get('hiddentext')
            choice_field = form.cleaned_data.get('choice_field')
            result = 'Invalid Form Input. Try Again!'
            if choice_field == '1':    
                result = text_encrypt(PlainText,HiddenText)

            elif choice_field == '2':
                result = text_decrypt(PlainText)

        args = {'form': form, 'result':result}
        return render(request, self.template_name, args)


class StegImageView(TemplateView):
    template_name = 'audio_steg/image_input.html'

    def get(self,request):
        form = ImageForm()
        return render(request, self.template_name,{'form':form})

    def post(self,request):
        form = ImageForm(request.POST)
        
        if form.is_valid():
            #form.save()
            Type = form.cleaned_data.get('stegtype')
            PlainText = form.cleaned_data.get('plaintext')
            HiddenText = form.cleaned_data.get('hiddentext')
            result = text_encrypt(PlainText,HiddenText)
        args = {'form': form, 'result':result}
        return render(request, self.template_name, args)



@login_required
def history(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'audio_steg/history.html', context)

def about(request):
    return render(request, 'audio_steg/about.html', {'title': 'About'})


def encryptresult(request):
    return render(request, 'audio_steg/encryptresult.html')



class HistoryListView(ListView):
    model = Post
    template_name = 'audio_steg/history.html'
    context_object_name = 'posts'
    ordering = ['-date']
