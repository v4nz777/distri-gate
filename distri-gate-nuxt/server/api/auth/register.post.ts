import type { AccessToken } from "~/types"

export default defineEventHandler(async (event)=>{

    const { username, password, email } = await readBody(event)
    const api = serverAPI(event)

    debugger
    const response = await api.post('/api/users/register_user/',{
        body: {
            username,
            password,
            email
        }
    }) as any

    //setCookie(event,'Authorization', response.access_token, { httpOnly:true } )
    debugger
    return {message: 'Registration sucess!'}
})


