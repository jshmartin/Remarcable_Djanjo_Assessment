from django.template import loader
from django.http import HttpResponse
from .models import Product

def items(request):
  myitems = Product.objects.all().values()
  template = loader.get_template('all_items.html')
  context = {
    'myitems':myitems,
  }

  return HttpResponse(template.render(context, request))

def details(request, id):
  myitems = Product.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myitems': myitems,
  }

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())