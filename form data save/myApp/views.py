from django.shortcuts import render

from django.http import HttpResponseRedirect

from myApp.forms import Register

from myApp.models import RegisterForm

# Create your views here.
def home(req):
    if req.method == "POST":
        form = Register(req.POST)
        if form.is_valid():
            formname = form.cleaned_data["Fullname"]
            formmail = form.cleaned_data["Email"]
            formpass = form.cleaned_data["Password"]

            # print(fullname, "\t",email, "\t",password)
            # Insert Data
            # user = RegisterForm(fullname = formname, email = formmail, password = formpass)
            # user.save()

            # Update Data
            # user = RegisterForm(id=2,fullname = formname, email = formmail, password = formpass)
            # user.save()

            # Delete Data
            user = RegisterForm(id = 2)
            user.delete()

            return HttpResponseRedirect("success/")
    else:    
        form = Register
    return render(req, "home.html", {"form" : form})


def success(req):
    return render(req, "success.html")