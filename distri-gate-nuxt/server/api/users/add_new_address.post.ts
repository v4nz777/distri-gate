import type { AddressSubmit, PrivateUser } from "~/types"

export default defineEventHandler(async(event)=>{
    const api = serverAPI(event)

    const body = await readBody(event)
    const response = await api.post('/api/users/add_new_address/', {
        body: body as AddressSubmit
    })
    return response as PrivateUser
})