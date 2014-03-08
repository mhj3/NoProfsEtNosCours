from models import CodePrograme

class GestBazProfesseur:

    def save(self,CodProg):
        CodProg.save()

    def modify(self,id,domaine, mention,specialite,typeCour,langue):
        CodePrograme.objects.filter(id=id).update(domaine=domaine,mention=mention,specialite=specialite,typeCour=typeCour,langue=langue)

    def returneOne(self,id):
        CodProg = CodePrograme.objects.get(id=id)
        return CodProg

    def delete(self,id):
        CodePrograme.objects.filter(id=id).delete()

    def returneAll(self):
        MaListe = CodePrograme.objects.all()
        return MaListe

    def isExist(self,domaine, mention,specialite,typeCour,langue):
       CodePrograme.objects.filter(domaine=domaine,mention=mention,specialite=specialite,typeCour=typeCour,langue=langue).exists()


