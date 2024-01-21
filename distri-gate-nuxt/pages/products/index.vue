<template>
    <div class="px-10 pt-28">
        <div v-if="productstore.fetching"  class="grid lg:grid-cols-4 md:grid-cols-2 sm:grid-cols-1 gap-5 justify-items-center">
            <div v-for="skeleton in 8" class="w-64 h-80 grid grid-cols-1">
                <div class="skeleton w-full h-52"></div>
                <div class="w-full h-8 flex gap-5">
                    <div class="skeleton h-8 w-8 rounded-full"></div>
                    <div class="skeleton h-full w-full"></div>
                </div>
                <div class="skeleton w-full h-4"></div>
                <div class="skeleton w-full h-4"></div>

            </div>
        </div>
        
        <ul v-else class="grid lg:grid-cols-4 md:grid-cols-2 sm:grid-cols-1 gap-5 justify-items-center">
            <li v-for="product in productstore.products" :key="product.id" class="w-max">
                <ProductCard :product="product" @clicked="navigateTo(`/products/${product.id}`)"/>
            </li>
        </ul>
     
    </div>
    <AddToCartViewer />

</template>

<script setup lang="ts">
    const productstore = useProducts()
    const itemForCart = useItemForCart()
    onMounted( async () => {
        await nextTick()
        await productstore.getAllProducts()
    })


</script>

<style scoped>

</style>