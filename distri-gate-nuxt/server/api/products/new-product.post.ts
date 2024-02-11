import { type ProductSubmit, type Product, type ProductVariationSubmit } from "~/types"

export default defineEventHandler(async (event):Promise<Product>=> {
    const dataFromClient = await readFormData(event)

    const api = serverAPI(event)

    const response = await api.post<Promise<Product>>('/api/products/add_or_update_product',{
        body: dataFromClient
    })

    

    return response as unknown as Product
})