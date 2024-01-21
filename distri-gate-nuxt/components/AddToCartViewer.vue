<template>
    <!-- <button class="btn" onclick="add_to_cart_viewer.showModal()">open modal</button> -->
    <dialog id="add_to_cart_viewer" class="modal ease-out duration-500" ref="modal">


        <div class="modal-box">
            <h3 class="font-bold text-lg text-neutral text-center">Confirm Item!</h3>
            <div class="divider"></div>
            <div class="py-5 flex gap-5">
                <figure class="w-24 h-24">
             
                    <UseImage :src="itemForCart?.productVariant.variant_image??'#'" class="w-full h-full object-contain">
                        <template #loading>
                        Loading Image..
                        </template>

                        <template #error>
                            <img src="/product.webp" class="w-full h-full object-contain">
                        </template>
                    </UseImage>
                </figure>
                <div class="flex flex-col justify-left gap-2">
                    <p class="font-semibold">{{ itemForCart?.productTitle}}</p>
                    <p class="font-bold text-xs">&#8212;{{ itemForCart?.productVariant.name}}</p>
                    <p class="">{{ cartstore.currency.symbol }}{{ totalAmount.toFixed(2) }}</p>
                    <div class="flex gap-2 justify-start"> 
                        <button class="btn btn-sm text-lg font-bold" @click="decreaseItemForCartQuantity">-</button>

                        <span class="w-8 text-center border-b border-t font-bold">
                            {{ itemForCart?.quantity }}
                        </span>

                        <button :disabled="futureSupply<1" class="btn btn-sm text-lg font-bold" @click="increaseItemForCartQuantity">+</button>
                    </div>
                    
                </div>
            </div>
            <div class="divider"></div>
            <div class="flex gap-5 justify-center"> 
                <button class="btn btn-ghost" @click="cancel">Cancel</button>
                <button class="btn btn-outline btn-primary" @click="confirmCart">Confirm</button>
            </div>
            
        </div>


        <form method="dialog" class="modal-backdrop">
            <button>close</button>
        </form>
    </dialog>
</template>

<script setup lang="ts">
import type { Alert, Product } from '~/types';
import { UseImage } from '@vueuse/components'


const itemForCart = useItemForCart()
const modal:Ref<HTMLDialogElement|null> = ref(null)

const cartstore = useCart()
const alertstore = useAlertStore()

const futureSupply = computed(()=> {
    if(!itemForCart.value)return 0
    return itemForCart.value.productVariant.supply_quantity - (itemForCart.value.quantity)
})


const totalAmount = computed(()=> {
    if(!itemForCart.value?.productVariant.price_amount) return 0
    return itemForCart.value.productVariant.price_amount * itemForCart.value?.quantity
})



const confirmCart = async ()=> {
    if(!itemForCart.value)return

    await cartstore.addItem({
        variantId: itemForCart.value.variantId,
        productId: itemForCart.value.productId,
        productTitle: itemForCart.value.productTitle,
        quantity: itemForCart.value.quantity,
        productVariant: itemForCart.value.productVariant,
        selectedVariantIndex: itemForCart.value.selectedVariantIndex,
        selected: false,
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
        const toCartQuantity = itemForCart.value.quantity??0
        const fromCartQuantity = cartstore.getItemCountFromCart(itemForCart.value.variantId)??0
        const variantSupply = itemForCart.value.productVariant.supply_quantity??0

        if(variantSupply - (toCartQuantity+fromCartQuantity) < 1)return
                    

        itemForCart.value.quantity++
    }
}

const decreaseItemForCartQuantity = ()=> {
    if(itemForCart.value && itemForCart.value!==null){
        itemForCart.value.quantity--
        if(itemForCart.value.quantity === 0) itemForCart.value=null
    }
}


onMounted( () => {
    modal.value?.addEventListener('close', ()=> {
        itemForCart.value = null
    })
})

watch(itemForCart,(value)=>{
    if(value){
        modal.value?.showModal()
    }else modal.value?.close()
    
},{deep:true})


</script>
