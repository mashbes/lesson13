from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Shortly

def index(request):
    urls = Shortly.objects.all().order_by('-visited')[:7]
    return render(request, 'shortly_app/index.html', {'urls':urls})

def create_short_link(request):
    if request.method == 'POST':
        new_url = request.POST.get('url')
        try:
            link = Shortly.objects.get('new_url')
        except Shortly.DoesNotExist as e:
            link = Shortly('new_url')
            link.save()
        return redirect('/short/' + str(link.url_id))
    return redirect('/shortly')

def follow_link(request, url_id):
    try:
        link = Shortly.objects.get(url_id=url_id)
        link.visited += 1
        link.save()
    except Shortly.DoesNotExist:
        return render(request, 'shortly_app/error.html', {'error': 'There are some mistakes in link'})
    return HttpResponseRedirect(link.url)

def details(request, url_id):
    try:
        link = Shortly.objects.get(url_id=url_id)
    except Shortly.DoesNotExist as e:
        print (e)
    return render(request, 'shortly_app/get_short.html', {'link': link})

def error404(request):
    return render(request, 'shortly_app/error.html', {'error': 'Short link is incorrect'})