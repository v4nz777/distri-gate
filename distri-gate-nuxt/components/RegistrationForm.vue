<template>
    <div class="card bg-base p-10 gap-5 shadow-xl max-w-[350px] w-full bg-white">
        <div class="w-full">
            <LogoAnimationLoading class="w-full"/>
            <h2 for="" class="text-center text-primary font-black text-2xl w-full">DISTRI GATE</h2>
        </div>
        
        <input type="text" placeholder="Username" class="input input-bordered w-full max-w-xs" v-model="username"/>
        <input type="password" placeholder="Password" class="input input-bordered w-full max-w-xs" v-model="password"/>
        <input type="password" placeholder="Confirm Password" class="input input-bordered w-full max-w-xs" v-model="confirm"/>
        <input type="text" placeholder="Email" class="input input-bordered w-full max-w-xs" v-model="email"/>
        <button class="btn" :class="username && password?'btn-primary':'btn-disabled'" @click="register()">
            <span class="loading loading-spinner loading-xs text-white" v-if="loading"></span>
            <span class="" v-else>REGISTER</span>
        </button>
        <div class="divider h-4">
            OR
        </div>
        <a class="link link-hover text-center" @click="emits('login-clicked')">LOGIN</a>
    </div>
</template>

<script setup lang="ts">
    const emits = defineEmits(['success', 'login-clicked'])

    const userstore = useUserStore()
    const alertstore = useAlertStore()

    const loading = ref(false)

    const username = ref('')
    const password = ref('')
    const confirm = ref('')
    const email = ref('')


    
    const register = async () => {

        if(!loading.value){
            loading.value=true
            debugger
            // await getAccessToken(username.value,password.value)
            let res = await userstore.createUser({
                username: username.value,
                password: password.value,
                confirm: confirm.value,
                email: email.value
            })
            debugger
            loading.value=false
            // userstore.loggedUser = username.value
            
            // if(userstore.isAuthenticated){
            //     emits('success')
            //     alertstore.addAlert({message:`Welcome ${username.value}`, type: 'success', shown:true, id:'temp'})
            // }
            // else alertstore.addAlert({message:'Wrong credentials', type: 'error', shown:true, id:'temp'})

            username.value = ''
            password.value = ''
            confirm.value = ''
            email.value = ''
        }
    }

</script>

<style scoped>

</style>