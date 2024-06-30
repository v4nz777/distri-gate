<template>
    <!-- <div class="flex flex-col items-center justify-start w-full mt-14" :class="logoLoaded?'h-[150vh]':''"> -->
    <div class="flex flex-col items-center justify-start w-full mt-14" id="home-container">
        <LogoAnimation class="w-full md:w-[680px]" @animationDone="loadElements"/>

        <Transition>
            <div v-if="logoLoaded" class="flex flex-col w-max items-center justify-center">
                <p class="text-primary text-2xl italic animate-write text-left self-start">Where your products begin!</p>
                <!-- <div class="divider"></div> -->
                <button class="btn btn-primary text-white w-max mt-8" @click="navigateTo('/products')">GO TO SHOP</button>
            </div>
        </Transition>

        <div class="my-24 flex flex-col justify-center" v-if="itemsLoaded">
            <div class="divider w-96 self-center text-neutral">Featured Products</div>
            
            <TransitionGroup class="w-full flex gap-5 justify-center" tag="ul" name="list">
                <li v-for="item in featuredItems" :key="item" class="w-max" >
                    <FeaturedProductCard :productId="item" />
                </li>
            </TransitionGroup>
            
        </div>

        
       
        
    </div>
</template>

<script setup lang="ts">

    const logoLoaded = ref(false)
    const itemsLoaded = ref(false)
    const featuredItems = ref<string[]>([])

    definePageMeta({
        layout: 'home'
    })

    const loadElements = async ()=> { 
        logoLoaded.value = true
        await nextTick()
        const writeAnimationElement = document.querySelector('.animate-write')
    
        writeAnimationElement?.addEventListener('animationend', ()=>{
            itemsLoaded.value = true
            setTimeout(() => {
                featuredItems.value.push('4JjgiqPPhYGvtpwKYWKYVi') 
            }, 500);

            setTimeout(() => {
                featuredItems.value.push('4JjgiqPPhYGvtpwKYWKYVi') 
            }, 750);
            setTimeout(() => {
                featuredItems.value.push('4JjgiqPPhYGvtpwKYWKYVi') 
            }, 1000);
            
         

        })
        
    }


    



</script>

<style scoped>
    .v-enter-active,
    .v-leave-active {
    transition: opacity 2s ease;
    }

    .v-enter-from,
    .v-leave-to {
    opacity: 0;
    }


    .list-enter-active,
    .list-leave-active {
    transition: all 0.5s ease;
    }
    .list-enter-from,
    .list-leave-to {
    opacity: 0;
    transform: translateY(-30%);
    }

    .animate-write {
        white-space: nowrap;
        overflow: hidden;
        animation: write 2s forwards
    }

    @keyframes write {
        0% {
            width: 0%;
        }

        100% {
            width: 100%;
        }
    }



</style>