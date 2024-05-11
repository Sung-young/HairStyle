from django.shortcuts import render,get_object_or_404,redirect
from .models import Community
from .forms import CommunityForm
from django.core.paginator import Paginator
# Create your views here.

def home (request):
    return render(request, 'home.html')

def hairstyle(request):
    return render(request, 'hairstyle.html')

def community_home(request):
    communities = Community.objects.all()
    paginator = Paginator(communities, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'community.html', {'page_obj': page_obj})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_community = Community()
    new_community.title = request.POST.get('title')
    new_community.content = request.POST.get('content')
    new_community.author = request.user
    new_community.save()
    return redirect('detail', new_community.id)

def detail(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    return render(request,'community_detail.html',{'community': community})

def edit(request, community_id):
    edit_community = get_object_or_404(Community, pk=community_id)
    if edit_community.author != request.user:
        return redirect('community_home')
    return render(request, 'edit.html', {'edit_community':edit_community})

def update(request, community_id):
    old_community = get_object_or_404(Community, pk=community_id)
    old_community.title = request.POST.get('title')
    old_community.content = request.POST.get('content')
    old_community.save()
    return redirect('detail', old_community.id)

    if form.is_valid():
        new_community = form.save(commit=False)
        new_community.save()
        return redirect('community_detail', old_community.id)

    return render(request, 'new.html', {'old_community': old_community})

def delete(request, community_id):
    delete_community = get_object_or_404(Community, pk=community_id)
    delete_community.delete()
    return redirect('community_home')

def map(request):
    return render(request, 'map.html')

def hair1(request):
    return render(request, 'hair/hair1.html')
def hair2(request):
    return render(request, 'hair/hair2.html')
def hair3(request):
    return render(request, 'hair/hair3.html')
def hair4(request):
    return render(request, 'hair/hair4.html')
def hair5(request):
    return render(request, 'hair/hair5.html')
def hair6(request):
    return render(request, 'hair/hair6.html')