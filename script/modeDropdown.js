{
    const drop = document.querySelector('.modal_dropdown');
    const wrapper = document.querySelector('.user_profile-wrapper');

    wrapper.addEventListener('click', e => {
        const target = e.target;
        (target.className === 'fas fa-ellipsis-v') ? drop.classList.add('active'): drop.classList.remove('active');
        
       
    })

}

