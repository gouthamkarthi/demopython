from .models import Category


# part of url creation
def menu_links(request):
    link = Category.objects.all()
    return dict(link=link)
