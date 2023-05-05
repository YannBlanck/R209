from django.shortcuts import render

def index(request):
    return render(request, 'myfirstapp/index.html')
def formulaire(request):
    return render(request, 'myfirstapp/formulaire.html')
def bonjour(request):
    nom=request.GET["nom"] # récupère la valeur du paramètre nom du formulaire
    return render(request,'myfirstapp/bonjour.html',{"nom":nom}) # passe cette valeur à
# Create your views here.
