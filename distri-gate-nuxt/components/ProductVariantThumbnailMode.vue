<template>
    
    <label :for="`variant-${variant.id}`" class="tooltip hover:after:delay-1000" :data-tip="variant.name">
        <div class="w-max h-max cursor-pointer hover:-translate-y-2 grayscale hover:grayscale-0 ease-in-out duration-1000" :class="variant.id === selectedVariant?' -translate-y-2 grayscale-0':''">
            <img :src="variant.variant_thumbnail" alt="" class="hover:shadow-fx object-contain h-10 w-10 ease-in-out duration-1000" :class="variant.id === selectedVariant?'shadow-fx':'shadow-fx-idle'">
        </div>
    </label>

    <input class="hidden" 
            type="radio" 
            :name="inputRadioGroupName" 
            :id="`variant-${variant.id}`" 
            v-model="selectedVariant" 
            :value="variant.id"/>
</template>

<script setup lang="ts">
    import type { ProductVariation } from '~/types';

    const selectedVariant = defineModel<number>({default:undefined})

    const props = defineProps<{
        variant: ProductVariation,
        inputRadioGroupName:string
    }>()

</script>

<style scoped>
    .hover\:shadow-fx:hover {
        filter: drop-shadow(0 6mm 1mm rgb(180, 180, 180));
    }
  
    .shadow-fx {
        filter: drop-shadow(0 6mm 1mm rgb(180, 180, 180));
    }

    .shadow-fx-idle {
        filter: drop-shadow(0 1.5mm 1.5mm rgb(180, 180, 180));
    }
</style>