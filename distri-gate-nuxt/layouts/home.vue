<template>
    <div class="w-full">
        <slot />
    </div>
</template>

<script setup lang="ts">
    const userstore = useUserStore()


    onMounted(async () => {
        await userstore.setUser(userstore.loggedUser)
    })
    
</script>

<style scoped>

</style>