from django.shortcuts import get_object_or_404, redirect, render

from .forms import productform
from .models import product


def create_product(request):
    form = productform(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('create_product')

    return render(request, 'form_app/product_form.html', {'form': form})


def product_details(request, pk):
    item = get_object_or_404(product, pk=pk)
    return render(request, 'form_app/product_details.html', {'product': item})


def product_search(request):
    query = request.GET.get('query', '').strip()
    results = product.objects.filter(name__icontains=query) if query else []
    return render(request, 'form_app/productsearch.html', {'results': results, 'query': query})
