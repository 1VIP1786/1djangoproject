from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):

   #Get the text

   djtext = request.GET.get('text', 'default')
   
def analyze(request):

    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")
   # #  #Analyze the text
   #  return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")


# def spaceremove(request):
#     return HttpResponse("space remover back")

# def charcount(request):
#     return HttpResponse("charcount ")
