import type { User } from "~/types"

export default defineEventHandler(async (event):Promise<User>=> {

    const username = getRouterParam(event, 'username')

    const api = serverAPI(event)

    const response = await api.get(`/api/users/get_user/${username}`)
  
    return response as User
})