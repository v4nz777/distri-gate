<template>
    <dialog class="modal" ref="exitingDialog">
        <LogoutUI @loggingOut="exitingDialog?.showModal()" @exited="exitingDialog?.close()"/>
    </dialog>
</template>

<script setup lang="ts">
    const exitingDialog = ref<HTMLDialogElement>()
</script>

<style scoped>

</style>