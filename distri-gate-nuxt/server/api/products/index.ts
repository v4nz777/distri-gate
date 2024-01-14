import type { Product } from "@/types"
import { pgConnection } from "~/server/utils/database"


export default defineEventHandler(async(event):Promise<Product[]>=> {
    const api = serverAPI(event)

    const response = await api.get('/api/products/get_products')
    return response as Product[]

})




const sqlResponse = async ():Promise<Product[]> => {
    try
        {
            const sql = pgConnection()

            return await sql`

                SELECT * FROM "Product";
            
            ` as Product[]
        }

    catch(error)
        {
            console.log(error)
            return [] as Product[]
        }
}



const demoResponse = ():Promise<Product[]>=>{
    return new Promise((resolve,reject)=> {
        setTimeout(() => {
            resolve(
                [
                    {
                        id:0,
                        title: 'title',
                        description: 'lorem epsum',
                        price: {
                            currency: 'PHP',
                            currency_symbol: '₱',
                            amount: 100,
                        },
                        image: '/product-demo1.png',
                        category: '',
                        rating: {
                            rate: 5,
                            count: 10
                        },
                    },
                    {
                        id:1,
                        title: 'title 2',
                        description: 'lorem epsum 3',
                        price: {
                            currency: 'PHP',
                            currency_symbol: '₱',
                            amount: 500,
                        },
                        image: '/product-demo2.png',
                        category: '',
                        rating: {
                            rate: 5,
                            count: 10
                        },
                    }
                ]
            )
        }, 2000);
    })
}