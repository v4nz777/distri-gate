<template>
    <div class="bg-white p-5 rounded-lg shadow-lg w-full max-w-xl min-h-[500px] h-max flex flex-col justify-between"> 
        <div class="divider mb-10">
            <h2 class="text-center text-lg font-bold">PAYMENTS</h2>
        </div>

        <div class="flex justify-center gap-5 border-t p-5 justify-self-end">
                <button class="btn  btn-ghost" @click="navigateTo('/cart/checkout')">BACK</button>
                <button class="btn btn-primary" @click="navigateTo('/cart/complete')">PAY</button>
        </div>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped>

</style>