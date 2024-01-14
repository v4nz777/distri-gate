export default defineNuxtRouteMiddleware((to,from)=> {
    const alerstore = useAlertStore()

    // Hide all alerts when navigating to next
    alerstore.alerts.forEach((alert)=>{
        if(alert.type!=='sticky')alerstore.hideAlert(alert.id)
    })
})