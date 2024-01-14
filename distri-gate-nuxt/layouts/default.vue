<template>
    <div class="w-full">
        <ClientOnly>
            <TopNav/>
        </ClientOnly>
        <slot />
        <LogoutUIDialog />
        <AlertsGroup/>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped>

</style>