<template>
    <div class="w-64 h-80 card glass">
        <figure>
            <UseImage :src="product.image" class="w-full h-full object-contain bg-neutral-content">
                <template #loading>
                Loading..
                </template>

                <template #error>
                    <img src="/product.webp" class="w-full h-full object-contain bg-neutral-content">
                </template>
            </UseImage>
            <!-- <img :src="product.image" class="w-full h-full object-contain bg-neutral-content"
            :alt="product.title"/> -->
        </figure>
        <div class="card-body">
            <h2 class="card-title text-primary">{{ product.title }}</h2>
            <p class="">{{ product.description }}</p>
            <div class="card-actions justify-end items-center">
                <p class="font-semibold text-2xl text-primary">{{ product.price.currency_symbol }}{{ product.price.amount.toFixed(2) }}</p>
                <AddToCartBtn @click="initializeItemToCart"/>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
    import { UseImage } from '@vueuse/components'
    import type { Product } from '~/types';
    
    

    const props = defineProps<{
        product: Product
    }>()

    // const {} = useImage(props.product.image)

    
   
    const itemForCart = useItemForCart()

    const initializeItemToCart = ()=> {
        if(!props.product) return
        itemForCart.value = {
            id: props.product.id,
            quantity: 1,
            product: props.product,
            selected: false
        }
    }
</script>

<style scoped>

</style>