<template>
    <input type="radio" :name="radioGroup" role="tab" class="tab text-primary text-xs" 
        :aria-label="truncateName(tabLabel,7)" 
        :checked="selected"
        v-model="model"
        :value="variantData.id"
        @change="emits('onSelected',variantData.id,photoUrl)"/>
        <!-- <button class="btn btn-xs text-xs w-max">X</button> -->

    
        <div role="tabpanel" class="tab-content bg-base-100 border-base-300 rounded-box p-6 h-max shadow">
        <div class="w-full h-full flex flex-col gap-4">

            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text-alt text-gray-500 font-bold">Variant Name</span>
                </div>
                <input v-model="variantData.name" type="text" placeholder="examples: XXL, Black, 200m" class="input input-sm input-bordered input-base-300 w-full" />
                <div class="label">
                    <span class="label-text-alt">⚠️Keep it as short as possible!</span>
                </div>
            </label>

            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text-alt text-gray-500 font-bold">Description</span>
                </div>
                <textarea v-model="variantData.variationDescription" type="text" 
                            placeholder="This is an example description..." 
                            class="textarea textarea-bordered textarea-xs w-full h-[200px]">
                </textarea>
            </label>

            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text-alt text-gray-500 font-bold">Price Amount</span>
                </div>
                <input v-model="variantData.priceAmount" type="number" placeholder="420" class="input input-sm input-bordered input-base-300 w-full" />
            </label>
            
            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text-alt text-gray-500 font-bold">Available Supply</span>
                </div>
                <input v-model="variantData.availableSupply" type="number" placeholder="360" class="input input-sm input-bordered input-base-300 w-full" />
            </label>

            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text-alt text-gray-500 font-bold">Upload Picture</span>
                </div>
                <button @click="openFileUploader()" class="btn btn-xs shadow w-full">Upload File</button>
            </label>
        
            <label class="form-control w-full">
                <div class="label">
                    <span class="label-text-alt text-gray-500 font-bold">Select Display Mode</span>
                </div>
                <select v-model="variantData.displayMode" class="select select-bordered select-sm w-full text-xs">
                    <option value="NAME_MODE">NAME MODE</option>
                    <option value="COLOR_MODE">COLOR MODE</option>
                    <option value="THUMBNAIL_MODE">THUMBNAIL MODE</option>
                </select>
            </label>

            <label class="form-control w-max" v-if="variantData.displayMode === 'COLOR_MODE'">
                <div class="label">
                    <span class="label-text-alt text-gray-500 font-bold">Pick Color</span>
                </div>
                <input v-model="variantData.variantColor" type="color" class="input input-sm input-bordered input-base-300" />
            
            </label>
            <button v-if="isDefault" class="btn btn-link btn-xs no-underline" @click="emits('onRemoved', variantData.id)">
                <span>
                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fill-rule="evenodd" clip-rule="evenodd" d="M15.7628 9.00012H7.63719C7.18864 9.00012 6.82501 9.37307 6.82501 9.83312V16.5001C6.82501 17.8808 7.91632 19.0001 9.26251 19.0001H14.1375C14.784 19.0001 15.404 18.7367 15.8611 18.2679C16.3182 17.799 16.575 17.1632 16.575 16.5001V9.83312C16.575 9.37307 16.2114 9.00012 15.7628 9.00012Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path fill-rule="evenodd" clip-rule="evenodd" d="M14.625 7.00008L14.5217 6.78908C13.9873 5.69263 12.8947 5 11.6995 5C10.5044 5 9.4118 5.69263 8.8774 6.78908L8.77502 7.00008H14.625Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M10.8247 12.3331C10.8247 11.9189 10.4889 11.5831 10.0747 11.5831C9.66047 11.5831 9.32469 11.9189 9.32469 12.3331H10.8247ZM9.32469 15.6661C9.32469 16.0803 9.66047 16.4161 10.0747 16.4161C10.4889 16.4161 10.8247 16.0803 10.8247 15.6661H9.32469ZM14.0753 12.3331C14.0753 11.9189 13.7396 11.5831 13.3253 11.5831C12.9111 11.5831 12.5753 11.9189 12.5753 12.3331H14.0753ZM12.5753 15.6661C12.5753 16.0803 12.9111 16.4161 13.3253 16.4161C13.7396 16.4161 14.0753 16.0803 14.0753 15.6661H12.5753ZM14.625 6.25012C14.2108 6.25012 13.875 6.58591 13.875 7.00012C13.875 7.41434 14.2108 7.75012 14.625 7.75012V6.25012ZM16.575 7.75012C16.9892 7.75012 17.325 7.41434 17.325 7.00012C17.325 6.58591 16.9892 6.25012 16.575 6.25012V7.75012ZM8.77501 7.75012C9.18923 7.75012 9.52501 7.41434 9.52501 7.00012C9.52501 6.58591 9.18923 6.25012 8.77501 6.25012V7.75012ZM6.82501 6.25012C6.4108 6.25012 6.07501 6.58591 6.07501 7.00012C6.07501 7.41434 6.4108 7.75012 6.82501 7.75012V6.25012ZM9.32469 12.3331V15.6661H10.8247V12.3331H9.32469ZM12.5753 12.3331V15.6661H14.0753V12.3331H12.5753ZM14.625 7.75012H16.575V6.25012H14.625V7.75012ZM8.77501 6.25012H6.82501V7.75012H8.77501V6.25012Z" fill="currentColor"></path> </g></svg>
                </span>
                <span>
                Remove me
                </span>
            </button>

        </div>
    </div>
</template>

<script setup lang="ts">
import { useFileDialog } from '@vueuse/core';
import type { ProductVariationSubmit } from '~/types'
import type { truncateName } from '~/utils';

const model = defineModel()

const props = defineProps<{
    radioGroup: string,
    tabLabel:string,
    variantData:ProductVariationSubmit,
    isDefault:boolean
}>()

const emits = defineEmits(['photoChanged','save', 'onSelected', 'onRemoved'])


// File Upload
const { files, open:openFileUploader, onChange } = useFileDialog({
    accept: 'image/*',
    multiple: false
})

const photoUrl = ref('')
onChange((_files)=>{
    if(!files.value)return
    props.variantData.variantImage = files.value[0]
    photoUrl.value = URL.createObjectURL(files.value[0])
    emits('photoChanged',photoUrl.value)
    
})


const selected = ref(false)
onMounted(() => {
    selected.value=true
    emits('onSelected',props.variantData.id,photoUrl.value)
})


watch(props.variantData,(value)=>{
    // const variantExists = props.referFrom.find(v => v.id===value.id)
    emits('save',props.variantData)
})



</script>




<style scoped>

</style>