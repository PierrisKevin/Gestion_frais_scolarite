const bnt = document.querySelector("#add-student button")
bnt.addEventListener("click", ()=>{
    document.querySelector(".overlay-container").classList.toggle("hidden")
})
document.querySelector(".overlay-student").addEventListener("click", ()=>{
    document.querySelector(".overlay-container").classList.toggle("hidden")
})

const controls = document.querySelectorAll(".form-control")
function focused(e){
    let parent =  e.target.parentNode
    for (let i=0;i<controls.length;i++){
        controls[i].style.boxShadow = "0 0 0 rgba(0,0,0,.0)"
        controls[i].style.transform = "scale(1)"
        // controls[i].style.border = "none"
    }
    parent.style.boxShadow = "0 15px 20px rgba(0,0,0,.3)"
    parent.style.transform = "scale(1.02)"
    // parent.style.border = "1px solid rgba(0,0,255,.4)"
}
const inputs = document.querySelectorAll(".form-control input")
inputs.forEach((input)=>{
    input.addEventListener("focus", focused)
})

const dels = document.querySelectorAll(".delete")
const delCOntainer = document.querySelector(".del-container")
const delLinks = document.querySelector(".choise-del a:nth-child(2)")

const cancel = document.querySelector(".cancel")
dels.forEach((del)=>{
    del.addEventListener("click",(e)=>{
        delCOntainer.classList.remove("hidden")
        console.log("id botton "+ e.target.id)
        delLinks.setAttribute("href", "delete/"+e.target.id)
        console.log(delLinks)
    })
})
cancel.addEventListener("click", ()=>{
    delCOntainer.classList.add("hidden")
})
document.querySelector('input[type="file"]').addEventListener("change",(e)=>{
    let contain_image = document.querySelector(".affiche-image")
    contain_image.innerHTML= ""
    let img = document.createElement("img")
    img.setAttribute("src", "#")
    let [picture] = e.target.files
    img.src=URL.createObjectURL(picture)
    contain_image.appendChild(img)
})

/* Updated fonction */
const allUpdate = document.querySelectorAll(".info-student input")
const selected = document.querySelectorAll(".info-student select")
const updateds = document.querySelectorAll("#btn-update")
const sumbitUpdate = document.querySelector(".updated")
const overlay_change = document.querySelector(".overlay-change")
let updateAuth = true
selected.forEach((select)=>{
    select.disabled=true
})

allUpdate.forEach((update)=>{
    update.disabled = true
})
updateds.forEach((updated)=>{
    updated.addEventListener("click", updateFOrm)
})

function updateFOrm(e){
    let inputs = this.parentNode.parentNode.childNodes
    console.log(this.parentNode.childNodes[5])
    console.log(inputs[13])
    this.parentNode.childNodes[5].classList.remove("hidden")
    if (updateAuth){
        for(let i=1;i<=inputs.length-3;i+=2){
            inputs[i].disabled=false
        }
        inputs[13].disabled=false
        e.target.textContent = "X"
        e.target.style.background = "rgb(255, 68, 68)"
        inputs[1].focus()
        updateAuth=false

        this.parentNode.parentNode.parentNode.parentNode.style.zIndex = "4"
        this.parentNode.parentNode.parentNode.parentNode.style.transform = "scale(1.02)"
    }
    else{
        for(let i=1;i<=inputs.length-3;i+=2){
            inputs[i].disabled=true
        }
        inputs[13].disabled=true
        e.target.textContent = "U"
        e.target.style.background = "var(--primary)"
        updateAuth=true
        this.parentNode.childNodes[5].classList.add("hidden")

        this.parentNode.parentNode.parentNode.parentNode.style.zIndex = "1"
        this.parentNode.parentNode.parentNode.parentNode.style.transform = "scale(1)"
    }
    overlay_change.classList.toggle("hidden")
}