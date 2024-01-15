


export type Alert = {
    id: string
    type: 'temporary'|'error'|'sticky'|'success'
    css_class?: string
    message: string
    shown: boolean
    cta_message?: string
}



export type Item = {
    id: number;
    quantity: number;
    product: Product;
    selected:boolean;
}

export type Product = {
    id:number;
    title:string;
    description:string;
    price:Price
    image:string;
    category:string;
    rating:{
        rate: number,
        count:number
    }
}

export type GiftCode = {
    code?: string
    discount?: number
}

export type Price = {
    currency: string
    currency_symbol: string
    amount: number
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