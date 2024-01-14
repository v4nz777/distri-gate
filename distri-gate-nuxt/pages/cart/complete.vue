<template>
    <div class="w-full flex justify-center">
        <ClientOnly>
            <CartComplete/>
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

    })
</script>

<style scoped>

</style>