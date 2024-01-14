import { skipHydrate } from "pinia"
import type { PrivateUser, AddressSubmit } from "~/types"

export const useUserStore = defineStore('userStore', ()=> {



    const currentUser = useLocalStorage<PrivateUser>('currentUser', {} as PrivateUser)


    const fetching = useLocalStorage<boolean>('fetching',false)

    const exiting = useLocalStorage<boolean>('exiting',false)


    const isAuthenticated = computed(()=>Object.keys(currentUser.value).length > 0)

    const toAuthenticate = ref(false)



    const setUser = async(username:string) => {
        const { data, pending, error, refresh } = await useFetch(`/api/auth/${username}`,{})
        fetching.value = pending.value
      
        currentUser.value = data.value as PrivateUser
        return { pending, error}
    }



    const clearUser = async () => {
        exiting.value = true
        const { pending,error } = await useFetch('/api/auth/logout', { 
            method: 'POST',
            body: {
                username: currentUser.value.username
            },
            onRequestError(error){
                console.log(error)
            }
        })
       
        currentUser.value = {} as PrivateUser
        exiting.value = pending.value
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





    return { 
        currentUser:skipHydrate(currentUser),
        fetching:skipHydrate(fetching),
        isAuthenticated:skipHydrate(isAuthenticated),
        exiting,
        toAuthenticate,

        setUser,
        clearUser,
        changeUserAddress,
        changeUserAddressById
     }

})