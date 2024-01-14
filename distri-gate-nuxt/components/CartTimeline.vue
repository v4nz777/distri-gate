<template>
<ul class="timeline">

  <li class="">
    <div class="timeline-start btn btn-sm btn-ghost" @click="navigateTo('/cart')">Cart</div>
    <div class="timeline-middle w-5 h-5 bg-base-300 rounded-full" v-if="route.name==='cart'">
      <div class="w-full h-full rounded-full animate-ping bg-orange-300"></div>
    </div>
 

    <div class="timeline-middle">
      <svg v-if="currentStep>1"
        xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5 text-orange-500"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" /></svg>
    </div>

    <hr :class="currentStep>1?'bg-orange-500':''"/>
  </li>




  <li class="">
    <hr :class="currentStep>1?'bg-orange-500':''"/>
    <div class="timeline-start btn btn-sm btn-ghost" @click="navigateTo('/cart/checkout')">Checkout</div>

    <div class="timeline-middle w-5 h-5 bg-base-300 rounded-full" v-if="currentStep<=2"></div>
    <div class="timeline-middle w-5 h-5 bg-orange-300 rounded-full animate-ping" v-if="route.name==='cart-checkout'"></div>
    

      <div class="timeline-middle">
        <svg v-if="currentStep>2"
          xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5 text-orange-500"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" /></svg>
      </div>
      
      <hr :class="currentStep>2?'bg-orange-500':''"/>
  </li>




  <li class="">
    <hr :class="currentStep>2?'bg-orange-500':''"/>
    <div class="timeline-start btn btn-sm btn-ghost" @click="navigateTo('/cart/payment')">Payment</div>

    <div class="timeline-middle w-5 h-5 bg-base-300 rounded-full" v-if="currentStep<=3"></div>
    <div class="timeline-middle w-5 h-5 bg-base-300 rounded-full animate-ping" v-if="route.name==='cart-payment'"></div>
    <div class="timeline-middle">
      <svg v-if="currentStep>3"
        xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5 text-orange-500"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" /></svg>
    </div>
 
    <hr :class="currentStep>3?'bg-orange-500':''"/>
  </li>





  <li class="">
    <hr :class="currentStep>3?'bg-orange-500':''"/>
    <div class="timeline-start btn btn-sm btn-ghost" @click="navigateTo('/cart/complete')">Complete</div>

    <div class="timeline-middle w-5 h-5 bg-base-300 rounded-full" v-if="currentStep<=3"></div>
    <!-- <div class="timeline-middle w-5 h-5 bg-base-300 rounded-full animate-ping" v-if="route.name==='cart-complete'"></div> -->
    <div class="timeline-middle">
      <svg v-if="currentStep>3"
        xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5 text-orange-500"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" /></svg>
    </div>
    
  </li>
  
</ul>
</template>

<script setup lang="ts">
  

  const route = useRoute()
  const router = useRouter()

  /* There are 4 steps in this timeline
    cart        1
    checkout    2
    payment     3
    complete    4
  */
  const currentStep = ref(0)

  onMounted(() => {
   
    if(route.name==='cart')currentStep.value=1
    else if(route.name==='cart-checkout')currentStep.value=2
    else if(route.name==='cart-payment')currentStep.value=3
    else if(route.name==='cart-complete')currentStep.value=4
  })

  router.beforeEach((to,from)=>{
    if(to.name==='cart')currentStep.value=1
    else if(to.name==='cart-checkout')currentStep.value=2
    else if(to.name==='cart-payment')currentStep.value=3
    else if(to.name==='cart-complete')currentStep.value=4

  })


</script>

<style scoped>

</style>