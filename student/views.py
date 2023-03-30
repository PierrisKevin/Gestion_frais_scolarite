from django.shortcuts import redirect, render
from database.models import student, paiment
from django.contrib.auth.decorators import login_required

@login_required
def studentviews(request):
    students = student.objects.all()
    # admin = administrator.objects.get(username="Pierris")
    # print(admin)
    print(request.user)
    context = {"students":students, "active":"student"}
    if request.method=="POST":
        test = request.POST.get("valeur")
        if test=="add":
            nom = request.POST.get("nom")
            prenom = request.POST.get("prenom")
            birth = request.POST.get("birthday")
            lieuNaissance = request.POST.get("lieuNaissance")
            adresse =  request.POST.get("adresse")
            mention =request.POST.get("mention")
            niveau = request.POST.get("niveau")
            image = request.FILES.get("image-student")

            save_student = student.objects.create(add_by=request.user, 
                                                nom=nom,
                                                prenom=prenom,
                                                mention=mention.upper(),
                                                niveau=niveau,
                                                date_naissance=birth,
                                                lieu_naissance=lieuNaissance,
                                                adresse=adresse,
                                                photoEtudiant=image)
            save_student.save()
            paiment.objects.create(student_pay=save_student)
        elif test=="chercher":
            values = request.POST.get("search")
            if values:
                context["students"]=student.objects.filter(nom__icontains=values, mention=request.POST.get("filiere"))
        else:
            id = request.POST.get("identifiant")
            studentId = student.objects.get(id=id)

            nom = request.POST.get("username")
            prenom = request.POST.get("prename")
            birth = request.POST.get("birth")
            lieuNaissance = request.POST.get("lieuDeNaissance")
            adresse =  request.POST.get("adresseChange")
            mention =request.POST.get("filiereCHange")
            niveau = request.POST.get("niveauChange")

            studentId.nom=nom
            studentId.prenom=prenom
            studentId.mention=mention.upper()
            studentId.niveau=niveau
            #studentId.date_naissance=birth,
            studentId.lieu_naissance=lieuNaissance
            studentId.adresse=adresse

            studentId.save()

    return render(request, "./student.html", context=context)


def deleteStudent(request, id):
    studs = student.objects.get(id=id)
    studs.delete()
    return redirect('student')

@login_required
def paymentViews(request):
    data = paiment.objects.all()
    content = {'allpay':data, "active":"payment"}
    if request.method=="POST":
        identifiant = request.POST.get("identiiant")
        print("identifiant est : ",identifiant)
        dataget = paiment.objects.get(id=identifiant)
        primo = False
        secondo = False
        if request.POST.get("premier"):primo=True
        if request.POST.get("deuxieme"):secondo=True

        dataget.premier = primo
        dataget.second = secondo
        dataget.save()

    return render(request,"./payment.html", context=content)
