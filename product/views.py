from .models import Product

from django.views import View
from django.http import  HttpResponse, JsonResponse

class CategoryListView(View):
    def get(self, request):
        product_data = Product.objects.all()
        category_list = []
        for data in product_data:
            category_list.append(
                {
                    'id'  : data.id,
                    'category_id' : data.category_id,
                    'name' : data.name,
                    'price' : data.price
                }
            )
        return JsonResponse({"category_list":category_list}, status = 200)
