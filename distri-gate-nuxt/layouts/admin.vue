<template>
    <div class="flex h-screen gg">
        <aside class="">
            
            <ul class="menu bg-base-200 w-56 h-full shadow-lg">
                <li class="menu-title mb-5">
                    <a @click="navigateTo('/admin')">
                        <h2 class="font-black text-primary">DISTRIGATE ADMIN</h2>
                    </a>
                </li>
                <li>
                    <AdminItemStore :open="links.store.some(item=>item.link===router.name)"/>
                </li>
          
            </ul>
        </aside>
        <main class="w-full h-full p-10 pb-20">
            <h1 class="font-bold text-lg">{{ title }}</h1>
            <div class="divider"></div>
            <slot/>
            <AlertsGroup/>
        </main>
    </div>
    
</template>

<script setup lang="ts">
    const router = useRoute()

    const title = computed(()=>{
        return links.store.find(item=>item.link===router.name)?.title
    })
    const links = {
        store: [
            {   
                title: 'Products',
                link:'admin-products'
            }, 
            {   
                title: 'Add Product',
                link:'admin-new-product'
            }
        ]
    }
    
</script>

<style scoped>

</style>