import type { Item,GiftCode } from "@/types"
import { skipHydrate } from "pinia"
import { useAlertStore } from "./alerts"

export const useCart = defineStore('cart-store', ()=> {

        const alertstore = useAlertStore()
        const userstore = useUserStore()

        // STATES
        const cartOwner = useLocalStorage<string|null>('cartOwner', null)
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
            items.value.forEach((item:Item)=>{
                price += (item.productVariant.price_amount??0) * item.quantity
            })
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

                const foundIndex = items.value.findIndex((i)=>i.variantId === newItem.variantId)
                
                setLoggedUserAsCartOwner() //

                if(foundIndex > -1){ // Avoid duplication
                    items.value[foundIndex].quantity += newItem.quantity
                    resolve('exists')
                }else {
                    items.value.push(newItem)
                    resolve('new')
                }

            })
        }

        const changeQuantity = (id:string, action:string) => {
            const foundIndex = getMyIndex(id)
            if(action === 'increase') increaseQuantity(id)
            else if(action === 'decrease')decreaseQuantity(id)

            if(items.value[foundIndex].quantity < 1) removeItem(id)
        }

        const increaseQuantity = (variantId:string)=> {
            const foundIndex = getMyIndex(variantId)

            const variantSupply = items.value[foundIndex].productVariant.supply_quantity
            const quantityFromCart = getItemCountFromCart(variantId)
            if(variantSupply - quantityFromCart < 1){
                alertstore.addAlert({
                    id:'temp',
                    type:'error',
                    message:`Limited supply! Max ${variantSupply} per purchase.`,
                    shown: true
                })
                return
            }

            items.value[foundIndex].quantity ++
        }

        const decreaseQuantity = (variantId:string)=> {
            const foundIndex = getMyIndex(variantId)
            items.value[foundIndex].quantity--
        }



        const removeItem = (id:string) => {
            const foundIndex = getMyIndex(id)
            items.value.splice(foundIndex,1)

           
        }

        const getMyIndex = (id:string) => items.value.findIndex((i:Item)=>i.variantId === id)

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

        const getItemCountFromCart = (itemId:string)=> {
            return items.value[getMyIndex(itemId)]?.quantity
        }


        const setLoggedUserAsCartOwner = ()=>{
            cartOwner.value = userstore.loggedUser
        }


        const reset =  ()=> {
            items.value = [] as Item[]
            cartGiftCode.value = ''
            discount.value = 0
            tax.value = 2.0
            cartIsNavigated.value = false
            cartOwner.value = null
        }


    // SIDE EFFECTS
        
        //Redirect to product page if cart is empty 
        watch(items,(value:Item[])=>{
            if(value.length < 1)navigateTo('/products')
        },{deep:true})


        watch(()=>userstore.loggedUser, (newValue)=>{
            if(newValue && cartOwner.value && newValue!==cartOwner.value) reset()
        })

 
 


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
        getItemCountFromCart,
        setLoggedUserAsCartOwner,
        reset

    }
})
