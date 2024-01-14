<template>
    <TransitionGroup class="fixed bottom-0 w-max right-0 p-5 grid grid-cols-1 gap-1" tag="ul" name="list">
        <li v-for="alert in alertstore.shownalerts" :key="alert.id">

            <AlertItemTemporary :alert="alert" v-if="alert.type==='temporary'">
                <button class="btn btn-xs btn-outline" @click.once="navigateTo('/cart')">VIEW</button>
            </AlertItemTemporary>

            <AlertItemError :alert="alert" v-else-if="alert.type==='error'">
                <button class="btn btn-xs btn-outline text-white" @click.once="alertstore.hideAlert(alert.id)">CLOSE</button>
            </AlertItemError>

        </li>
        
    </TransitionGroup>
</template>

<script setup lang="ts">
    
    const alertstore = useAlertStore()
    
</script>

<style scoped>
    .list-enter-active,
    .list-leave-active {
    transition: all 0.5s ease;
    }
    .list-enter-from,
    .list-leave-to {
    opacity: 0;
    transform: translateY(-30%);
    }
</style>