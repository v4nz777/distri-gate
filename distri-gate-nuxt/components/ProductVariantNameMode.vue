<template>
    
    <label :for="`variant-${variant.id}`" 
        class="btn btn-xs"
        :class="variant.id === selectedVariant?'border-2 hover:border-2 border-primary hover:border-primary':''">
        {{ variant.name }}
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

    const selectedVariant = defineModel<string>({default:undefined})

    const props = defineProps<{
        variant: ProductVariation,
        inputRadioGroupName:string
    }>()

</script>

<style scoped>
    
</style>