export const getAccessToken =  async (username:string, password:string)=> {
    if(!username && !password) throw Error('Invalid form value')
    
    const { data, pending, error, refresh } = await useFetch('/api/auth/login',{
        method: 'POST',
        body: {
            username: username,
            password: password
        },

        onResponseError({request,response,options}){
            throw Error(response.statusText)
        },
        onResponse({request,response,options}){
            return response
        }
    })
    // return { data, pending, error, refresh }
}
