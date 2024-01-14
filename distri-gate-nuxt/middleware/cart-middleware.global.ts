
export default defineNuxtRouteMiddleware((to, from) => {
    const cartstore = useCart()
    const userstore = useUserStore()

    // Redirect to products page if CART is EMPTY except CART/COMPLETE
    if(to.name==='cart' || to.name==='cart-checkout' || to.name==='cart-payment'){
        if (process.client) {
            if(cartstore.items.length < 1) return navigateTo('/products')
        }
    }

     // For login if not authenticated
     if(to.name==='cart-checkout'||to.name==='cart-payment'||to.name==='cart-complete'){
           
        if(!userstore.isAuthenticated){
            return abortNavigation()
        }
    }
})
