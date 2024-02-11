<template>
    <div class="navbar bg-base-100">
        <div class="flex-1">
            <NuxtLink class="btn btn-ghost text-xl" to="/products">
                <img src="/logo.svg" class="h-12" alt="">
            </NuxtLink>
        </div>
        <div class="flex-none">
            
            <div class="dropdown dropdown-end" v-if="userstore.isAuthenticated">
                <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
                    <div class="w-10 rounded-full">
                        <UseImage :src="userstore.currentUser?.avatar?userstore.currentUser.avatar:''">
                            <template #error>
                                <img alt="Tailwind CSS Navbar component" src='/profile.png' />
                            </template>
                            <template #loading>
                                <img alt="Tailwind CSS Navbar component" src='/profile.png' />
                            </template>
                        </UseImage>
                    </div>
                </div>
                <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
                    <li>
                    <a class="justify-between">
                        Profile
                        <span class="badge">New</span>
                    </a>
                    </li>
                    <li><a>Settings</a></li>
                    <li><a @click="userstore.clearUser()">Logout</a></li>
                </ul>
            </div>
        </div>  
    </div>
</template>

<script setup lang="ts">
    import { UseImage } from '@vueuse/components';
    const cartstore = useCart()
    const userstore = useUserStore()
</script>

<style scoped>

</style>