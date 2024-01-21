export default (id:string|number, targetArray:Array<any>)=>{
    return targetArray.findIndex((target)=>target.id===id)
}
