from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Moviedetails, Watchlist
from django.core.paginator import Paginator
#from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

#@login_required
def index(request):
    #return render('page1.html', context_instance= RequestContext(request))
    

#def searchmovie(request):
    if 'q' in request.GET:
        q=request.GET['q']
        posts=Moviedetails.objects.filter(movie_title__contains=q)
    else:
        posts=Moviedetails.objects.all()

    paginator=Paginator(posts,2)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)
    return render(request,'page1.html',{'posts':posts_obj})

def watchlist_add(request, product_id):
    item_to_save = get_object_or_404(Moviedetails, pk=product_id)
    # Check if the item already exists in that user watchlist
    #if Moviedetails.objects.filter(user=request.user, item=rank).exists():
        #messages.add_message(request, messages.ERROR, "You already have it in your watchlist.")
        #return HttpResponseRedirect(reverse("auctions:index"))
    # Get the user watchlist or create it if it doesn't exists
    #t, created = Moviedetails.objects.get_or_create(id=item_to_save.id, year =item_to_save.year, movie_title=item_to_save.movie_title )
    user_list, created = Watchlist.objects.get_or_create(user=request.user)
    # Add the item through the ManyToManyField (Watchlist => item)
    user_list.item.add(item_to_save)
    user_list.save()
   
    messages.add_message(request, messages.SUCCESS, "Successfully added your watchlist")
    messages.add_message(request, messages.SUCCESS, "got")
    watch= Watchlist.objects.all()[0]
    #watch=Watchlist.objects.filter(user=request.user).count()
    return render(request, "page1.html",{'watch': watch.item.all()})

def getwatchlist(request):
    messages.add_message(request, messages.SUCCESS, "got")
    watch= Watchlist.objects.filter(user=request.user)
    lists=[1,2,3]
    
    #paginator=Paginator(watch,2)
    #page_number=request.GET.get('page')
    #watch_obj=paginator.get_page(page_number)
    return render(request,'try.html')
   # template = loader.get_template('page1.html')
    #return HttpResponse(template.render())
    # if request.method == "POST":
    #     searched = request.POST['searched']
	# 	#movies = Moviedetails.objects.filter(name__contains=searched)
	
    #     return render(request, 
	# 	'search.html', 
	# 	{'searched':searched,
	# 	})
    # else:
    #     return render(request, 
	# 	'search.html', 
	# 	{})
    #return render(request, 'search.html', {})
    #template = loader.get_template('search.html')
    #return ttpResponseH(template.render())

    
  #template = loader.get_template('search.html') 
  #return HttpResponse(template.render())


# def index(request):
#     return HttpResponse("Hellooo world!")

# Create your views here.
