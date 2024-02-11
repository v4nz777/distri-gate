<template>
    <ClientOnly>
    <div class="card w-96 bg-base-100 shadow-xl">
        <div class="mx-10 mt-10 px-10 py-5 bg-primary flex justify-center items-center rounded-lg">
            <p class="w-max h-max rounded-lg font-black text-white text-4xl">DISTRIGATE</p>
        </div>
        <div class="card-body items-center text-center">
            <h2 class="card-title text-2xl font-bold">{{ userstore.currentUser?.username }}</h2>
            <p class="font-thin">You are about to be logged out...</p>
            <div class="card-actions">
                <span class="loading loading-bars loading-lg text-primary"></span>
            </div>
        </div>
    </div>
    </ClientOnly>
</template>

<script lang="ts" setup>
    const userstore = useUserStore()
    const emits = defineEmits(['loggingOut','exited'])

    watch(()=>userstore.exiting, (value)=> {
        if(value)emits('loggingOut')
        else emits('exited')
    },{deep:true})
</script>

<style scoped>

</style>