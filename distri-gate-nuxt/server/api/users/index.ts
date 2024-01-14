import type { User } from "~/types"

export default defineEventHandler(async(event):Promise<User[]>=> {
    const api = serverAPI(event)

    const response = await api.get('/api/users/get_users')

    return response as User[]
})