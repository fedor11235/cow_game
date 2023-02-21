let cowsWait = []
const timerIncr = 1

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
    setTimer(event.target)
    myScore.innerHTML = ++myScore.innerHTML
  }
}

// TODO исправить таймер
function setTimer(cowTarget) {
  const timeBegan = new Date()
  deadline = new Date(
    timeBegan.getFullYear(),
    timeBegan.getMonth(),
    timeBegan.getDate(),

    timeBegan.getHours(),
    timeBegan.getMinutes() + timerIncr,
    timeBegan.getSeconds(),
    timeBegan.getMilliseconds()
  );
  cowsWait.push({cowTarget: cowTarget, time: deadline})
}

function checkTime() {
  let timeNow = new Date()

  let tempCowsWait = []

  for(const cow of cowsWait) {
    if(timeNow >= cow.time) {
      cow.cowTarget.classList.remove('cow-disable')
      cow.cowTarget.innerHTML = ''
    } else {
      timeLeft = new Date(cow.time - timeNow)
      console.log(timeLeft)
      const [y, hour, minutes, seconds] = [
        timeLeft.getYear(),
        timeLeft.getHours(),
        timeLeft.getMinutes(),
        timeLeft.getSeconds(),
      ]
      const timer = `${y}:${hour}:${minutes}:${seconds}`
      cow.cowTarget.innerHTML = timer
      tempCowsWait.push(cow)
    }
  }
  cowsWait = tempCowsWait
}
window.setInterval( checkTime, 100);