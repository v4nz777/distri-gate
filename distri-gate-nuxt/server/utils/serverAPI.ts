import { H3Event } from 'h3'
import Client from '~/utils/api/client'

export const serverAPI =  (event:H3Event) => {
    const { baseURL } = useRuntimeConfig()

    const accessToken = getCookie(event,'Authorization')

    const client = new Client(baseURL, {
        headers: {
            'Authorization':   `Bearer ${ accessToken }`
        } as HeadersInit
    })

    return client
}