from django.http import HttpRequest
from products.schemas import ProductInput, VariantInput
from django.core.files.uploadedfile import InMemoryUploadedFile

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
        image:InMemoryUploadedFile = request.FILES.get(f'variations[{variant_index}][variantImage]')
        variations[variant_index]['variantImage']=image.read()
        variations[variant_index]['variantImageName']=image.name

        
    
    # Convert from variations to list of VariantInput
    variant_input_list = []
    for variant in variations:
        converted = VariantInput(
            name = variations[variant]['name'][0],
            type = variations[variant]['displayMode'][0],
            variant_image = variations[variant]['variantImage'],
            variant_image_name = variations[variant]['variantImageName'],
            variant_color = variations[variant]['variantColor'][0],
            price_amount = float(variations[variant]['priceAmount'][0]),
            price_currency_code = variations[variant]['priceCurrencyCode'][0],
            price_currency_symbol = variations[variant]['priceCurrencySymbol'][0],
            supply_quantity = int(variations[variant]['availableSupply'][0]),
            variation_description = variations[variant]['variationDescription'][0],
            is_default = variations[variant]['default'][0]=='true',
        )
        variant_input_list.append(converted)



   
    return ProductInput(
        title=title,
        category=category,
        variations=variant_input_list
    )
    