export const truncateName = (name:string, maxLength:number):string => {
    return name.length > maxLength ? name.slice(0, maxLength) + '...' : name;
}

export const getIndexFromIdAndArray =  (id:string|number, targetArray:Array<any>):number=>{
    return targetArray.findIndex((target)=>target.id===id)
}