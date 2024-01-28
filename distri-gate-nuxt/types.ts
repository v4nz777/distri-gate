


export type Alert = {
    id: string
    type: 'temporary'|'error'|'sticky'|'success'
    css_class?: string
    message: string
    shown: boolean
    cta_message?: string
}



export type Item = {
    variantId: number;
    quantity: number;
    productId: number;
    productTitle: string;
    productVariant: ProductVariation;
    selectedVariantIndex?: number;
    selected:boolean;
}

export type Product = {
    id:number;
    title:string;
    description:string;
    image:string;
    category:string;
    variations: ProductVariation[];
    default_variant: number;
    discounted:boolean;
    new:boolean;
    original:boolean;
}



export type ProductVariation = {
    id: number
    name: string
    type: string
    variant_image?: string
    variant_color?: string
    variant_thumbnail?:string
    price_amount: number
    price_currency_code: string
    price_currency_symbol: string
    variant_description: string
    supply_quantity: number
}

export type GiftCode = {
    code?: string
    discount?: number
}


export type AccessToken = {
    access_token: string
}

export type Address = {
    id: string
    full_address_string?: string
    address_line?: string
    street?: string
    city: string
    province: string
    country: string
    postal_code: string
    contact: string
    contact_person: string
}

export interface User {
    id: number
    username: string
    first_name?: string
    last_name?: string
    full_name?:string
    avatar?:string

}

export interface PrivateUser extends User {
    address?: Address[] | []
    address_current?: Address
    email?: string
    contact_number?: string
    
}



export type AddressSubmit = {
    form_contact_person:string
    form_contact:string
    form_address_line?:string
    form_street?:string
    form_city:string
    form_postal_code:string
    form_province:string
    form_country:string
}

export type ProductSubmit = {
    title: string
    category?: string
    variations: ProductVariationSubmit[]
}

export type ProductVariationSubmit = {
    id:string
    name?: string
    displayMode: 'NAME_MODE' | 'THUMBNAIL_MODE'| 'COLOR_MODE'
    variantImage?: File | null
    variantColor?:string
    priceAmount?:  string
    priceCurrencyCode?: string
    priceCurrencySymbol?: string
    variationDescription?: string
    availableSupply?:string,
    default:boolean

}

export type ProductImageDataSubmit = {
    name: string
    type: string
    data: string
}