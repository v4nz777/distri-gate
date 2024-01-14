<template>
    <div class="w-full flex justify-center">
        <ClientOnly>
            <CartPayment />
        </ClientOnly>
    </div>
</template>

<script setup lang="ts">
    definePageMeta({
        layout: 'cart',
        pageTransition: {
            name: 'cart-slide-left',
            mode: 'out-in'
        },
        
        middleware(to,from) {
            if(from.name==='cart-complete'){
                from.meta.pageTransition = {
                    name: 'cart-slide-right'
                }
            }
        }
    })
</script>

<style scoped>

</style>