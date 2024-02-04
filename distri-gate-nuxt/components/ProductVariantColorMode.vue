<template>
    
    <label :for="`variant-${variantId}`" class="cursor-pointer tooltip hover:after:delay-1000" :data-tip="variantName">
        <div class="w-6 h-6 rounded-md shadow-md" ref="colorBody"
        :class="variantId === selectedVariant?'border-2 hover:border-2 border-primary hover:border-primary':''">
        </div>
    </label>



    <input class="hidden"
            type="radio" 
            :name="inputRadioGroupName" 
            :id="`variant-${variantId}`" 
            v-model="selectedVariant" 
            :value="variantId"/>
</template>

<script setup lang="ts">
    import type { ProductVariation } from '~/types';

    const selectedVariant = defineModel<string>({default:null})

    const props = defineProps<{
        variantName: string,
        inputRadioGroupName:string,
        variantId:string,
        variantColor:string
    }>()

    const colorBody = ref<HTMLDivElement>()

    const setColor = (color:string|undefined=undefined)=> {
        if(colorBody.value){
            colorBody.value.style.backgroundColor = props.variantColor??color??'lightgray'
        }
    }

    onMounted(() => {
        setColor(props.variantColor)
    })

    watch(()=>props.variantColor, (value)=>{
        setColor(value)
    })

</script>

<style scoped>
    
</style>