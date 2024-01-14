
import type { Product } from "~/types"

export default defineEventHandler(async (event):Promise<Product|null> => {
    const id = getRouterParam(event, 'id')

    const response = await $fetch(`${process.env.DJANGO_SERVER_URL}/api/products/${id}`)
    
    
    return response as Product

})


