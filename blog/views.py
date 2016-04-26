from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from .models import Post, Tag
from datetime import datetime
from django.utils import timezone

# home page displays most recent posts in list
def index(request, page=1):
    
    # get posts ordered by newest first
    posts_list = Post.objects.filter(posted__lte=timezone.now()).order_by('-posted')
    
    # paginate to 15 posts per page
    paginator = Paginator(posts_list, 15)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render(request, "blog/index.html", {'posts':posts})
    
# view indivivual post
def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post.html", {'post':post})
    
# list of all posts within a tag
def tag(request, tag, page=1):
    posts = Post.objects.order_by('-posted')
    
    # create list of tagged posts (currently empty)
    tagged_posts_list = []
    
    # check that post has tag, add post to list
    for post in posts:
        if tag in post.display_tags():
            tagged_posts_list.append(post)
            
    # paginate tag posts list
    paginator = Paginator(tagged_posts_list, 1)
    try:
        tagged_posts = paginator.page(page)
    except PageNotAnInteger:
        tagged_posts = paginator.page(1)
    except EmptyPage:
        tagged_posts = paginator.page(paginator.num_pages)
        
    return render(request, "blog/tag.html", {'posts':tagged_posts, 'tag':tag})
    
def about(request):
    return render(request, "blog/about.html")


""" SEARCH STUFF """
# god only knows how this works
import re

from django.db.models import Q

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query
    
def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        entry_query_title = get_query(query_string, ['title'])
        entry_query_text = get_query(query_string, ['body'])
        
        found_entries_title = Post.objects.filter(entry_query_title).order_by('-posted')
        found_entries_text = Post.objects.filter(entry_query_text).order_by('-posted')
        
    return render_to_response('blog/search_results.html', { 'query_string': query_string, 'found_entries_title': found_entries_title, 'found_entries_text': found_entries_text }, context_instance=RequestContext(request))
                          
def search_page(request):
    return render(request, 'blog/search.html')