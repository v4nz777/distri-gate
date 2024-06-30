import { skipHydrate } from "pinia"
import type { PrivateUser, AddressSubmit } from "~/types"

export const useUserStore = defineStore('userStore', ()=> {


    const cartstore = useCart()


    const loggedUser = useLocalStorage<string>('loggedUser', null)

    const currentUser = ref<PrivateUser|null>(null)

    const fetching = ref<boolean>(false)

    const exiting = ref<boolean>(false)
    
    const isAuthenticated = computed(():boolean=>currentUser.value !== null && currentUser.value !== undefined)

    const loginDialogTrigger = ref(false)



    const setUser = async(username:string) => {
        if(!username)return

        const { data, pending, error, refresh } = await useFetch(`/api/auth/${username}`,{})
        fetching.value = pending.value
        currentUser.value = data.value as PrivateUser

        return currentUser.value
    }
    interface NewUser {
        username: string
        password:string
        confirm:string
        email:string
    }

    const createUser = async(inputData:NewUser) => {
        debugger
        if(inputData.password !== inputData.confirm){
            alert('Error @42: Password didnt match');
            return
        }
            
        if(!inputData.username || !inputData.email || !inputData.password){
            alert('Error @47: Invalid form, some required fields are empty');
            return
        }

        const { data, pending, error, refresh } = await useFetch(`/api/auth/register`,{
            method: 'POST',
            body: {
                username: inputData.username,
                password: inputData.password,
                email: inputData.email
            },

            onResponseError({request,response,options}){
                throw Error(response.statusText)
            },
            onResponse({request,response,options}){
                return response
            }
        })
        fetching.value = pending.value
        //currentUser.value = data.value as any
        debugger
        return data
    }



    const clearUser = async () => {
        exiting.value = true
        const { pending,error } = await useFetch('/api/auth/logout', { 
            method: 'POST',
            body: {
                username: currentUser.value?.username
            },
            onRequestError(error){
                console.log(error)
            }
        })
       
        currentUser.value = null
        cartstore.reset()
        exiting.value = pending.value
        loggedUser.value = null
    }

    const changeUserAddress = async (address:AddressSubmit)=> {
        fetching.value = true
        const { data, pending, error, refresh } = await useFetch('/api/users/add_new_address',{
            method: 'POST',
            body: address
        })

        fetching.value = pending.value

        currentUser.value = data.value as unknown as PrivateUser
    }

    const changeUserAddressById = async (addresId:number|null)=> {
        if (!addresId) return
        fetching.value = true
        const { data, pending, error, refresh } = await useFetch('/api/users/change_address', {
            method: 'POST',
            body: {
                address_id: addresId
            }
        })

        fetching.value = pending.value

        currentUser.value = data.value as unknown as PrivateUser
    }


    
    /** Needs to have:
     * - DialogModal `<dialog>` element with login form
     * - Dialog element must be put inside a layout component
     * - Must call `hideLoginFormDialog` function every successful login
     * - the hide function must be called within the login function
     * - Finally, must have a watcher to watch the `loginDialogTrigger` and call this function if `true`
     * - Put the watcher a component where the `<dialog>` is located
     */
    const showLoginFormDialog = ()=> {
        loginDialogTrigger.value = true
    }

    const hideLoginFormDialog = ()=> {
        loginDialogTrigger.value = false
    }





    return { 
        currentUser:skipHydrate(currentUser),
        fetching:skipHydrate(fetching),
        isAuthenticated:skipHydrate(isAuthenticated),
        loggedUser:skipHydrate(loggedUser),
        exiting,
        loginDialogTrigger,

        setUser,
        createUser,
        clearUser,
        changeUserAddress,
        changeUserAddressById,
        showLoginFormDialog,
        hideLoginFormDialog
     }

})