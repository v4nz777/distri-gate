<template>
    
    <ProductPageSkeleton v-if="pending" />
    <div v-else class="w-full h-full flex p-10 max-md:flex-col max-md:items-center mt-5 justify-center gap-20">

        <div class="w-full h-max min-w-[28rem] max-w-md max-h-[776px] grid grid-cols-1 gap-3 content-start">

            <div class="w-full h-max rounded-xl">
                <figure class="p-5 hover:scale-150 h-[400px] ease-in-out duration-1000">
                    <UseImage :src="product?.variations[selectedVariantIndex].variant_image??'#'" class="w-full h-full object-contain drop-shadow-lg">
                        <template #loading>
                            <LogoAnimationLoading class="w-full h-full object-contain"/>
                        </template>
                        <template #error>
                            <img src="/product.webp" class="w-full h-full object-contain"/>
                        </template>
                    </UseImage>
                </figure>
            </div>

            <!-- <div class="w-full h-36 grid grid-cols-3 gap-3">

                <div class="bg-primary-content class w-full h-36 max-w-36 rounded-lg">
                </div>

                <div class="bg-primary-content class w-full h-36 max-w-36 rounded-lg">
                </div>

                <div class="bg-primary-content class w-full h-36 max-w-36 rounded-lg">
                </div>

            </div> -->
        </div>

        <div class="w-full h-[576px] max-w-md max-h-[576px] grid grid-cols-1 content-start gap-5">
            <div>
                <h2 class="font-normal text-4xl text-primary ">{{ product?.title }}</h2>
                <div class="flex gap-2 py-2">
                    <div class="badge badge-sm bg-orange-500 text-white">NEW!</div>
                    <div class="badge badge-sm badge-success text-white">DISCOUNTED!</div>
                    <div class="badge badge-sm badge-primary">ORIGINAL</div>
                </div>
            </div>
            
            <p class="text-md  flex gap-2">
                <span class="font-bold text-primary">&#8212; {{ product?.variations[selectedVariantIndex].name }}</span>
            </p>
            <div>
                <p class="text-xs text-neutral mb-3 font-semibold">Choose variation:</p>
                <ul class="flex gap-2 items-end">
                    <li v-for="variant in product?.variations">

                        <ProductVariantNameMode v-if="variant.type === 'NAME_MODE'"
                            :variant="variant" 
                            inputRadioGroupName="product-variant" 
                            v-model="selectedVariant"/>
                            
                        <ProductVariantColorMode v-else-if="variant.type === 'COLOR_MODE'"
                            :variant="variant" 
                            inputRadioGroupName="product-variant" 
                            v-model="selectedVariant"/>

                        <ProductVariantThumbnailMode v-else-if="variant.type === 'THUMBNAIL_MODE'"
                            :variant="variant" 
                            inputRadioGroupName="product-variant" 
                            v-model="selectedVariant"/>
                   
                    </li>
                </ul>
            </div>
            <p v-if="product" class="text-neutral text-md font-light">{{ product.variations[selectedVariantIndex].variant_description||product.description }}</p>
            <div>
                <div class="flex gap-1 py-4">
                    <p class="line-through text-neutral">{{ product?.variations[selectedVariantIndex].price_currency_symbol }}{{ product?.variations[selectedVariantIndex].price_amount.toFixed(2) }}</p>
                    <span class="badge badge-outline badge-success text-xs border-dashed">100% OFF!</span>
                </div>
                
                <p class="font-bold text-2xl text-accent flex items-center">
                    <span class="text-xl font-semibold">{{ product?.variations[selectedVariantIndex].price_currency_symbol }}</span>
                    <span>{{ product?.variations[selectedVariantIndex].price_amount.toFixed(2) }}</span>
                </p>
            </div>

            <div>
                <p class="text-xs font-light text-white mb-3 bg-accent w-max px-2 py-1" v-if="!isVariantSoldOut">
                    <span class="font-black">{{  selectedVariantSupplyLeft+' ' }}</span>
                    <span v-if="selectedVariantSupplyLeft > 1">pieces left!</span>
                    <span v-else>piece left!</span>
                </p>
                <p class="text-xs font-bold text-white mb-3 bg-accent w-max px-2 py-1" v-else>
                    <span>SOLD OUT!</span>
                </p>
            </div>

    
            <div class="w-full">
                <button class="btn btn-primary font-bold" :disabled="isVariantSoldOut" @click="initializeItemToCart">ADD TO CART</button>
            </div>

            <div class="w-full">
                <div class="divider"></div>
                <div>
                    <h2 class="font-normal text-sm mb-5">BROUGHT TO YOU BY:</h2>
                    <img src="/logo.svg" alt="" class="w-[150px] object-contain">
                    <!-- <p class="font-normal text-sm">Distri Gate Original</p> -->
                </div>
            </div>
            
        </div>
        <AddToCartViewer/>

    </div>
</template>

<script setup lang="ts">
    import { UseImage } from '@vueuse/components';
    import type { Product, ProductVariation } from '~/types';

    
    const route = useRoute()
    const id = route.params.id

   

    const { data:product, pending, error, refresh } = await useFetch<Product>(`/api/products/${id}`,{
        server:false
    })

    const selectedVariantIndex = computed(()=>{
        if(selectedVariant.value && product.value){
            return useIndexFromItemId(selectedVariant.value,product.value.variations)
        }else return 0
    })

    const selectedVariantSupplyLeft = computed(()=> product.value?.variations[selectedVariantIndex.value].supply_quantity??0)

    const selectedVariant = ref<number|undefined>(undefined)

    const isVariantSoldOut = computed(()=>selectedVariantSupplyLeft.value<1)

    const itemForCart = useItemForCart()

    const initializeItemToCart = ()=> {
        if(!product.value) return
        itemForCart.value = {
            variantId: product.value.variations[selectedVariantIndex.value].id,
            productId: product.value.id,
            productTitle: product.value.title,
            quantity: 1,
            productVariant: product.value.variations[selectedVariantIndex.value],
            selectedVariantIndex: selectedVariantIndex.value,
            selected: false
        }
    }

    onMounted(() => {
        const waitProduct = setInterval(()=>{
            if(product.value){
                selectedVariant.value = product.value.default_variant
                clearInterval(waitProduct)
            }
        },1000)
        
    })

</script>

<style scoped>

</style>