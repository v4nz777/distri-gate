from django.http import HttpRequest
from products.schemas import ProductInput


def transform_product_input_data(request:HttpRequest)->ProductInput:
    
    title = request.POST.get('title')
    category = request.POST.get('category')
    variations = {}

    for key,value in request.POST.lists():

        # Filter variants and then index it.
        if key.startswith('variations'):
            index = int(key.split('[')[1].split(']')[0])
            prop = key.split('[')[2].split(']')[0]

            # Append variant
            if index not in variations:
                variations[index] = {}

            variations[index][prop] = value
    
    # Handle file upload
    for variant_index in variations:
        image = request.FILES.get(f'variations[{variant_index}][variantImage]')
        variations[variant_index]['variantImage']=image
    
    return ProductInput(
        title=title,
        category=category,
        variations=variations
    )
    