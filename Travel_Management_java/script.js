const warpper = document.querySelector('warpper');
const busPage = document.querySelector('.bus-page');
const homePage = document.querySelector('.home-page');
const nextBusPage = document.querySelector('.nx-btn');

warpper.classList.remove('home');

busPage.addEventListener('click',()=>{
    warpper.classList.remove('next-bus');
    warpper.classList.add('prev-bus');
    warpper.classList.remove('home');
})

homePage.addEventListener('click',()=>{
    warpper.classList.remove('next-bus');
    warpper.classList.remove('prev-bus');
    warpper.classList.add('home');
    // warpper.classList.add('close-next-bus');
    // warpper.classList.add('close-prev-bus');
})

nextBusPage.addEventListener('click',()=>{
    warpper.classList.remove('prev-bus');
    warpper.classList.remove('home');
    warpper.classList.add('next-bus');
})
