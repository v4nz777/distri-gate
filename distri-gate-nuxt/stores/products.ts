
import { skipHydrate } from "pinia"
import type { Product } from "~/types"

export const useProducts = defineStore('products-store', ()=> {

    const products = ref<Product[]>([])
    const fetching = ref<boolean>(true)

    const getAllProducts = async () => {
        const { data, pending, error, refresh } = await useFetch('/api/products',{})
        fetching.value = pending.value
        if(data.value)products.value = data.value as Product[]
    }

    return {
        products,
        fetching,

        getAllProducts
    }
})