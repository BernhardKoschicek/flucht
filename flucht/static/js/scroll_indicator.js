window.addEventListener('scroll',()=> indicateScrollBar())

function indicateScrollBar() {
const distanceFromPageTop = document.body.scrollTop || document.documentElement.scrollTop;

const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;

const scrolled = (distanceFromPageTop / height) * 100;

document.querySelector(".scroll-bar").style.width =  `${scrolled}%`;

} 
