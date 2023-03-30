from django.shortcuts import render
from database.models import paiment,student
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    allStudent = student.objects.all()
    nothing = paiment.objects.filter(premier=False,second=False)
    primo = paiment.objects.filter(premier=True, second=False)
    second = paiment.objects.filter(premier=False ,second=True)
    total = paiment.objects.filter(premier=True, second=True)
    stat = [(len(nothing)/len(allStudent))*100, (len(primo)+len(second))*100/len(allStudent), len(total)/len(allStudent)*100]

    money = (len(primo)+len(second))*225000+len(total)*450000
    print(stat)
    return render(request, "./dashboard.html", context={"statistique": stat, "nbStudent": len(allStudent), "revenu": money, "manque":len(second)+len(primo), "active":"dash"})
