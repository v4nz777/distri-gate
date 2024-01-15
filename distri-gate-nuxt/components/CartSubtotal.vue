<template>
    <div class="bg-white p-5 rounded-lg shadow-lg w-[350px] h-max"> 
        <div class="divider mb-10">
            <h2 class="text-center text-lg font-bold">ORDER</h2>
        </div>
        <div class="w-full border-b">
            <div class="w-full flex justify-between text-sm">
                <p>SUBTOTAL</p>
                <p>{{cartstore.currency.symbol + cartstore.cartSubTotalAmount.toFixed(2) }}</p>
            </div>

            <div class="w-full flex justify-between text-sm">
                <p>SHIPPING</p>
                <p>{{cartstore.currency.symbol + cartstore.shipping.toFixed(2) }}</p>
            </div>
        </div>

        <div class="w-full flex justify-end text-sm">
              <p>{{cartstore.currency.symbol + (cartstore.cartSubTotalAmount + cartstore.shipping).toFixed(2) }}</p>
        </div>

        <div class="w-full mb-5 pb-5 py-5 mt-8">
            <input type="text" placeholder="Enter Gift Code..." class="input input-bordered input-sm w-full max-w-xs mb-5" />
            <div class="w-full flex justify-between text-xs" v-if="cartstore.discount">
                <p>DISCOUNT</p>
                <p>{{'-' + cartstore.currency.symbol + cartstore.discount.toFixed(2) }}</p>
            </div>
            <div class="w-full flex justify-between text-sm font-bold">
                <p>TOTAL</p>
                <p>{{cartstore.currency.symbol + cartstore.cartTotalAmount.toFixed(2) }}</p>
            </div>
            <div class="flex justify-center gap-5 border-t p-5">
                <button class="btn btn-sm btn-ghost" @click="emits('backwards')">ADD MORE</button>
                <button class="btn btn-sm btn-primary" @click="emits('forwards')">PROCEED</button>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
    const cartstore = useCart()
    const emits = defineEmits(['backwards', 'forwards'])

</script>

<style scoped>

</style>