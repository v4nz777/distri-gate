<template>
    <div>
        <ClientOnly fallback-tag="span" fallback="Preparing cart...">
            <div class="flex gap-5 justify-center max-md:flex-col max-md:items-center">
                <CartTable />
                <CartSubtotal @backwards="navigateTo('/products')" @forwards="proceedToCheckout()"/>
            </div>
        </ClientOnly>
        
        
    </div>
    
</template>

<script setup lang="ts">
    const userstore = useUserStore()

    
    const proceedToCheckout = ()=> {
        if(!userstore.isAuthenticated)userstore.showLoginFormDialog()
        else navigateTo('/cart/checkout')
    }

    definePageMeta({
        layout:'cart',
        pageTransition: {
            name: 'cart-slide-left',
            mode: 'out-in',
        },

        middleware(to,from) {

            // For transition
            if(from.name==='cart-checkout'||from.name==='cart-payment'||from.name==='cart-complete'){
                from.meta.pageTransition = {
                    name: 'cart-slide-right'
                }
            }

            
        }
    })




    
</script>

<style scoped>

</style>