

export default defineEventHandler(async (event)=>{

    const { username } = await readBody(event)
    const api = serverAPI(event)

    
    const response = await api.post('/api/users/logout/',{
        body: { username }
    })

    return response
})


