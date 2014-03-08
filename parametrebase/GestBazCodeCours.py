from models import CodeCours

class GestBazProfesseur:

    def save(self,CodCour):
        CodCour.save()

    def modify(self,id,nom, grade,sem,ncour):
        CodeCours.objects.filter(id=id).update(nom=nom,grade=grade,sem=sem,ncour=ncour)

    def returneOne(self,id):
        CodCour = CodeCours.objects.get(id=id)
        return CodCour

    def delete(self,id):
        CodeCours.objects.filter(id=id).delete()

    def returneAll(self):
        MaListe = CodeCours.objects.all()
        return MaListe

    def isExist(self,nom,grade,sem,ncour):
        CodeCours.objects.filter(nom=nom,grade=grade,sem=sem,ncour=ncour).exists()
