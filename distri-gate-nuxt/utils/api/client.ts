import type { FetchOptions } from 'ofetch'

export default class Client {
    options?: FetchOptions
    baseUrl : string


    constructor(baseUrl:string, options?:FetchOptions){
        this.options = options
        this.baseUrl = baseUrl
    }



    async raw<T>(
        url: string, 
        method: 'GET'|'POST'|'PUT'|'PATCH'|'DELETE'|'OPTIONS'|'HEAD'|'CONNECT'|'TRACE'|'get'|'post'|'put'|'patch'|'delete'|'options'|'head'|'connect'|'trace'|undefined,
        options: FetchOptions
        ):Promise<T>
        {
            try {
                const data = await $fetch.raw<T>(`${this.baseUrl}${url}`, {...options, ...this.options,method})
                return data as T
            }

            catch (error) {
                return Promise.reject(error)
            }
        }
    


    async post<T>(url:string, options?:FetchOptions):Promise<T>
    {
        try {
            const data = await $fetch<T>(`${this.baseUrl}${url}`, {
                ...options,
                ...this.options,
                method: 'POST'
            })
            return data as T
        }

        catch (error) {
            return Promise.reject(error)
        }
    }



    async get<T>(url:string, options?:FetchOptions):Promise<T>
    {
        try {
            const data = await $fetch<T>(`${this.baseUrl}${url}`, {
                ...options,
                ...this.options,
                method: 'GET'
            })
            return data as T
        }

        catch (error) {
            return Promise.reject(error)
        }
    }
    
    
}