from django.template import loader
from django.http import HttpResponse
from .models import Category, Product, Tag

def items(request):
    myitems = Product.objects.all().values()
    template = loader.get_template('all_items.html')
    context = {
        'myitems':myitems,
    }

    return HttpResponse(template.render(context, request))

def details(request, id):
    myitem = Product.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myitem': myitem,
    }
    return HttpResponse(template.render(context, request))

def search(request):
    query = request.GET.get('q', '').strip()
    selected_category_id = request.GET.get('category', None)
    selected_tags_ids = request.GET.getlist('tags')
    
    # gather all products and all current categories and tags for the filter dropdowns
    results = Product.objects.all()
    all_tags = Tag.objects.all()
    all_categories = Category.objects.all()

    selected_category = Category.objects.filter(id=selected_category_id).first() if selected_category_id else None
    selected_tags = Tag.objects.filter(id__in=selected_tags_ids) if selected_tags_ids else None
    print(f"Selected category: {selected_category}")
    print(f"Selected tags: {selected_tags}")
    
    # add filters based on the query parameters
    if query:
        results = results.filter(description__icontains=query)
    
    if selected_category_id:
        results = results.filter(category_id=selected_category_id)
    
    if selected_tags_ids:
        results = results.filter(tags__id__in=selected_tags_ids).distinct()

    template = loader.get_template('search.html')
    context = {
        'results': results,
        'query': query,
        'selected_category_id': selected_category_id,
        'selected_tags_ids': selected_tags_ids,
        'all_tags': all_tags,
        'all_categories': all_categories,
        'selected_category': selected_category,
        'selected_tags': selected_tags,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request))