<template>
    <!-- <button class="btn" onclick="add_to_cart_viewer.showModal()">open modal</button> -->
    <dialog id="add_to_cart_viewer" class="modal" ref="modal">


        <div class="modal-box">
            <h3 class="font-bold text-lg text-neutral text-center">Confirm Item!</h3>
            <div class="divider"></div>
            <div class="py-5 flex gap-5">
                <figure class="w-24 h-24">
             
                    <UseImage :src="itemForCart?itemForCart.product.image:''" class="w-full h-full object-contain">
                        <template #loading>
                        Loading Image..
                        </template>

                        <template #error>
                            <img src="/product.webp" class="w-full h-full object-contain">
                        </template>
                    </UseImage>
                </figure>
                <div class="flex flex-col justify-left gap-2">
                    <p class="font-semibold">{{ itemForCart?.product.title }}</p>
                    <p>{{ cartstore.currency.symbol }}{{ totalAmount.toFixed(2) }}</p>
                    <div class="flex gap-2 justify-center"> 
                        <button class="btn btn-sm text-lg font-bold" @click="decreaseItemForCartQuantity">-</button>

                        <span class="w-8 text-center border-b border-t font-bold">
                            {{ itemForCart?.quantity }}
                        </span>

                        <button class="btn btn-sm text-lg font-bold" @click="increaseItemForCartQuantity">+</button>
                    </div>
                    
                </div>
            </div>
            <div class="divider"></div>
            <div class="flex gap-5 justify-center"> 
                <button class="btn btn-ghost" @click="cancel">Cancel</button>
                <button class="btn btn-outline" @click="confirmCart">Confirm</button>
            </div>
            
        </div>


        <form method="dialog" class="modal-backdrop">
            <button>close</button>
        </form>
    </dialog>
</template>

<script setup lang="ts">
import type { Alert } from '~/types';
import { UseImage } from '@vueuse/components'

const itemForCart = useItemForCart()
const modal:Ref<HTMLDialogElement|null> = ref(null)
const cartstore = useCart()
const alertstore = useAlertStore()


const totalAmount = computed(()=> {
    if(!itemForCart.value?.product.price) return 0
    return itemForCart.value.product.price.amount * itemForCart.value?.quantity
})

const confirmCart = async ()=> {
    if(!itemForCart.value)return

    await cartstore.addItem({
        id: itemForCart.value.id,
        quantity: itemForCart.value.quantity,
        product:itemForCart.value.product,
        selected: false
    })

    alertstore.addAlert({
        id: 'temporary_id',
        type: 'temporary',
        css_class: 'alert',
        shown: true,
        message: `${itemForCart.value.quantity} new item/s added to your cart!`,
    })


    itemForCart.value=null
}

const cancel = ()=> {
    itemForCart.value = null
}

const increaseItemForCartQuantity = ()=> {
    if(itemForCart.value && itemForCart.value!==null){
        itemForCart.value.quantity++
    }
}

const decreaseItemForCartQuantity = ()=> {
    if(itemForCart.value && itemForCart.value!==null){
        itemForCart.value.quantity--
        if(itemForCart.value.quantity === 0) itemForCart.value=null
    }
}

onMounted(() => {
    modal.value?.addEventListener('close', ()=> {
        itemForCart.value = null
    })
})

watch(itemForCart,(value)=>{
    if(value){
        modal.value?.showModal()
    }else modal.value?.close()
    
})


</script>
