from django.http import HttpRequest
from products.schemas import ProductInput, VariantInput
from django.core.files.uploadedfile import InMemoryUploadedFile
from users.models import User
from products.models import Product, ProductVariant
from django.core.files.base import ContentFile



def update_product(existing_product:Product, changed:ProductInput)->Product:
    existing_product.title = changed.title
    existing_product.category = changed.category

    added_variants = set_variants_and_add_default(existing_product,changed)

    # Remove variants that are not in changed
    updated_variants = filter_out_variants(added_variants,existing_product)

    return existing_product





def save_new_product(product_input:ProductInput, seller:User)-> Product:
    new_product = Product.objects.create(
        title = product_input.title,
        category = product_input.category,
        seller = seller
    )

    set_variants_and_add_default(new_product,product_input.variations)
    
    new_product.save()
    return new_product





def filter_out_variants(added_variants:list[ProductVariant], _from:Product)->list[ProductVariant]:
    """Remove variants from product if not in the list of `added_variants`"""

    current_variants = _from.variations

    for current in current_variants:
        if current not in added_variants:
            current_variants.remove(current)
    
    _from.save()
    
    return _from.variations




def set_variants_and_add_default(product:Product,variants_input:list[VariantInput])->list[ProductVariant]:

    added_variants = []

    for variant in variants_input:

        # This will likely trigger for updating product
        if ProductVariant.objects.filter(id=variant.temporary_id).exists():
            target_variant = ProductVariant.objects.get(id=variant.temporary_id)
            update_variant(target_variant,variant)
        # This will likely trigger on new product
        else:
            target_variant = save_new_variant(variant,product)
        
        # Add variant to product
        product.variations.add(target_variant)

        # Set as default variant
        if variant.is_default:
            product.default_variant = ProductVariant.objects.get(id=variant.temporary_id)
        
        added_variants.append(target_variant)

    product.save()
    return added_variants




def update_variant(variant:ProductVariant, changes:VariantInput)->ProductVariant:
    variant.name = changes.name
    variant.type = changes.type
    variant.name = changes.name
    variant.variant_description = changes.variation_description
    variant.price_amount = changes.price_amount
    variant.price_currency_code = changes.price_currency_code
    variant.price_currency_symbol = changes.price_currency_symbol
    
    # avoid image duplication:
    if variant.variant_image.name != changes.variant_image_name and variant.variant_image != b'':
        
        variant.variant_image.save(
            changes.variant_image_name,
            ContentFile(changes.variant_image,changes.variant_image_name),
            save=True)

    variant.save()
    return variant





def save_new_variant(variant:VariantInput, group:Product)->ProductVariant:
    # Initiating new variant
    new_variant = ProductVariant.objects.create(
        id    = variant.temporary_id,
        group = group,
        type  = variant.type,
        name  = variant.name,
        variant_description = variant.variation_description,
        price_amount  = variant.price_amount,
        price_currency_code    = variant.price_currency_code,
        price_currency_symbol  = variant.price_currency_symbol
    )

    # Add the image to the variant
    if variant.variant_image != b'':
        new_variant.variant_image.save(
            variant.variant_image_name,
            ContentFile(variant.variant_image,variant.variant_image_name),
            save=True)
        
    new_variant.save()
    return new_variant





def transform_product_input_data(request:HttpRequest)->ProductInput:
    
    title = request.POST.get('title')
    category = request.POST.get('category')
    product_id = request.POST.get('id')
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
            temporary_id = variations[variant]['id'][0],
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
        temporary_id=product_id,
        variations=variant_input_list
    )
    