<template>
<div class="bg-white p-5 rounded-lg shadow-lg w-[650px] h-max">
    <div class="divider mb-10 px-20">
        <h2 class="text-center text-lg font-bold">CART</h2>
    </div>
    
    <div class="overflow-x-auto">
        <table class="table">
            <!-- head -->
            <thead>
            <tr>
                <th>
                <label>
                    <input type="checkbox" class="checkbox" v-model="allItemsSelected"/>
                </label>
                </th>
                <th>PRODUCT</th>
                <th class="text-center">QTY</th>
                <th>TOTAL</th>
                <th>
                    <div class="tooltip font-light hover:tooltip-open tooltip-left" data-tip="Remove selected items">
                        <button class="btn btn-ghost btn-sm" @click="removeSelectedItems()">
                            <svg class="w-4 h-4" version="1.1" id="svg2" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" sodipodi:docname="remove.svg" inkscape:version="0.48.4 r9939" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1200 1200" enable-background="new 0 0 1200 1200" xml:space="preserve" fill="#000000"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path id="path18404" inkscape:connector-curvature="0" d="M0,264.84L335.16,600L0,935.16L264.84,1200L600,864.84L935.16,1200 L1200,935.16L864.84,600L1200,264.84L935.16,0L600,335.16L264.84,0L0,264.84z"></path> </g></svg>
                        </button>
                    </div>
                </th>
            </tr>
            </thead>
            <TransitionGroup tag="tbody" name="list">
            
            <!-- row 1 -->
            <tr v-for="item in cartstore.items" :key="item.variantId">
                <CartTableItem :item="item"/>
            </tr>
        
            </TransitionGroup>
         
            <!-- foot -->
            <!-- <tfoot class="h-96">
            <tr>
                <th></th>
                <th>PRODUCT</th>
                <th>QTY</th>
                <th>TOTAL</th>
                <th></th>
            </tr>
            </tfoot> -->
            
        </table>
    </div>
</div>
</template>





<script setup lang="ts">

    const cartstore = useCart()
    const allItemsSelected = ref(false)

    watch(allItemsSelected,(value)=> {
        cartstore.items.forEach(item=>item.selected = value)
    },{deep:true})

    const removeSelectedItems = () => {
        const selectedItems = cartstore.items.filter(item=>item.selected)
        selectedItems.forEach(selectedItem => cartstore.removeItem(selectedItem.variantId))

        allItemsSelected.value = false
    }

</script>





<style scoped>

.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(-30px);
}

</style>