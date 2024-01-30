export default defineEventHandler(async (event)=> {
    const dataFromClient = await readFormData(event)

    const api = serverAPI(event)

    await api.post('/api/products/add_new_product/',{
        body: dataFromClient
    })

    
    return {
        data: 'body'
    }
})