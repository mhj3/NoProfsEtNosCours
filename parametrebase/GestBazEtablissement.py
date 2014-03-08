from models import Etablissement

class GestBazEtablissement:

    def save(self,etabl):
        etabl.save()

    def modify(self,id,nom,lieu):
        Etablissement.objects.filter(id=id).upadte(nom=nom, lieu=lieu)

    def returnOne(self,id):
        etab = Etablissement.objects.get(id=id)
        return etab

    def delete(self,id):
        Etablissement.objects.filter(id=id).delete()

    def returnAll(self):
        MaListe = Etablissement.objects.all()
        return MaListe

    def isExist(self,nom,lieu):
        Etablissement.objects.filter(nom=nom, lieu=lieu).exists()
