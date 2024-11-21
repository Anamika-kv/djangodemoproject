from django.shortcuts import render,redirect
from books.models import book
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required
def add(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p= request.POST['p']
        pa= request.POST['pa']
        l= request.POST['l']
        c=request.FILES['c']
        f=request.FILES['f']
        b=book.objects.create(title=t,author=a,price=p,pages=pa,language=l,cover=c,pdf=f)
        b.save()
        return view(request)

    return render(request,'add.html')
@login_required
def view(request):
    k=book.objects.all()#reads all recods from tables book
    context={'book':k} #passes all data from views to html,context is dictionary type
    return render(request,'view.html',context)
def detail(request,p):
    b=book.objects.get(id=p)
    context={'book':b}
    return render(request, 'detail'
                           '.html',context)
def edit(request,p):
    b = book.objects.get(id=p)
    if (request.method == "POST"):  # After submitting form
        b.title = request.POST['t']
        b.author = request.POST['a']
        b.price = request.POST['p']
        b.pages = request.POST['pa']
        b.language = request.POST['l']
        if (request.FILES.get('c') == None):
            b.save()
        else:
            b.cover = request.FILES.get('c')
        if (request.FILES.get('f') == None):
            b.save()
        else:
            b.pdf = request.FILES.get('f')
            b.save()
            return redirect('books:view')
    context = {'books': b}
    return render(request, 'edit.html',context)
def delete(request,p):
    b=book.objects.get(id=p)
    b.delete()
    return redirect('books:view')
from django.db.models import Q
def search(request):
    b=None #iniyialized  to none
    query=""
    if(request.method=="POST"):# after form submission
        query=request.POST['q']
        if query:
            b=book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query)) # django lookups
    return render(request, 'search.html',{'books':b,'query':query})



