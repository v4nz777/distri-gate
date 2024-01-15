<template>
    <div>
        <ClientOnly>
            <div class="flex gap-5 justify-center max-md:flex-col max-md:items-center">
                <CartSummary />
                <CartCheckout @backwards="navigateTo('/cart')" @forwards="proceedToPayment()"/>
            </div>
        </ClientOnly>
        
    </div>
</template>

<script setup lang="ts">
    const userstore = useUserStore()

    const proceedToPayment = ()=> {
        if(!userstore.isAuthenticated)userstore.showLoginFormDialog()
        else navigateTo('/cart/payment')
    }


    definePageMeta({
        layout:'cart',
        pageTransition: {
            name: 'cart-slide-left',
            mode: 'out-in'
        },

        middleware(to,from) {
            if(from.name==='cart-payment'||from.name==='cart-complete'){
                from.meta.pageTransition = {
                    name: 'cart-slide-right'
                }
            }
        }
    })
</script>

<style scoped>

</style>