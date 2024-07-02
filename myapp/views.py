from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # aboutMe = {"name": "Olim", "surname": "Yuldoshev"}
    # return render(request, "index.html", aboutMe)
    return render(request, "index.html")


# def counter(request):
#     text = request.GET["text"]
#     lengthOfText = len(text.split())

#     # dictionaryText = {"text": text}
#     dictionaryLengthOfText = {"lengthOfText": lengthOfText}


#     # return render(request, "counter.html", dictionaryText)
#     return render(request, "counter.html", dictionaryLengthOfText)
def counter(request):
    text = request.POST["text"]
    lengthOfText = len(text.split())

    # dictionaryText = {"text": text}
    dictionaryLengthOfText = {"lengthOfText": lengthOfText}

    # return render(request, "counter.html", dictionaryText)
    return render(request, "counter.html", dictionaryLengthOfText)
