from django.template import Library
from blog.models import Tag, Post
from operator import itemgetter

register = Library()

@register.filter(name="taglist")
def taglist(value):
    tags = Tag.objects.all().order_by('name')
    tagslist = {}
    
    for tag in tags:
        name = tag.name
        instances = Post.objects.filter(tags=tag).count()
        tagslist[name] = instances
    
    sorted_list = sorted(tagslist.items(), key=itemgetter(1), reverse=True)
    
    return sorted_list