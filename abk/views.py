from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from .forms import EnquiryForm

def home(request):
    categories = ProductCategory.objects.all()
    return render(request, 'abk/home.html', {'categories': categories})

def product_list(request):
    category_slug = request.GET.get('category')
    if category_slug:
        products = Product.objects.filter(category__slug=category_slug)
    else: 
        products = Product.objects.all()
    return render(request, 'abk/product_list.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'abk/product_detail.html', {'product': product})

def contact(request):
    from .forms import EnquiryForm
    success_message = ''
    error_message = ''
    
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "✅ Thank you! Your enquiry has been submitted."
            form = EnquiryForm()  # reset form
        else:
            error_message = "❌ Please correct the errors below."
    else:
        form = EnquiryForm()

    return render(request, 'abk/contact.html', {
        'form': form,
        'success_message': success_message,
        'error_message': error_message
    })
