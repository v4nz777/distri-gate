<template>
    
    <label :for="`variant-${variantId}`" 
        class="btn btn-xs"
        :class="variantId === selectedVariant?'border-2 hover:border-2 border-primary hover:border-primary':''">
        {{ variantName }}
    </label>

    <input class="hidden" 
            type="radio" 
            :name="inputRadioGroupName" 
            :id="`variant-${variantId}`" 
            v-model="selectedVariant" 
            :value="variantId"/>
</template>

<script setup lang="ts">
   

    const selectedVariant = defineModel<string>({default:undefined})

    const props = defineProps<{
        variantId: string,
        variantName: string,
        inputRadioGroupName:string
    }>()

</script>

<style scoped>
    
</style>