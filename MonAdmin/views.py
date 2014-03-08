from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from parametrebase.models import *
from parametrebase.GestBazEtablissement import GestBazEtablissement
import datetime

# Create your views here.


# ETABLISSEMENT
#Differene Methode qui gere la table Etablissement

def index(request):
    gerEtabl = GestBazEtablissement()
    Etabl = gerEtabl.returnAll()
    return render(request, 'PagesBackend/Etablissement/ListerEtab.html',{'listEtab': Etabl})

def Ajout(request):
    nom = None
    lieu = None
    try:
        nom = request.GET['Nom']
        lieu = request.GET['Lieu']
    except:
        pass
    if nom!=None and lieu!=None:
        gerEtabl =  GestBazEtablissement()
        Etabl = Etablissement(Nom=nom,Lieu=lieu)
        if(not gerEtabl.save(Etabl)):
            msg =" Ajout reussi!"
        else:
            msg ="Echec de l'ajout"
        return render(request, 'PagesBackend/Etablissement/Sauvegarder.html', {'gerEtabl':Etabl})
    dtnow = datetime.datetime.now()
    Nouvo = get_template('PagesBackend/Etablissement/AjouterEtab.html')
    nv = Nouvo.render(Context({'current_date':dtnow}))
    return HttpResponse(nv)

#def Sauvegarde(request):
#    nom =request.GET['Nom']
#    lieu = request.GET['Lieu']
#    gerEtabl =  GestBazEtablissement()
#    Etabl = Etablissement(Nom=nom,Lieu=lieu)
#    if(not gerEtabl.save(Etabl)):
#        msg =" Ajout reussi!"
#    else:
#        msg ="Echec de l'ajout"
#    return render(request, 'PagesBackend/Etablissement/Sauvegarder.html', {'gerEtabl':Etabl})

def modification(request,id):
    gerEtabl= GestBazEtablissement()
    Etabl = gerEtabl.returnOne(id)

    return render (request, 'PagesBackend/Etablissement/ModifierEtab.html',{'formModif':Etabl})

def SauvModif(request, id):
    nom=request.GET['Nom']
    lieu=request.GET['Lieu']
    gerEtabl =  GestBazEtablissement()
    Etabl = Etablissement(Nom=nom, Lieu=lieu)

    if(gerEtabl.modify(id=id, Nom=nom, Lieu=lieu)):
        msg = "Les informations concernnant l'etablissement n'ont pas ete modifie."
    else:
        msg = "Etabissement modifier avec succes."
    return render(request, 'PagesBackend/ Etablissement/Sauvegarder.html',{'msg':msg})

def Suppression(request, id):
    gerEtabl =  GestBazEtablissement()
    Etabl = gerEtabl.returnOne(id)
    return render(request, 'PagesBackend/Etablissement/supprimerEtab.html', {'SuppEtab': Etabl})

def SauvSupp(request, id):
    gerEtabl =  GestBazEtablissement()
    if(not gerEtabl.delete(id=id)):
        msg = "Etablissement efface"
    else:
        msg = "L'etablisssemnt n'a pas ete efface"
    return render(request, 'PagesBackend/Etablissement/Sauvegarder.html',{'msg': msg})