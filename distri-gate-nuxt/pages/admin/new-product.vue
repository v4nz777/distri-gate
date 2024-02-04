<template>
    <div class="w-full h-16 bg-white shadow-md rounded-box flex items-center p-5">
        <span class="loading loading-bars loading-xs" v-if="saving"></span>
        <button class="btn btn-primary btn-xs flex gap-0" v-else @click="saveProduct" :disabled="!isReady">
            <svg viewBox="0 0 24 24" class="w-5 h-5" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M4 6C4 4.89543 4.89543 4 6 4H12H14.1716C14.702 4 15.2107 4.21071 15.5858 4.58579L19.4142 8.41421C19.7893 8.78929 20 9.29799 20 9.82843V12V18C20 19.1046 19.1046 20 18 20H6C4.89543 20 4 19.1046 4 18V6Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M8 4H13V7C13 7.55228 12.5523 8 12 8H9C8.44772 8 8 7.55228 8 7V4Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M7 15C7 13.8954 7.89543 13 9 13H15C16.1046 13 17 13.8954 17 15V20H7V15Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
            <span>Save Product</span>
        </button>
    </div>

    <div class="w-full h-max flex max-md:flex-col max-md:items-start mt-5 justify-start gap-10">
        <div class="w-full min-w-[12rem] max-w-md grid grid-cols-1 gap-3 content-start">
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
  
        <div class="w-full max-w-md  grid grid-cols-1 content-start gap-5">


            <label class="form-control w-full">
                <div class="label flex">
                    <span class="label-text-alt text-gray-500 font-bold">Product Title</span>
                    
                </div>
                <input :disabled="saving" type="text" placeholder="Premium Product X" class="input input-sm input-bordered input-base-300 w-full shadow" 
                    v-model="productForm.title" />
            </label>


            <ClientOnly>
                
                <div role="tablist" class="tabs tabs-lifted pb-10 tabs-lg">
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
                            :disabled="saving"
                            />


                        <button @click="addVariantForm(null)" class="btn btn-xs m-2 font-bold btn-ghost" :disabled="saving">
                            <svg class="w-5 h-5"  viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fill="currentColor" fill-rule="evenodd" clip-rule="evenodd" d="M11 17C11 17.5523 11.4477 18 12 18C12.5523 18 13 17.5523 13 17V13H17C17.5523 13 18 12.5523 18 12C18 11.4477 17.5523 11 17 11H13V7C13 6.44771 12.5523 6 12 6C11.4477 6 11 6.44771 11 7V11H7C6.44772 11 6 11.4477 6 12C6 12.5523 6.44772 13 7 13H11V17Z"></path> </g></svg>
                        </button>   
                </div>
            </ClientOnly>
         
        </div>
        
    </div>
    <div class="bg-red-500 w-full my-20">
            fds
    </div>
</template>

<script setup lang="ts">
    import type { ProductSubmit, ProductVariationSubmit, Product } from '~/types';
    import { UseImage } from '@vueuse/components';
    import { v4 as uuidv4 } from 'uuid';
    import { getIndexFromIdAndArray } from '~/utils'


    definePageMeta({
        layout: 'admin'
    })

    const alerstore = useAlertStore()


    // Variant Forms
    const { 
        selectedVariantForm,
        addVariantForm, 
        removeVariantForm, 
        executeVariantForm,
        setSelectedVariantForm
    } = useVariantFormControl('')
    

    // Product Forms
    const { 
        productForm, 
        saving,  
        saveProduct,
        isReady
    } = useProductFormControl()

    
    //Photo
    const { 
        temporaryPhoto, 
        setTemporaryPhoto 
    } = useTemporaryPhoto()


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
            console.log(productForm.variations[0].id)
            selectedVariantForm.value = productForm.variations[0].id
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
                                                            default:false
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
            selectedVariantForm, 
            addVariantForm,
            removeVariantForm, 
            executeVariantForm, 
            setSelectedVariantForm
        }

    }

    function useProductFormControl() {
        const productForm  = reactive<ProductSubmit>({
            title: '',
            category: '',
            id: `tempPID-${uuidv4()}`,
            variations: [{
                id:uuidv4(),
                name: undefined,
                variationDescription: '',
                variantImage:undefined,
                priceAmount:undefined,
                priceCurrencyCode:'PHP',
                priceCurrencySymbol:'₱',
                availableSupply:undefined,
                displayMode:'NAME_MODE',
                variantColor:undefined,
                default:true
            }]
        })

        const allVariantAreReady = computed(():boolean => {
            const { variations } = productForm
            const truthies:boolean[] = [];

            variations.forEach(variant => {
                let truthy  = false
                if(variant.displayMode==='THUMBNAIL_MODE') truthy = (
                    variant.variationDescription?.trim()!== '' &&
                    typeof variant.priceAmount !== 'undefined' &&
                    String(variant.priceAmount)?.trim()!== '' &&
                    typeof variant.availableSupply !== 'undefined' &&
                    String(variant.availableSupply)?.trim()!== '' &&
                    variant.priceCurrencyCode?.trim()!== '' &&
                    variant.priceCurrencySymbol?.trim()!== '' &&
                    typeof variant.variantImage !== 'undefined')

                else if(variant.displayMode==='COLOR_MODE') truthy = (
                    variant.variationDescription?.trim()!== '' &&
                    typeof variant.priceAmount !== 'undefined' &&
                    String(variant.priceAmount)?.trim()!== '' &&
                    typeof variant.availableSupply !== 'undefined' &&
                    String(variant.availableSupply)?.trim()!== '' &&
                    variant.priceCurrencyCode?.trim()!== '' &&
                    variant.priceCurrencySymbol?.trim()!== '' &&
                    typeof variant.variantColor !== 'undefined')

                else truthy = (
                    variant.variationDescription?.trim()!== '' &&
                    typeof variant.priceAmount !== 'undefined' &&
                    String(variant.priceAmount)?.trim()!== '' &&
                    typeof variant.availableSupply !== 'undefined' &&
                    String(variant.availableSupply)?.trim()!== '' &&
                    variant.priceCurrencyCode?.trim()!== '' &&
                    variant.priceCurrencySymbol?.trim()!== ''
                )
                truthies.push(truthy)
            });
          
            return !truthies.includes(false)

        })

        const isReady = computed(():boolean=>{
            const { title, variations } = productForm
            return title.trim() !== '' && allVariantAreReady.value
            
        })

        const saving = ref(false)



        
        const saveProduct =  async () => {
            saving.value = true
            const rawData = structuredClone(toRaw(productForm))

            const fd = toFormData(rawData)
            try {
                const response = await $fetch<Promise<Product>>('/api/products/new-product',{
                    method: 'post',
                    body: fd
                })
                productForm.id = response.id
                
                alerstore.addAlert({
                    id: 'tempId',
                    message: `Product: ${productForm.id} is saved!`,
                    type: 'success',
                    shown: true
                })
            } catch(error) {
                alerstore.addAlert({
                    id: 'tempId',
                    message: 'Error occured while saving product.',
                    type: 'error',
                    shown: true
                })
            }
            finally { saving.value = false }
        }

        return {
            productForm,
            saveProduct,
            saving,
            isReady
            
        }

    }

    // Utils
    function toFormData(productData:ProductSubmit ){

        const _fd = new FormData()

        _fd.append('title', productData.title)
        _fd.append('category', productData.category??'')
        _fd.append('id',productData.id)

        productData.variations.forEach((variant:ProductVariationSubmit,index)=>{
            
            for(const key in variant){
                if (Object.prototype.hasOwnProperty.call(variant, key)){
                    if(key==='variantImage'){
                        
                        _fd.append(`variations[${index}][${key}]`, variant[key]??new Blob(),variant[key]?.name )
                    }
                    else _fd.append(`variations[${index}][${key}]`,String(variant[key as keyof ProductVariationSubmit]??''))
                }
            }
            
        })

        return _fd
    }

    function getFileNameFromUrl(url:string|null|undefined):string{
        if(!url)return "" 
        const match =  url.match(/\/([^\/?#]+)(\?.*)?$/)
        
        return match?match[1]:""

    }
</script>

<style scoped>

</style>