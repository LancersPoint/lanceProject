const modal = document.querySelector(".modal");
const closeModalBtn = document.querySelector(".modal_back");
const openModalBtn = document.querySelectorAll(".popup");
const overlay = document.querySelector(".overlay");

for(i = 0; i<openModalBtn.length; i++)
openModalBtn[i].addEventListener('click', function(){
    modal.classList.remove('hidden');
    overlay.classList.remove('hidden');
    closeModalBtn.classList.remove('')
});


const closeModal = function(){
    modal.classList.add('hidden');
    overlay.classList.add('hidden');
};
    

closeModalBtn.addEventListener('click',closeModal );

overlay.addEventListener('click', closeModal);

document.addEventListener('keydown', function(e){
    console.log(e.key);
    if(e.key === 'Escape'){
        modal.classList.add('hidden');
        overlay.classList.add('hidden');
    }
});



