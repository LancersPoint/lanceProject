{
    const modal = document.querySelector('.modal_dropdown');
    const container = document.querySelector('.dispute_inbox_container');

    container.addEventListener('click', e => {
        const target = e.target;
        (target.className === 'fas fa-chevron-down') ? modal.classList.add('active'): modal.classList.remove('active');
        
       
    })

}




