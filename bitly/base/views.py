from django.shortcuts import render

# Create your views here.
def base(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username,password)
        return render(request,"base.html",{'name':request.POST["username"]})

    return render(request,"base.html")