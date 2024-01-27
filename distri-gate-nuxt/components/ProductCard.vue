<template>
    <div class="w-64 h-[420px] card glass">
        <figure @click="emits('clicked')" class="min-h-[180px] max-h-[180px]">
            <UseImage :src="product.variations[getIndexFromIdAndArray(product.default_variant,product.variations)].variant_image??'#'" class="w-full h-full object-contain bg-neutral-content hover:scale-125 cursor-pointer ease-in-out duration-1000" >
                <template #loading>
                    <LogoAnimationLoading class="w-full h-full object-contain bg-neutral-content cursor-pointer"/>
                </template>

                <template #error>
                    <img src="/product.webp" class="w-full h-full object-contain bg-neutral-content hover:scale-125 cursor-pointer ease-in-out duration-1000">
                </template>
            </UseImage>
            <!-- <img :src="product.image" class="w-full h-full object-contain bg-neutral-content"
            :alt="product.title"/> -->
        </figure>
        <div class="card-body">
            <div class="tooltip tooltip-top w-full" :data-tip="product.title">
                <h2 class="card-title text-primary font-normal text-lg line-clamp-1" @click="emits('clicked')">{{ product.title }}</h2>
            </div>
            <p class="line-clamp-1 text-sm text-neutral font-light w-full">{{ product.description||'No description' }}</p>
            <div class="card-actions justify-end items-center">
                <p class="font-semibold text-2xl text-primary">{{ cartstore.currency.symbol }}{{ product.variations[getIndexFromIdAndArray(product.default_variant,product.variations)].price_amount.toFixed(2) }}</p>
                <button class="btn btn-primary font-bold" @click="emits('clicked')">BUY</button>
                <!-- <AddToCartBtn @click="initializeItemToCart"/> -->
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
    import { UseImage } from '@vueuse/components'
    import type { Product } from '~/types';
    import { getIndexFromIdAndArray } from '~/utils'
    
    const cartstore = useCart()

    const emits = defineEmits(['clicked'])

    const props = defineProps<{
        product: Product
    }>()

    
   
    const itemForCart = useItemForCart()
</script>

<style scoped>

</style>