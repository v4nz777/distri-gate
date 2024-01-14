import type { AccessToken } from "~/types"

export default defineEventHandler(async (event)=>{

    const { username, password } = await readBody(event)
    const api = serverAPI(event)

    
    const response = await api.post('/api/users/login/',{
        body: {
            username,
            password
        }
    }) as unknown as AccessToken

    setCookie(event,'Authorization', response.access_token, { httpOnly:true } )
    return {message: 'Login success!'}
})


