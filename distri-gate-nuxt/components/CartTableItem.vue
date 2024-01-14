<template>
<th>
    <label>
        <input type="checkbox" class="checkbox" v-model="item.selected"/>
    </label>
</th>

<td>
    <div class="flex items-center gap-3">
        <div class="avatar">
        <div class="mask mask-squircle w-12 h-12">
          
            <UseImage :src="item.product.image" :alt="item.product.description">
                <template #loading>
                Loading..
                </template>

                <template #error>
                    <img src="/product.webp">
                </template>
            </UseImage>
        </div>
        </div>
        <div>
        <div class="font-bold">{{ item.product.title }}</div>
        <div class="text-sm opacity-50">{{item.product.price.currency_symbol}}{{ item.product.price.amount }}</div>
        </div>
    </div>
</td>

<td>
    
    
    
    <div class="flex gap-2">
        <button class="btn btn-ghost btn-sm text-xl" @click="cartstore.changeQuantity(item.id,'decrease')">-</button>
        <span class="font-bold w-3 text-center flex items-center justify-center">
            {{ item.quantity }}
        </span>
        <button class="btn btn-ghost btn-sm text-xl" @click="cartstore.changeQuantity(item.id,'increase')">+</button>

    </div>
    
</td>

<td>{{item.product.price.currency_symbol}} {{ (item.product.price.amount*item.quantity).toFixed(2) }}</td>

<th>
    <div class="tooltip font-light hover:tooltip-open tooltip-top" data-tip="Remove item">
        <button class="btn btn-ghost btn-sm" @click="cartstore.removeItem(item.id)">
            <svg class="w-4 h-4" version="1.1" id="svg2" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" sodipodi:docname="remove.svg" inkscape:version="0.48.4 r9939" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1200 1200" enable-background="new 0 0 1200 1200" xml:space="preserve" fill="#000000"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path id="path18404" inkscape:connector-curvature="0" d="M0,264.84L335.16,600L0,935.16L264.84,1200L600,864.84L935.16,1200 L1200,935.16L864.84,600L1200,264.84L935.16,0L600,335.16L264.84,0L0,264.84z"></path> </g></svg>
        </button>
    </div>
</th>

</template>

<script setup lang="ts">
    

    import type { Item } from '~/types';
    import { UseImage } from '@vueuse/components'

    const props = defineProps<{
        item:Item,
    }>()

    const cartstore = useCart()

</script>

<style scoped>

</style>