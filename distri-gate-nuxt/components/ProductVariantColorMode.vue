<template>
    
    <label :for="`variant-${variant.id}`" class="cursor-pointer">
        <div class="w-6 h-6 rounded-md shadow-md" ref="colorBody"
        :class="variant.id === selectedVariant?'border-2 hover:border-2 border-primary hover:border-primary':''">
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
        inputRadioGroupName:string,
        variantColor?:string
    }>()

    const colorBody = ref<HTMLDivElement>()

    const setColor = (color:string|undefined=undefined)=> {
        if(colorBody.value){
            colorBody.value.style.backgroundColor = props.variantColor??color??'lightgray'
        }
    }

    onMounted(() => {
        setColor(props.variant.variant_color)
    })

</script>

<style scoped>
    
</style>