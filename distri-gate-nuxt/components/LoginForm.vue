<template>
    <div class="card bg-base p-10 gap-5 shadow-xl max-w-[350px] w-full bg-white">
        <div class="w-full">
            <LogoAnimationLoading class="w-full"/>
            <h2 for="" class="text-center text-primary font-black text-2xl w-full">DISTRI GATE</h2>
        </div>
        
        <input type="text" placeholder="Username" class="input input-bordered w-full max-w-xs" v-model="username"/>
        <input type="password" placeholder="Password" class="input input-bordered w-full max-w-xs" v-model="password"/>
        <button class="btn" :class="username && password?'btn-primary':'btn-disabled'" @click="login()">
            <span class="loading loading-spinner loading-xs text-white" v-if="loading"></span>
            <span class="" v-else>LOGIN</span>
        </button>
        <div class="divider h-4">
            OR
        </div>
        <a class="link link-hover text-center" @click="emits('registration-clicked')">CREATE ACCOUNT</a>
    </div>
</template>

<script setup lang="ts">
    const emits = defineEmits(['success', 'registration-clicked'])

    const userstore = useUserStore()
    const alertstore = useAlertStore()

    const loading = ref(false)

    const username = ref('')
    const password = ref('')
    
    const login = async () => {

        if(!loading.value){
            loading.value=true

            await getAccessToken(username.value,password.value)
            await userstore.setUser(username.value)

            loading.value=false
            userstore.loggedUser = username.value
            
            if(userstore.isAuthenticated){
                emits('success')
                alertstore.addAlert({message:`Welcome ${username.value}`, type: 'success', shown:true, id:'temp'})
            }
            else alertstore.addAlert({message:'Wrong credentials', type: 'error', shown:true, id:'temp'})

            username.value = ''
            password.value = ''
        }
    }

</script>

<style scoped>

</style>