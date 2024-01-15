export default defineNuxtRouteMiddleware(async (to,from)=> {
    
    
    const userstore = useUserStore()
    await userstore.setUser(userstore.loggedUser)

    if(to.name==='login' && userstore.isAuthenticated){
        return navigateTo('/')
    }else return

    
})