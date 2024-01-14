<template>
    <div class="w-full">
        <ClientOnly>
            <TopNavCart/>
        
            <main class="w-full p-10">
                <div class="rounded-xl p-2 m-2 w-full flex justify-center">
                    <CartTimeline />
                </div>
                <div class="flex justify-center">
                    <slot />
                </div>
                
            </main>
            
            <dialog ref="loginForm" class="modal">
                <LoginForm @success="loginForm?.close()"/>
            </dialog>
            <LogoutUIDialog />

            <AlertsGroup/>
        </ClientOnly>
    </div>
</template>

<script setup lang="ts">
    const userstore = useUserStore()
    const loginForm = ref<HTMLDialogElement>()
    

    onMounted(async () => {
        await nextTick()
   
        if(!userstore.isAuthenticated){
            loginForm.value?.showModal()
        }
        
        
        
    })

 

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