from django.shortcuts import *
from django.http import HttpResponse
from nav import *
# Create your views here.
def abcd(request):
	return render_to_response("nav/abc.html")
def index(request):
	return render_to_response("nav/index.html")
def analyze(request):
	djtext=request.GET.get('text','default')
	removpunc=request.GET.get('removepunc','off')
	caps=request.GET.get('capslock','off')
	nlinerem=request.GET.get('newline','off')
	extrspc=request.GET.get('extraspace','off')
	chcnt=request.GET.get('charcount','off')
	analyzed=""
	purpose=""
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	if removpunc=='on':
		analyzed=""
		for char in djtext:
			if char not in punctuations:
				analyzed=analyzed+char
		purpose= purpose+"Removed Punctuations"
		#params={'purpose':'','analyzed_text':analyzed}
		djtext=analyzed
		#return render(request,"nav/analyze.html",params)
	if caps=='on':
		analyzed=""
		for char in djtext:
			analyzed=analyzed+char.upper()
		#params={'purpose':'IN UPPERCASE','analyzed_text':analyzed}
		purpose=purpose+" | IN UPPER CASE"
		djtext=analyzed
		#return render(request,"nav/analyze.html",params)
	if nlinerem=='on':
		analyzed=""
		for char in djtext:
			if char!="\n":
				analyzed=analyzed+char
		purpose=purpose+" | NEW LINE REMOVED"
		#params={'purpose':'New Line Removed','analyzed_text':analyzed}
		djtext=analyzed
		#return render(request,"nav/analyze.html",params)
	if extrspc=='on':
		analyzed=""
		for index,char in enumerate(djtext):
			if index+1<len(djtext):
				if djtext[index]==' ' and djtext[index+1]==' ':
					pass
				else:
					analyzed=analyzed+char
		#params={'purpose':'Extra Space Removed','analyzed_text':analyzed}
		purpose=purpose+" | EXTRA SPACE REMOVED"
		djtext=analyzed
		#return render(request,"nav/analyze.html",params)
	if removpunc=='on' or caps=='on' or nlinerem=='on' or extrspc=='on':
		if chcnt=='on':
			analyzed=analyzed+" and character count is "+str(len(djtext))
		params={'purpose2':purpose,'analyzed_text':analyzed}
		return render(request,"nav/analyze.html",params)
	else:
		return HttpResponse("Error")
def about(request):
	return render(request,'nav/abt.html')
def contact(request):
	return render(request,'nav/con.html')
	