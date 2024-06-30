<template>
    <dialog ref="loginForm" class="modal">
        <LoginForm @success="userstore.hideLoginFormDialog()" v-if="mode==='login'" @registration-clicked="mode='registration'"/>
        <RegistrationForm v-else-if="mode==='registration'" @login-clicked="mode='login'"/>
    </dialog>
</template>

<script setup lang="ts">
    const userstore = useUserStore()
    const loginForm = ref<HTMLDialogElement>()
    const mode = ref('login')
    

    onMounted(async () => {
        await nextTick()
        await userstore.setUser(userstore.loggedUser)

        if(!userstore.isAuthenticated){
            userstore.showLoginFormDialog()
        }

        loginForm.value?.addEventListener('keydown', event => {
            if(event.key==='Escape') event.preventDefault()
        })
    })

    watch(()=>userstore.loginDialogTrigger, (value)=> {
        if(value)loginForm.value?.showModal()
        else loginForm.value?.close()
    },{deep:true})

</script>

<style scoped>

</style>