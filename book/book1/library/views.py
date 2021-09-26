from django.shortcuts import render
from django.shortcuts import render
from library.models import Book
from django.db.models import Q
# Create your views here.

def relative(request):
    return render(request,'relative.html')
def viewdetails(request):
    k=Book.objects.all()
    return render(request,'list.html',{'s':k})
def form3(request):
    if(request.method=="POST"):
        title=request.POST['title']
        author=request.POST['author']
        year = request.POST['year']
        publisher = request.POST['publisher']
        desc = request.POST['desc']
        pdf = request.FILES['pdf']
        cover = request.FILES['cover']

        s=Book.objects.create(title=title,author=author,year=year,publisher=publisher,desc=desc, cover=cover, pdf=pdf)
        s.save()
        return viewdetails(request)

    return render(request,'form3.html')
def search(request):
    if request.method == "POST":
        srch = request.POST['srh']
        if srch:
            match = Book.objects.filter(Q(title__icontains=srch) | Q(author__icontains=srch) | Q(publisher__icontains=srch) | Q(desc__icontains=srch) )
            if match:
                return render(request, 'search.html', {'sr': match})
            else:
                return search(request)
        else:

            messages.error(request, "NO results Found")
    return render(request,"search.html")