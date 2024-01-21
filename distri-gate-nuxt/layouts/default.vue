<template>
    <div class="w-full px-5 h-screen">
        <ClientOnly>
            <TopNav/>
        </ClientOnly>
        <slot />
        <LogoutUIDialog />
        <AlertsGroup/>
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