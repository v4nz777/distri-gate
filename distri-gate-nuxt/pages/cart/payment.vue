<template>
    <div class="w-full flex justify-center">
        <ClientOnly>
            <CartPayment @backwards="navigateTo('/cart/checkout')" @forwards="pay()"/>
        </ClientOnly>
    </div>
</template>

<script setup lang="ts">
    const userstore = useUserStore()
    const pay = ()=> {
        if(!userstore.isAuthenticated)userstore.showLoginFormDialog()
        else navigateTo('/cart/complete')
    }


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