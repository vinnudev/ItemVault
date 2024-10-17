from django.shortcuts import render
from .models import Item
from django.core.paginator import Paginator
import pytz

def item_list(request):
    items = Item.objects.all()    
    for item in items:
        item.created_at = item.created_at.astimezone(pytz.timezone('Asia/Kolkata'))
        
    sort = request.GET.get('sort', 'created_at')  #  sorting by created_at
    items = items.order_by(sort)

    paginator = Paginator(items, 10)  # Show 10 items per page
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'store/item_list.html', {'page_obj': page_obj})
