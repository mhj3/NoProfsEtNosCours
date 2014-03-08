from django.db import models

# Create your models here.
class Etablissement(models.Model):
    Nom = models.CharField(max_length=250, unique=True)
    Lieu = models.CharField(max_length=250)

    def __unicode__(self):
        return self.Nom


class CodeCours(models.Model):
    Grade = models.CharField(max_length=2)
    Semestre = models.CharField(max_length=2)
    NomCours = models.CharField(max_length = 30)

    def __unicode__(self):
        return u'%s-%s-%s' % (self.Grade, self.Semestre, self.NomCours)


class CodePrograme(models.Model):
    Domaine = models.CharField(max_length=2)
    Mention = models.CharField(max_length=2)
    Specialite = models.CharField(max_length=3)
    Type_de_cours = models.CharField(max_length=2)
    Langue = models.CharField(max_length=2)

    def __unicode__(self):
        return u'%s-%s-%s-%s-%s' %(self.Domaine, self.Mention, self.Specialite, self.Type_de_cours, self.Langue)

class Professeur(models.Model):
    Nom= models.CharField(max_length=25)
    Prenom = models.CharField(max_length=40)
    No_identite = models.CharField(max_length=15)
    cv = models.CharField(max_length=250)

    def __unicode__(self):
        return u'%s %s' % (self.Nom, self.Prenom)

class Cours(models.Model):
    codecours = models.ForeignKey(CodeCours)
    codeprogram = models.ForeignKey(CodePrograme)
    prof = models.ForeignKey(Professeur) and models.ManyToManyField(Professeur)
   # profs =
    titre = models.CharField(max_length=30)
    credits = models.IntegerField(max_length=1)
    lieu = models.CharField(max_length=40)
    public_cible = models.CharField(max_length=25)
    pre_requis = models.CharField(max_length=30)
    objectif = models.CharField(max_length=100)
    description =models.CharField(max_length=250)
    plan = models.CharField(max_length=300)
    forma = models.CharField(max_length = 50, verbose_name='format')
    ressource = models.CharField(max_length=50)
    evaluation = models.CharField(max_length=50)

    def __unicode__(self):
        return self.titre
