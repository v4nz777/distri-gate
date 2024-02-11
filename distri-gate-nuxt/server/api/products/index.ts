import type { Product } from "@/types"
import { pgConnection } from "~/server/utils/database"


export default defineEventHandler(async(event):Promise<Product[]>=> {
    const api = serverAPI(event)

    const response = await api.get('/api/products/get_products')
    return response as Product[]

})

