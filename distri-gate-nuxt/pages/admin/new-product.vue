<template>
    
    <div class="w-full h-max flex max-md:flex-col max-md:items-start mt-5 justify-start gap-10">
        

        <div class="w-full max-w-md  grid grid-cols-1 content-start gap-5">

            <label class="form-control w-full">
                <div class="label flex">
                    <span class="label-text-alt text-gray-500 font-bold">Product Title</span>
                    <button class="btn btn-primary btn-xs">Save Product</button>
                </div>
                <input type="text" placeholder="Premium Product X" class="input input-sm input-bordered input-base-300 w-full shadow" />
            </label>
            <ClientOnly>
            <div role="tablist" class="tabs tabs-lifted pb-10">
                    <NewProductVariantForm v-for="forme in productForm.variations" :key="forme.id" 
                        v-model="selectedVariantForm"
                        :tabLabel="forme.name||'VARIANT'" 
                        radioGroup="variant-radio"
                        :variantData="forme"
                        :isDefault="forme.default"
                        @photoChanged="setTemporaryPhoto" 
                        @save="executeVariantForm" 
                        @onSelected="setSelectedVariantForm"
                        @onRemoved="removeVariantForm"
                        />


                    <button @click="addVariantForm(null)" class="btn btn-xs m-2 font-bold btn-ghost">
                        <svg class="w-5 h-5"  viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fill="currentColor" fill-rule="evenodd" clip-rule="evenodd" d="M11 17C11 17.5523 11.4477 18 12 18C12.5523 18 13 17.5523 13 17V13H17C17.5523 13 18 12.5523 18 12C18 11.4477 17.5523 11 17 11H13V7C13 6.44771 12.5523 6 12 6C11.4477 6 11 6.44771 11 7V11H7C6.44772 11 6 11.4477 6 12C6 12.5523 6.44772 13 7 13H11V17Z"></path> </g></svg>
                    </button>   
            </div>
            </ClientOnly>
         
        </div>
        <div class="w-full min-w-[28rem] max-w-md grid grid-cols-1 gap-3 content-start">
          
            <figure class="p-5 hover:scale-125  ease-in-out duration-1000">
                <UseImage :src="temporaryPhoto" class="w-full h-full object-contain drop-shadow-lg">
                    <template #loading>
                        <LogoAnimationLoading class="w-full h-full object-contain"/>
                    </template>
                    <template #error>
                        <img src="/product.webp" class="w-full h-full object-contain"/>
                    </template>
                </UseImage>
            </figure>
        </div>
    </div>
</template>

<script setup lang="ts">
    import type { ProductSubmit, ProductVariationSubmit } from '~/types';
    import { UseImage } from '@vueuse/components';
    import { v4 as uuidv4 } from 'uuid';
    import { getIndexFromIdAndArray } from '~/utils'


    definePageMeta({
        layout: 'admin'
    })

    // Variant Forms
    const { 
        selectedVariantForm, 
        addVariantForm, 
        removeVariantForm, 
        executeVariantForm,
        setSelectedVariantForm
    } = useVariantFormControl('')
    
    

   


    // Product Forms
    const productForm  = reactive<ProductSubmit>({
        title: '',
        description:'',
        category: '',
        variations: [{
            id:uuidv4(),
            name: undefined,
            variationDescription: undefined,
            variantImage:undefined,
            priceAmount:undefined,
            priceCurrencyCode:undefined,
            priceCurrencySymbol:undefined,
            availableSupply:undefined,
            displayMode:'NAME_MODE',
            variantColor:undefined,
            default:false
        }]
    })


    //Photo
    const { temporaryPhoto, setTemporaryPhoto } = useTemporaryPhoto()


    // Hooks
    onMounted(()=>{   
   
    })



    //Inline Composables
    function useTemporaryPhoto(initial:string='') {
        const temporaryPhoto = toRef('')

        const setTemporaryPhoto = (photoUrl:string)=> {
            temporaryPhoto.value = photoUrl
        }

        return {
            temporaryPhoto,
            setTemporaryPhoto
        }
    }

    function useVariantFormControl(initial:string=''){

        const selectedVariantForm = toRef(initial)

        const removeVariantForm = (variantId:string)=>{
        const index = getIndexFromIdAndArray(variantId,productForm.variations)
        productForm.variations.splice(index,1)
        selectedVariantForm.value = productForm.variations[index-1].id
        }

        const addVariantForm = (variantData:ProductVariationSubmit|null|undefined)=>{
            productForm.variations.push(variantData ??  {
                                                            id:uuidv4(),
                                                            name: undefined,
                                                            variationDescription: undefined,
                                                            variantImage:undefined,
                                                            priceAmount:undefined,
                                                            priceCurrencyCode:undefined,
                                                            priceCurrencySymbol:undefined,
                                                            availableSupply:undefined,
                                                            displayMode:'NAME_MODE',
                                                            variantColor:undefined,
                                                            default:true
                                                        }
            )
        }

        const executeVariantForm = (variantData:ProductVariationSubmit)=> {
            const exists = productForm.variations.find((variant)=>variant.id===variantData.id)
            if(!exists)productForm.variations.push(variantData)
        }

        const setSelectedVariantForm = (varId:string,photoUrl:string)=> {
            setTemporaryPhoto(photoUrl)
        }

        

        return {
            selectedVariantForm, addVariantForm,removeVariantForm, executeVariantForm, setSelectedVariantForm
        }

    }
</script>

<style scoped>

</style>