const controls = document.querySelectorAll(".form-control")
function focused(e){
    let parent =  e.target.parentNode
    for (let i=0;i<controls.length;i++){
        controls[i].style.boxShadow = "0 0 0 rgba(0,0,0,.0)"
        controls[i].style.transform = "scale(1)"
        controls[i].style.border = "none"
    }
    parent.style.boxShadow = "0 15px 20px rgba(0,0,0,.3)"
    parent.style.transform = "scale(1.02)"
    parent.style.border = "1px solid rgba(0,0,255,.4)"
}
function error(e){
    // console.log(e.target.parentNode.childNodes[7])
    var element = e.target.value
    if (element.length<5){
        e.target.parentNode.style.border = "2px solid red"
        e.target.parentNode.style.background = "#ff6767"
        e.target.parentNode.childNodes[7].style.opacity ="1"
    }
    else{
        e.target.parentNode.childNodes[7].style.opacity ="0"
        e.target.parentNode.style.border = "none"
        e.target.parentNode.style.background = "#adadff"
    }
}

const evaluate = ["false", "false"]
const inputs = document.querySelectorAll("input")
const button = document.querySelector("form button")
for (let i=0; i<inputs.length;i++){
    inputs[i].addEventListener("keyup", error)
    inputs[i].addEventListener("focus", focused)
}

document.querySelector("form").addEventListener("submit", (e)=>{
    // e.preventDefault()
    // console.log(e.target.childNodes[9].childNodes)
    e.target.childNodes[9].childNodes[1].textContent = "Please wait..."
    e.target.childNodes[9].childNodes[1].style.background = "rgba(46, 46, 255,.6)"
    e.target.childNodes[9].childNodes[1].style.fontSize = ".8em"
    e.target.childNodes[9].childNodes[1].classList.add("inload")
})

document.querySelector(".show").addEventListener("mousedown", (e)=>{
    e.target.parentNode.childNodes[3].setAttribute("type", "text")
})
document.querySelector(".show").addEventListener("mouseup", (e)=>{
    e.target.parentNode.childNodes[3].setAttribute("type", "password")
})