export default (delay:number, func:Function)=> {
    return new Promise((resolve,reject)=> {
        setTimeout(() => {
            resolve(func)
        }, delay);
    })
}