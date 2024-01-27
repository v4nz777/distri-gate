<template>
    <div class=" grid grid-cols-1 p-20">
        <button class="btn btn-ghost w-max text-primary font-bold" @click="navigateTo('/admin/new-product')">ADD NEW PRODUCT</button>
    </div>
</template>

<script setup lang="ts">
    definePageMeta({
        layout: 'admin'
    })
</script>

<style scoped>

</style>