import { type Product } from "~/types"

export default defineEventHandler(async (event):Promise<Product>=> {
    const dataFromClient = await readFormData(event)

    const api = serverAPI(event)

    const response = await api.post('/api/products/add_new_product',{
        body: dataFromClient
    })

    

    
    return response as unknown as Product
})