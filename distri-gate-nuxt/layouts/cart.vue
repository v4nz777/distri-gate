<template>
    <div class="w-full px-5">
        <ClientOnly>
            <TopNavCart/>
        
            <main class="w-full p-10">
                <div class="rounded-xl p-2 mx-2 w-full flex justify-center">
                    <CartTimeline />
                </div>
                <div class="flex justify-center">
                    <slot />
                </div>
                
            </main>
            
            
            <LoginFormDialog />
            <LogoutUIDialog />
            <AlertsGroup class="z-50"/>

        </ClientOnly>
    </div>
</template>

<script setup lang="ts">
   

</script>

<style>
    .cart-slide-left-enter-from,
    .cart-slide-left-leave-to,
    .cart-slide-right-enter-from,
    .cart-slide-right-leave-to {
    transition: all 0.5s;
    }


    .cart-slide-left-enter-from {
        transform: translate(40%, 0);
        opacity: 0;
    }

    .cart-slide-left-leave-to {
        transform: translate(-40%, 0);
        opacity: 0;
    }

    .cart-slide-right-enter-from {
        transform: translate(-40%, 0);
        opacity: 0;
    }

    .cart-slide-right-leave-to {
        transform: translate(40%, 0);
        opacity: 0;
    }
</style>