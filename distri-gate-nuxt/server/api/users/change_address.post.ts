import type { PrivateUser } from "~/types"

export default defineEventHandler(async(event):Promise<PrivateUser>=> {
    const api = serverAPI(event)
    const { address_id } = await readBody(event)
    const response = await api.post('/api/users/change_current_address',{
        body: {
            address_id
        }
    })
    
    return response as PrivateUser
})