import type { PrivateUser } from "~/types"

export default defineEventHandler(async (event):Promise<PrivateUser>=> {
    console.log('called')
    const username = getRouterParam(event, 'username')

    const api = serverAPI(event)

    const response = await api.get(`/api/users/get_private_user/${username}`)
  
    return response as unknown as PrivateUser
})