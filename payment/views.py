from django.shortcuts import render
from django.http import HttpResponse
from database.models import paiment

def paymentViews(request):
    data = paiment.objects.all()
    print(data)
    return render(request,"./payment.html", context=data)
