document.addEventListener("DOMContentLoaded", handlerDOMContentLoaded)

function handlerDOMContentLoaded() {
  const cows = document.getElementsByClassName('cow')
  const myScore = document.getElementById('my-score')

  for(const cow of cows){ 
    cow.addEventListener('click', handlerClickOnCow)
  }

  function handlerClickOnCow(event) {
    event.target.classList.add('cow-disable')
    event.target.dataset.cowNumber
    myScore.innerHTML = ++myScore.innerHTML
  }
}