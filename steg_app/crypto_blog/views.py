from django.shortcuts import render
from django.http import HttpResponse

# Views 

posts = [
	{
		'author':'Sunny D',
		'title':'Crypto Blog',
		'content':'content posted',
		'date_posted':'August 10, 1998'
	},
	{
		'author':'Sae-D',
		'title':'Anatomy Blog',
		'content':'Diabetic Foot thing',
		'date_posted':'August 10, 2018'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request,'crypto_blog/home.html', context)

def about(request):
	return render(request,'crypto_blog/about.html', {'title': 'About'})





