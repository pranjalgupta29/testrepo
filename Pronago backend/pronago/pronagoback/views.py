from django.shortcuts import render
from .models import Join


# Create your views here.
def home(request):
    return render(request, 'pronagoback/home.html')


def join(request):
    if request.method == "POST":
        oname = request.POST.get('oname', '')
        cname = request.POST.get('cname', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip = request.POST.get('zip', '')
        gstin = request.POST.get('gstin', '')
        desc = request.POST.get('desc', '')
        join = Join(oname=oname, cname=cname, phone=phone, email=email, address=address, city=city, state=state,
                    zip=zip, gstin=gstin, desc=desc)
        join.save()
    return render(request, 'pronagoback/joinus.html')
