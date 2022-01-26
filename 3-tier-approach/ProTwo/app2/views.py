from django.shortcuts import render

# Create your views here.


def signup(request):
    if request.method == "POST":
        user = request.POST['user']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass']
    else:
        return render(request, 'b.html')