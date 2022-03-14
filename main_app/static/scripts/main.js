console.log("who are you and why are you looking at the console for my app?")
const URL = 'https://api.adviceslip.com/advice'
const dateThing = document.getElementById('date-picker')
const advisor = document.getElementById('advisor')
let advice = ''
const options = {
    method: "GET",
    headers: {},
}
if (dateThing){
    setDate()
}

if (advisor){
    getAdvice()
}

function setDate(){
    newDate = new Date()
    finalFormatted = ''
    formatted = newDate.toLocaleString('swe-FR', {
        day: '2-digit',
        year: 'numeric',
        month: '2-digit'
    })
    for (let i = 0; i < formatted.length; i++){
        if (formatted[i] === '/'){
            finalFormatted += '-'
        } else {
            finalFormatted += formatted[i]
        }

    }
    
    dateThing.value = finalFormatted
    
}

function getAdvice(){
    fetch(URL, options).then((resp) => {
        resp.json().then((data) => {
        advisor.innerText = data.slip.advice
        })
    })
}