from django.db import models
from django.contrib.auth.models import AbstractUser

class administrator(AbstractUser):
    photoProfil = models.ImageField(upload_to="img_admin", blank=True,null=True)

class student(models.Model):
    add_by = models.ForeignKey(administrator,on_delete=models.DO_NOTHING, related_name="add-+" )
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    mention = models.CharField(max_length=50)
    niveau = models.CharField(max_length=20)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=150)
    adresse = models.CharField(max_length=150)
    photoEtudiant = models.ImageField(upload_to="img_student" , blank=True,null=True, default="./default.png")

    def __str__(self):
        return f"{self.nom} | {self.prenom}"

class paiment(models.Model):
    student_pay = models.OneToOneField(student, on_delete=models.CASCADE)
    premier = models.BooleanField(default=False)
    second = models.BooleanField(default=False)

    def __str__(self):return f"{self.student_pay.nom}"
