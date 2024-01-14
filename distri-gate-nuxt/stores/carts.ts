import type { Item,GiftCode } from "@/types"
import { skipHydrate } from "pinia"

export const useCart = defineStore('cart-store', ()=> {

        // STATES
        
        const items = useLocalStorage('cartItems',[] as Item[])
        const cartGiftCode = useLocalStorage('cartGiftCode', '')
        const discount = useLocalStorage('discount',0)
        const tax = useLocalStorage('tax',2.0)
        const cartIsNavigated = useLocalStorage('cartIsNavigated', false)
        const currency = useLocalStorage('currency', {
            symbol: '₱',
            code: 'PHP'
        })

        const shipping = useLocalStorage('shipping', 80)



    // GETTERS
        const cartCount = computed(()=> {
            if(!items.value?.length) return 0

            let count=0
            items.value.forEach((item:Item)=>count += item.quantity)
            return count
        })
        
        const cartSubTotalAmount = computed(()=> {
            let price = 0
            items.value.forEach((item:Item)=>price += (item.product?item.product.price.amount:0) * item.quantity)
            return price
        }) 

        const cartIsEmpty = computed( ():boolean=> !items.value.length)

        const cartTotalAmount = computed(():number=> {
            let total = (cartSubTotalAmount.value + shipping.value)- discount.value
            if(total < 1)total = 0
            return total
        })

        const cartTotalAmountTaxed = computed(():number=> {
            return (tax.value /  100) * cartTotalAmount.value
        })

        const cartTotalAmountWithTax = computed(():number=> {
            return cartTotalAmountTaxed.value + cartTotalAmount.value
        })



    // ACTIONS
        /**  
         * returns string `exists` if already in cart (this will add quantity instead of new item).
         * Otherwise, returns `new`  (this will add new item)
        */
        const addItem = (newItem:Item)=> {
            return new Promise<string>((resolve,reject)=> {    
                const foundIndex = items.value.findIndex((i)=>i.id === newItem.id)
                

                if(foundIndex > -1){ // Avoid duplication
                    items.value[foundIndex].quantity += newItem.quantity
                    resolve('exists')
                }else {
                    items.value.push(newItem)
                    resolve('new')
                }

            })
        }

        const changeQuantity = (id:number, action:string) => {
            const foundIndex = getMyIndex(id)
            if(action === 'increase')items.value[foundIndex].quantity ++
            else if(action === 'decrease')items.value[foundIndex].quantity--

            if(items.value[foundIndex].quantity < 1) removeItem(id)
        }

        const removeItem = (id:number) => {
            const foundIndex = getMyIndex(id)
            items.value.splice(foundIndex,1)

           
        }

        const getMyIndex = (id:number) => items.value.findIndex((i:Item)=>i.id === id)

        /**  Input an Array of valid codes from giftcodes database */
        const validateGiftCode = (sourceValidGiftCodes:GiftCode[]) => {
            
            for(let i in sourceValidGiftCodes){
                const validCode = sourceValidGiftCodes[i]
                if(validCode.code===cartGiftCode.value){
                    discount.value = validCode.discount
                    break;
                }
                else discount.value = 0
            }
        }


        const reset =  ()=> {
            items.value = [] as Item[]
            cartGiftCode.value = ''
            discount.value = 0
            tax.value = 2.0
            cartIsNavigated.value = false
        }


    // SIDE EFFECTS
        
        //Redirect to product page if cart is empty 
        watch(items,(value:Item[])=>{
            if(value.length < 1)navigateTo('/products')
        },{deep:true})


 
 


    return {
        items:skipHydrate(items),
        cartGiftCode:skipHydrate(cartGiftCode),
        discount:skipHydrate(discount),
        tax:skipHydrate(tax),
        cartIsNavigated:skipHydrate(cartIsNavigated),
        currency:skipHydrate(currency),
        shipping:skipHydrate(shipping),



        cartCount,
        cartSubTotalAmount,
        cartIsEmpty,
        cartTotalAmount,
        cartTotalAmountTaxed,
        cartTotalAmountWithTax,

        addItem,
        changeQuantity,
        getMyIndex,
        validateGiftCode,
        removeItem,
        reset

    }
})
