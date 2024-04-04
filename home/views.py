from django.shortcuts import render,redirect
from . import models
from django.http import HttpResponse

# Create your views here.
def get_all_products(request):
    products = models.Product.objects.all()
    return render(request=request,template_name='home/products.html',context={'products':products})

def get_product(request,pk):
    product = models.Product.objects.get(pk=pk)
    return render(request=request,template_name='home/product_detail.html',context={'product':product})
    

def review_form(request,product_id):
    if request.method == "GET":
        return render(request,'home/review_form.html')
    elif request.method == "POST":
        author = request.POST.get('author')
        text = request.POST.get('text')
        rating = request.POST.get('rating')
        
        try:
            product = models.Product.objects.get(pk=product_id)
        except models.Product.DoesNotExist:
            return HttpResponse('product does not exist',status=404)

        review = models.Review.objects.create(
            product=product,
            author= author,
            text=text,
            rating=rating,
        )
        review.save()
        return redirect('product-detail',pk=product_id)
        
