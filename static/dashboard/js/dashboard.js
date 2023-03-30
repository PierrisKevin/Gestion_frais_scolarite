function chiffreLoad(elem,elemVal, n=0){
    if (elemVal>=n){
        elem.textContent=n
        setTimeout(()=>{chiffreLoad(elem,elemVal,n+10)},1)
    }
}

const allInfo = document.querySelectorAll("#info-business div p:nth-child(2)")
allInfo.forEach((info)=>{
    window.addEventListener("load",chiffreLoad(info,parseInt(info.textContent)))
})
