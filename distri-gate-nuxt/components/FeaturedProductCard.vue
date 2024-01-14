<template>
    <div class="card w-52 bg-base-100 shadow-xl hover:scale-105 h-full" @click="navigateTo('/products')">
        <figure class="px-10 pt-10 w-full h-[270px] min-h-[260px]">
            <UseImage :src="product?product.image:''" alt="" class="rounded-xl bg-neutral-content h-full">
                <template #loading>
                    Loading
                </template>
                <template #error>
                    <img src="/product.webp" class="rounded-xl bg-neutral-content">
                </template>
            </UseImage>
        </figure>
        <div class="card-body items-center text-center">
            <h2 class="card-title text-primary">{{ product?.title }}</h2>
            <p>{{ product?.description }}</p>
            <div class="card-actions">
            <!-- <button class="btn btn-primary">Buy Now</button> -->
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
    import type { Product } from '~/types';
    import { UseImage } from '@vueuse/components';


    const { productId } = defineProps(['productId'])

    const product = ref<Product|null>({} as Product)

    onMounted(async () => {
      const { data, pending, error, refresh } = await useFetch(`/api/products/${productId}`)
      product.value = data.value
      console.log(data.value)
    })

</script>

<style scoped>

</style>