from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.template import RequestContext
from .models import Moviedetails, Watchlist, Towatch, Liked
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# def home(request):
#     return render(request, 'home.html')

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

@login_required
def index(request):
    
    if 'q' in request.GET:
        q=request.GET['q']
        posts=Moviedetails.objects.filter(movie_title__contains=q)
        paginator=Paginator(posts,2)
        page_number=request.GET.get('page')
        posts_obj=paginator.get_page(page_number)
        return render(request,'page1.html',{'posts':posts_obj})
    else:
        posts=Moviedetails.objects.filter(release = 'n')
        return render(request,'first.html',{'posts':posts})

@login_required
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
    #messages.add_message(request, messages.SUCCESS, "got")
    watch= Watchlist.objects.all()[request.user.id-1]
    #watch=Watchlist.objects.filter(user=request.user).count()  
    return render(request, "page2.html",{'watch': watch.item.all() })

@login_required
def towatch_add(request, product2_id):
    item_to_save = get_object_or_404(Moviedetails, pk=product2_id)
    # Check if the item already exists in that user watchlist
    #if Moviedetails.objects.filter(user=request.user, item=rank).exists():
        #messages.add_message(request, messages.ERROR, "You already have it in your watchlist.")
        #return HttpResponseRedirect(reverse("auctions:index"))
    # Get the user watchlist or create it if it doesn't exists
    #t, created = Moviedetails.objects.get_or_create(id=item_to_save.id, year =item_to_save.year, movie_title=item_to_save.movie_title )
    user_list, created = Towatch.objects.get_or_create(user=request.user)
    # Add the item through the ManyToManyField (Watchlist => item)
    user_list.item.add(item_to_save)
    user_list.save()
   
    messages.add_message(request, messages.SUCCESS, "Successfully added your watchlist")
    #messages.add_message(request, messages.SUCCESS, "got")
    watch2= Towatch.objects.all()[request.user.id-1]
    #watch=Watchlist.objects.filter(user=request.user).count()  
    return render(request, "page3.html",{'watch2': watch2.item.all() })

@login_required
def liked_add(request, product3_id):
    item_to_save = get_object_or_404(Moviedetails, pk=product3_id)
    # Check if the item already exists in that user watchlist
    #if Moviedetails.objects.filter(user=request.user, item=rank).exists():
        #messages.add_message(request, messages.ERROR, "You already have it in your watchlist.")
        #return HttpResponseRedirect(reverse("auctions:index"))
    # Get the user watchlist or create it if it doesn't exists
    #t, created = Moviedetails.objects.get_or_create(id=item_to_save.id, year =item_to_save.year, movie_title=item_to_save.movie_title )
    user_list, created = Liked.objects.get_or_create(user=request.user)
    # Add the item through the ManyToManyField (Watchlist => item)
    user_list.item.add(item_to_save)
    user_list.save()
   
    messages.add_message(request, messages.SUCCESS, "Successfully added your watchlist")
    #messages.add_message(request, messages.SUCCESS, "got")
    watch3= Liked.objects.all()[request.user.id-1]
    #watch=Watchlist.objects.filter(user=request.user).count()  
    return render(request, "page4.html",{'watch3': watch3.item.all() })


def getwatchlist(request):
    messages.add_message(request, messages.SUCCESS, "got")
    watch= Watchlist.objects.filter(user=request.user)
    lists=[1,2,3]
    
    #paginator=Paginator(watch,2)
    #page_number=request.GET.get('page')
    #watch_obj=paginator.get_page(page_number)
    return render(request,'try.html')


