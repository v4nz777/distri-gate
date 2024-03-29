<template>
    <div class="bg-white w-[400px] h-max shadow-md rounded-md">

        <div class="w-full p-2">
            <div class="flex justify-start gap-1 text-sm text-black-500 font-bold m-5 border-b-2">
                <p class="text-lg">SHIPPING INFORMATION</p>
            </div>
            
            <div class="p-5 grid grid-cols-1 gap-2" v-if="userstore.currentUser">
                <input type="text" placeholder="Full Name" class="input input-sm input-bordered w-full max-w-xs" v-model="form_contact_person" :disabled="!newAddressMode"/>
                <input type="text" placeholder="Contact number" class="input input-sm input-bordered w-full max-w-xs" v-model="form_contact_number" :disabled="!newAddressMode"/>
            </div>

            <div class="p-5 grid grid-cols-1 gap-2">
                <div class="divider my-0 w-full max-w-xs text-sm font-semibold">
                    ADDRESS
                </div>

                <Transition>
                <select class="select select-sm select-bordered w-full max-w-xs" v-model="selectedAddress" v-if="!newAddressMode"
                    @change="userstore.changeUserAddressById(selectedAddress as number)">
                    <option class="text-sm" disabled :selected="!userstore.currentUser?.address_current">Select from existing...</option>
                    <option class="text-sm" v-for="address_item in userstore.currentUser?.address" 
                        :key="address_item.id" 
                        :value="address_item.id">
                      
                        {{ address_item.full_address_string }} 
                    </option>
                </select>
                </Transition>
                
                <Transition>
                <button v-if="!newAddressMode" class="btn btn-xs btn-ghost text-secondary w-max" @click="newAddressMode=true">Enter a new address</button>
                </Transition>

                <Transition>
                    <div class="w-full grid grid-cols-1 gap-2" v-if="newAddressMode">
                        <input type="text" v-model="form_address_line" placeholder="Adress line 1..." class="input input-sm input-bordered w-full max-w-xs" />
                        <input type="text" v-model="form_street" placeholder="Street/Barangay" class="input input-sm input-bordered w-full max-w-xs" />
                        <input type="text" v-model="form_city" placeholder="City" class="input input-sm input-bordered w-full max-w-xs" />
                        <input type="text" v-model="form_postal_code" placeholder="Postal Code" class="input input-sm input-bordered w-full max-w-[8rem]" />
                        <input type="text" v-model="form_province" placeholder="Province" class="input input-sm input-bordered w-full max-w-xs" />
                        <input type="text" v-model="form_country" placeholder="Country" class="input input-sm input-bordered w-full max-w-xs" />
                        <div class="flex justify-between w-full max-w-xs">
                            <button class="btn btn-ghost w-max btn-xs btn-secondary text-secondary" @click="newAddressMode=false">Select from recent</button>
                            <div>
                                <span class="loading loading-spinner loading-sm text-secondary" v-if="userstore.fetching"></span>
                                <button v-else class="btn w-max btn-xs btn-secondary text-white relative" :disabled="!newAddressReady"
                                    @click="applyAddress">
                                    <span class="animate-ping absolute inline-flex w-full h-full rounded-full bg-secondary opacity-75" v-if="formModified&&newAddressReady"></span>
                                    Save & apply
                                </button>
                            </div>
                        </div>
                    </div>
                </Transition>
            </div>


            
            <div class="p-5 grid grid-cols-1 gap-2 mt-5">
                <div class="bg-orange-50 text-secondary p-2 min-h-[100px] max-w-xs border-secondary border-2 border-dashed text-sm">
                    <div class="w-full h-full flex justify-center items-center" v-if="userstore.fetching">
                        <span class="loading loading-bars loading-md"></span>
                    </div>
                    <div class="w-full h-full" v-else>
                        <p class="font-bold">{{ userstore.currentUser?.address_current?.contact_person??userstore.currentUser?.full_name??'' }}</p>
                        <p>{{ userstore.currentUser?.address_current?.full_address_string }}</p>
                        <p>{{ userstore.currentUser?.address_current?.contact??userstore.currentUser?.contact_number??'' }}</p>
                    </div>
                    
                    

                </div>
                <span class="text-xs font-thin text-secondary">ⓘ Check the shipping information before you proceed</span>
            </div>
            

            <div class="flex justify-center gap-5 border-t p-5">
                <button class="btn btn-sm btn-ghost" @click="emits('backwards')">GO BACK</button>
                <button class="btn btn-sm btn-primary" @click="emits('forwards')">PROCEED TO PAYMENT</button>
            </div>
            
           
        </div>
    </div>
</template>

<script setup lang="ts">


    const emits = defineEmits(['backwards','forwards'])
    const userstore = useUserStore()
    const cartstore = useCart()

    const selectedAddress = ref<string|number|null>(null)
    const newAddressMode = ref(false)

    const form_contact_person = ref(userstore.currentUser?.address_current?.contact_person??userstore.currentUser?.full_name??'')
    const form_contact_number = ref(userstore.currentUser?.address_current?.contact??userstore.currentUser?.contact_number??'')
    const form_address_line = ref('')
    const form_street = ref('')
    const form_city = ref('')
    const form_postal_code = ref('')
    const form_province = ref('')
    const form_country = ref('')

    const newAddressReady = computed(()=> {
        return (
            form_address_line.value &&
            form_street.value &&
            form_city.value &&
            form_postal_code.value &&
            form_province.value &&
            form_country.value
        )
    })

    const applyAddress = async ()=> {
        await userstore.changeUserAddress({
            form_contact_person: form_contact_person.value,
            form_contact: form_contact_number.value,
            form_address_line: form_address_line.value,
            form_street: form_street.value,
            form_city: form_city.value,
            form_postal_code: form_postal_code.value,
            form_province: form_province.value,
            form_country: form_country.value,
        })
        formModified.value = false
    }

    onMounted(async() => {
        await nextTick()
        if(userstore.currentUser && userstore.currentUser.address_current){
            newAddressMode.value = false
            selectedAddress.value = userstore.currentUser.address_current.id
        }
        else newAddressMode.value = true
    })

    const formModified = ref(false)
    const newAddressForm = computed(()=>{
        return {
            form_contact_person: form_contact_person.value,
            form_contact: form_contact_number.value,
            form_address_line: form_address_line.value,
            form_street: form_street.value,
            form_city: form_city.value,
            form_postal_code: form_postal_code.value,
            form_province: form_province.value,
            form_country: form_country.value,
        }
    })

    

    watch(newAddressForm, (oldValue,newValue)=> {
        if(oldValue===newValue)formModified.value=false
        else formModified.value = true
    })


    watch(()=>userstore.currentUser, ()=>{
        form_contact_person.value = userstore.currentUser?.address_current?.contact_person??userstore.currentUser?.full_name??''
        form_contact_number.value = userstore.currentUser?.address_current?.contact??userstore.currentUser?.contact_number??''
    },{deep:true})


</script>

<style scoped>
    .v-enter-active,
    .v-leave-active {
    transition: opacity 0.9s ease;
    }

    .v-enter-from,
    .v-leave-to {
    opacity: 0;
    scale: 0%;
   
    }
</style>