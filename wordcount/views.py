from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request,'home.html')
def count(request):
	fulltext=request.GET['fulltext']
	
	word_list=fulltext.split()
	
	return render(request,'count.html',{'fulltext':fulltext,'countwords':len(word_list)})