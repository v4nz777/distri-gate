import type { Alert } from "@/types";
import {v4 as uuidv4} from 'uuid';

export const useAlertStore = defineStore('alertStore', ()=> {

    const alerts = ref<Alert[]>([])

    const shownalerts = computed(()=> {
        return alerts.value.filter((i)=>i.shown)
    })

    

    const addAlert = (alert:Alert):void=> {
        const newAlert = {
            id: uuidv4(),
            type: alert.type,
            message: alert.message,
            shown: alert.shown,
            cta_message: alert.cta_message??''
        }

        alerts.value.push(newAlert)
    }


    const hideAlert = (alertId:string)=> {
        const alertIndex = alerts.value.findIndex((alert)=>alert.id === alertId)
        if(alertIndex < 0)return
        
        alerts.value[alertIndex].shown = false
    }


    return {
        
        alerts,

        shownalerts,

        addAlert,
        hideAlert
    }


})