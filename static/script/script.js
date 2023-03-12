let cowsWait = []
const timerIncr = 1
const testTimerEnd = [2023, 03, 12, 15, 11]

document.addEventListener("DOMContentLoaded", handlerDOMContentLoaded)

function handlerDOMContentLoaded() {
  const cows = document.getElementsByClassName('cow')
  const myScore = document.getElementById('my-score')

  for(const cow of cows){ 
    cow.addEventListener('click', handlerClickOnCow)
  }

  function handlerClickOnCow(event) {
    event.target.classList.add('cow-disable')
    // const cowNumber = event.target.dataset.cowNumber
    const deadline = Date.parse(new Date()) + 6 * 1000*60*60
    // const deadline = new Date(...testTimerEnd)
    initializeClock(event.target, deadline);
    myScore.innerHTML = ++myScore.innerHTML
  }
}

function getTimeRemaining(endtime){
  let ifEnd = false
  const t = endtime - Date.parse(new Date())
  const seconds = Math.floor( (t/1000) % 60 )
  const minutes = Math.floor( (t/1000/60) % 60 )
  const hours = Math.floor( (t/(1000*60*60)) % 24 )
  // var days = Math.floor( t/(1000*60*60*24) );
  if(hours === 0 && minutes === 0 && seconds === 0) {
    ifEnd = true
  }
  return {
    ifEnd: ifEnd,  
    time: `${hours}:${minutes}:${seconds}`,  
  }
}

function initializeClock(target, endtime){  
  const timeinterval = setInterval(function() {  
    const t = getTimeRemaining(endtime)
    target.innerHTML = t.time
    if(t.ifEnd){
      clearInterval(timeinterval)
      target.classList.remove('cow-disable')
      target.innerHTML = ''
    }  
  },1000);  
}