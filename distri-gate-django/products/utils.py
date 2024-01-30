from django.http import HttpRequest
from products.schemas import ProductInput, VariantInput


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
    
    # Covert to variations to list of VariantInput
    variant_input_list = []
    for variant in variations:
        converted = VariantInput(
            name = variations[variant]['name'],
            type = variations[variant]['displayMode'],
            variant_image = variations[variant]['variantImage'],
            variant_color = variations[variant]['variantColor'],
            price_amount = variations[variant]['priceAmount'],
            price_currency_code = variations[variant]['priceCurrencyCode'],
            price_currency_symbol = variations[variant]['priceCurrencySymbol'],
            supply_quantity = variations[variant]['availableSupply'],
            variation_description = variations[variant]['variationDescription'],
            is_default = variations[variant]['default'],
        )
        variant_input_list.append(converted)



   
    return ProductInput(
        title=title,
        category=category,
        variations=variant_input_list
    )
    