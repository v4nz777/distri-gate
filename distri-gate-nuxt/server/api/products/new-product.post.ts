export default defineEventHandler(async (event)=> {
    const data = await readFormData(event)
    
    return {
        data: 'body'
    }
})