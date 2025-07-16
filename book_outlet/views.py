from django.shortcuts import render

# Create your views here.
def index(request):
    books=Book.objects.all()
    return render(request,"book_outlet/index.html",{
        "books":books
    })