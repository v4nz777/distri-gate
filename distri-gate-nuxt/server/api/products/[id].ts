
import type { Product } from "~/types"

export default defineEventHandler(async (event):Promise<Product|null> => {
    const id = getRouterParam(event, 'id')
    const api = serverAPI(event)
    
    const response = await api.get(`/api/products/get_product/${id}`)
    
    return response as Product

})


